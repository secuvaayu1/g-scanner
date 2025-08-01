
#!/usr/bin/env python3

import requests
import argparse
import concurrent.futures
import json
import re
import sys
from bs4 import BeautifulSoup

BANNER = """
 ██████╗  ███████╗  █████╗   ██████╗███╗   ██╗███╗   ██╗███████╗██████╗
██╔════╝  ██╔══██╗██╔══██╗██╔════╝████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║  ███╗ ███████║███████║██║     ██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║   ██║ ██╔══██║██╔══██║██║     ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝ ██║  ██║██║  ██║╚██████╗██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═════╝  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
               Subdomain Finder by Gopal
"""

HEADERS = {'User-Agent': 'Mozilla/5.0 (Gopal Subdomain Finder)'}

def print_help():
    print(BANNER)
    print("Usage: python3 g-scanner.py <domain> [-o OUTPUT]")
    print("Example: python3 g-scanner.py nasa.gov -o nasa_subs.txt\n")

def fetch_urlscan(domain):
    try:
        resp = requests.get(f'https://urlscan.io/api/v1/search/?q=domain:{domain}', headers=HEADERS, timeout=10)
        results = set()
        for r in resp.json().get('results', []):
            results.add(r.get('page', {}).get('domain'))
        return results
    except:
        return set()

def fetch_anubis(domain):
    try:
        resp = requests.get(f"https://jldc.me/anubis/subdomains/{domain}", headers=HEADERS, timeout=10)
        return set(resp.json())
    except:
        return set()

def fetch_hackertarget(domain):
    try:
        resp = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", headers=HEADERS, timeout=10)
        return set(i.split(',')[0] for i in resp.text.splitlines())
    except:
        return set()

def fetch_alienvault(domain):
    try:
        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
        resp = requests.get(url, headers=HEADERS, timeout=10)
        return set(i.get('hostname') for i in resp.json().get('passive_dns', []))
    except:
        return set()

def fetch_certspotter(domain):
    try:
        resp = requests.get(f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names", headers=HEADERS, timeout=10)
        return set(sub for i in resp.json() for sub in i.get('dns_names', []))
    except:
        return set()

def fetch_facebook_cert(domain):
    try:
        resp = requests.get(f"https://developers.facebook.com/tools/ct/search/?domain={domain}", headers=HEADERS, timeout=10)
        return set(re.findall(r'[\w.-]*\.' + re.escape(domain), resp.text))
    except:
        return set()

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("domain", nargs='?', help="Target domain (e.g., nasa.gov)")
    parser.add_argument("-o", "--output", help="Output file to save subdomains")
    parser.add_argument("-h", "--help", action="store_true", help="Show help menu")
    args = parser.parse_args()

    if args.help or not args.domain:
        print_help()
        sys.exit(0)

    domain = args.domain.strip()
    print(BANNER)
    print(f"[*] Enumerating subdomains for: {domain}")

    sources = [
        fetch_urlscan,
        fetch_anubis,
        fetch_hackertarget,
        fetch_alienvault,
        fetch_certspotter,
        fetch_facebook_cert,
    ]

    all_subs = set()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(src, domain): src.__name__ for src in sources}
        for future in concurrent.futures.as_completed(futures):
            src_name = futures[future]
            try:
                results = future.result()
                print(f"[+] {src_name}: {len(results)} found")
                all_subs.update(results)
            except Exception as e:
                print(f"[!] {src_name} error: {e}")

    unique_subs = sorted(set(sub for sub in all_subs if sub and domain in sub))
    print(f"[+] Total unique subdomains found: {len(unique_subs)}")

    if args.output:
        with open(args.output, 'w') as f:
            f.write("\n".join(unique_subs))
        print(f"[✓] Subdomains saved to {args.output}")

if __name__ == "__main__":
    main()
