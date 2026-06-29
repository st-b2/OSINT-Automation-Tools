import re
import requests

def get_emails(url):
    try:
        response = requests.get(url, timeout=10)
        text = response.text
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        return list(set(emails))
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


if __name__ == '__main__':
    url = input("Введите URL для поиска email: ")
    found_emails = get_emails(url)
    
    print(f"\nНайдено email: {len(found_emails)}")
    for email in found_emails:
        print(f"  - {email}")