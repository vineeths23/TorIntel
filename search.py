import re
from config import SITES_TO_MONITOR

keywords = ["fortinet", "internal use only", "classified", "leak", "breach", "SSN", "passport", "credit card"]
email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

def search_sensitive_data(text):
    found_data = []

    for keyword in keywords:
        if keyword in text:
            found_data.append(keyword)
    
    emails = email_pattern.findall(text)
    if emails:
        found_data.extend(emails)

    return found_data
