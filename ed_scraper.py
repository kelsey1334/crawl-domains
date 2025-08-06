import requests
from bs4 import BeautifulSoup

URL = "https://www.expireddomains.net/backorder-expired-domains/"
TARGET_TLDS = (".uk.com", ".us.com", ".ru.com", ".jpn.com")

def fetch_domains():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(URL, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    domains = []
    table = soup.find("table", {"class": "base1"})

    if not table:
        return []

    rows = table.find_all("tr")[1:]  # skip header
    for row in rows:
        cols = row.find_all("td")
        if not cols:
            continue
        domain = cols[0].text.strip().lower()
        if domain.endswith(TARGET_TLDS):
            domains.append(domain)

    return domains
