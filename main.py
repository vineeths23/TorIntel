from scraper import scrape_dark_web
from search import search_sensitive_data
from alert import send_alert
from database import store_leak
from config import SITES_TO_MONITOR

def monitor():
    for site in SITES_TO_MONITOR:
        print(f"🔍 Scanning {site}...")
        content = scrape_dark_web(site)
        if content:
            matches = search_sensitive_data(content)
            if matches:
                print(f"🚨 Sensitive Data Found: {matches}")
                store_leak(str(matches), site)
                send_alert(matches)

if __name__ == "__main__":
    monitor()
print("Dark Web Monitoring Tool is running...")
