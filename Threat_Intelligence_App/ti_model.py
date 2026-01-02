from IOC_Extractor import extract_iocs
from ThreatScoring import calculate_threat_score

def analyze_message(text):
    iocs = extract_iocs(text)
    threat_score = calculate_threat_score(text, iocs)

    if threat_score >= 70:
        verdict = "HIGH RISK"
    elif threat_score >= 40:
        verdict = "SUSPICIOUS"
    else:
        verdict = "LOW RISK"

    return {
        "verdict": verdict,
        "threat_score": threat_score,
        "iocs": iocs
    }