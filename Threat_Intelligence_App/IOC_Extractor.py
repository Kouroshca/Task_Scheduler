import re

def extract_iocs(text):
    urls = re.findall(r'https?://\S+', text)
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    phones = re.findall(r'\b\d{8,}\b', text)

    return {
        "urls": urls,
        "emails": emails,
        "phones": phones
    }