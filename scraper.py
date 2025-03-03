import requests
from bs4 import BeautifulSoup
from config import proxies

def get_tor_session():
    session = requests.Session()
    session.proxies = {'http': proxies, 'https': proxies}
    return session

def scrape_dark_web(url):
    session = get_tor_session()
    try:
        response = session.get(url, timeout=10)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "lxml").get_text()
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    return None
