SUSPICIOUS_KEYWORDS = [
    "free", "win", "prize", "urgent",
    "call now", "act fast", "limited",
    "click", "verify", "claim"
]   # at any time more keywords can be added to this list

def calculate_threat_score(text, iocs):
    score = 0
    text_lower = text.lower()

    # Keyword-based scoring
    for word in SUSPICIOUS_KEYWORDS:
        if word in text_lower:
            score += 10

    # IOC-based scoring
    if len(iocs["urls"]) > 0:
        score += 25

    if len(iocs["phones"]) > 0:
        score += 20

    if len(iocs["emails"]) > 0:
        score += 10

    # Cap score at 100
    return min(score, 100)
