import requests

def get_whois(domain):
    try:
        url = f"http://ip-api.com/json/{domain}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return {
                    'ip': data.get('query'),
                    'country': data.get('country'),
                    'city': data.get('city'),
                    'isp': data.get('isp'),
                }
        return None
    except:
        return None

def get_dns(domain):
    try:
        url = f"https://dns.google/resolve?name={domain}&type=A"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'Answer' in data:
                ips = []
                for record in data['Answer']:
                    if 'data' in record:
                        ips.append(record['data'])
                return ips
        return []
    except:
        return []

def get_subdomains(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            subdomains = set()
            for entry in data:
                name = entry.get('name_value', '')
                if name and not name.startswith('*'):
                    subdomains.add(name.lower())
            return list(subdomains)[:15]
        return []
    except:
        return []

# Использование
domain = input("Введите домен: ")

print(f"\n{'='*50}")
print(f"Информация о домене: {domain}")
print(f"{'='*50}")


whois = get_whois(domain)
if whois:
    print("\nWHOIS:")
    for key, value in whois.items():
        print(f"  {key}: {value}")


ips = get_dns(domain)
if ips:
    print("\nDNS (A-записи):")
    for ip in ips:
        print(f"  - {ip}")


subs = get_subdomains(domain)
if subs:
    print("\nПоддомены:")
    for sub in subs[:10]:
        print(f"  - {sub}")