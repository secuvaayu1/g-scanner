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
