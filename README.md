# G-Scanner – Subdomain Finder by Gopal

**G-Scanner** is a lightweight, Python-based subdomain enumeration tool developed by Gopal (Adavirao) with the assistance of AI. It collects subdomains from multiple OSINT sources using parallel processing to ensure fast and accurate enumeration.

---

## Description

G-Scanner is designed to assist security professionals, bug bounty hunters, and ethical hackers in performing reconnaissance by discovering subdomains associated with a target domain. The tool uses various public data sources and executes requests concurrently to optimize performance.

---

## Features

- Multi-threaded subdomain discovery
- Utilizes 6 publicly available data sources:
  - URLScan.io
  - Anubis
  - HackerTarget
  - AlienVault OTX
  - CertSpotter
  - Facebook Certificate Transparency
- Saves enumerated subdomains to a file (optional)
- Simple CLI interface
- Easily extendable for more sources

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/g-scanner.git
cd g-scanner



 python3 'g-scanner (1).py' -h

 ██████╗  ███████╗  █████╗   ██████╗███╗   ██╗███╗   ██╗███████╗██████╗
██╔════╝  ██╔══██╗██╔══██╗██╔════╝████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║  ███╗ ███████║███████║██║     ██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║   ██║ ██╔══██║██╔══██║██║     ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝ ██║  ██║██║  ██║╚██████╗██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═════╝  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
               Subdomain Finder by Gopal

Usage: python3 g-scanner.py <domain> [-o OUTPUT]
Example: python3 'g-scanner (1).py' testphp.vulnweb.com -o test.txt


## Output

 
 ██████╗  ███████╗  █████╗   ██████╗███╗   ██╗███╗   ██╗███████╗██████╗
██╔════╝  ██╔══██╗██╔══██╗██╔════╝████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║  ███╗ ███████║███████║██║     ██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║   ██║ ██╔══██║██╔══██║██║     ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝ ██║  ██║██║  ██║╚██████╗██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═════╝  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
               Subdomain Finder by Gopal

[*] Enumerating subdomains for: testphp.vulnweb.com
[+] fetch_alienvault: 3 found
[+] fetch_urlscan: 1 found
[+] fetch_facebook_cert: 0 found
[+] fetch_certspotter: 0 found
[+] fetch_anubis: 0 found
[+] fetch_hackertarget: 1 found
[+] Total unique subdomains found: 3
[✓] Subdomains saved to test.txt

sieb-web1.testphp.vulnweb.com
testphp.vulnweb.com
www.testphp.vulnweb.com


Note :- Install Required Library and dependencies
