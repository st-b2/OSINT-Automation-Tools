# 🕵️ OSINT Automation Tools

A set of simple scripts to automate the collection of information from open sources (OSINT). The project is being created for educational purposes and is intended to teach the basics of OSINT using Python.

---

## 📚 Contents

- [📖 Project description](#-project-description)
- [🛠️Tools](#️-tools)
  - [🌐 Email Hunter](#-email-hunter)
  - [👤 Username Search](#-username-search)
  - [🌍 Domain Info](#-domain-info)
  - [📸 Image Analyzer](#-image-analyzer)
  - [🔑 Check Breach](#-check-breach)
  - [📞 Phone Lookup](#-phone-lookup)
- [🚀 Quick start](#-quick-start)
- [📂 Project structure](#-project-structure)
- [Disclaimer](#️-disclaimer)
  
---

## 📖 Project description

A simple set of scripts to automate OSINT tasks. Everything is simplified as much as possible - no classes or complex structures, only functions that can be run and immediately get the result.

**What he can do:**
- Collect email addresses from websites
- Check username availability on social networks
- Receive WHOIS and DNS information about a domain
- Analyze image metadata
- Check passwords for leaks
- Determine country by phone number

---

## 🛠️ Tools

### 🌐 Email Hunter (`email_hunter.py`)

Collects all email addresses from a website page.

```python
from email_hunter import get_emails

emails = get_emails("https://example.com")
print(emails)
# ['info@example.com', 'support@example.com']
```

### 👤 Username Search (`username_search.py`)

Checks for username availability on popular platforms.

```python
from email_hunter import get_emails

emails = get_emails("https://example.com")
print(emails)
# ['info@example.com', 'support@example.com']
```

### 🌍 Domain Info (`domain_info.py`)

Retrieves WHOIS and DNS information about a domain.

```python
from domain_info import get_whois, get_dns

whois = get_whois("example.com")
dns = get_dns("example.com")
```
### 📸 Image Analyzer (`image_analyzer.py`)

Extracts metadata from images (EXIF, GPS coordinates).

```python
from image_analyzer import analyze_image

metadata = analyze_image("photo.jpg")
# {'Camera': 'Canon EOS', 'GPS': '48.8566, 2.3522', ...}
```

### 🔑 Check Breach (`check_breach.py`)

Checks if the password has been compromised (via the Have I Been Pwned API).

```python
from check_breach import check_pwned

found, message = check_pwned("qwerty123")
print(message) # 'Found in 1234 leaks!' or 'Not found in leaks'
```

### 📞 Phone Lookup (`phone_lookup.py`)

Determines the country by phone number.

```python
from phone_lookup import search_phone

info = search_phone("+7 123 456-78-90")
# {'country': 'Russia', 'clean': '71234567890', ...}
```

## 🚀 Quick start

1. Cloning
```bash
git clone https://github.com/st-b2/OSINT-Automation-Tools.git
cd OSINT-Automation-Tools
```
2. Installing dependencies
```bash
pip install -r requirements.txt
```
3. Launch
```bash
# Main menu
python main.py

# Or individual scripts
python email_hunter.py
python username_search.py
python domain_info.py
python image_analyzer.py
python check_breach.py
python phone_lookup.py
```
4. Example of work
```bash
$python main.py

=====================================================
🕵️ OSINT Automation Tools
=====================================================
1. Search for email addresses
2. Search by username
3. WHOIS domain
4. Checking your password for leaks
5. Exit
=====================================================

Select action: 1
Enter the site URL: https://example.com

Found email: 3
  - info@example.com
  - admin@example.com
  - support@example.com
```
## 📂 Project structure

```text
📁OSINT-Automation-Tools/
│
├── email_hunter.py # Collecting email addresses
├── username_search.py # Search by username
├── domain_info.py # Domain information
├── image_analyzer.py # Image analysis
├── check_breach.py # Checking for leaks
├── phone_lookup.py # Search by number
├── main.py # Main menu
├── requirements.txt # Dependencies
└── README.md
```

## ⚠️ Disclaimer

This project was created solely for educational purposes. Use the knowledge and tools acquired only to test your own systems or systems for which you have written permission. The author is not responsible for the use of the information provided for illegal purposes.
