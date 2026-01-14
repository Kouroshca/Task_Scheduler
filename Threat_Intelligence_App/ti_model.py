from IOC_Extractor import extract_iocs
from ml_classifier import predict_spam

def analyze_message(message):
    iocs = extract_iocs(message)

    threat_score = 10
    threat_score += len(iocs["urls"]) * 20
    threat_score += len(iocs["emails"]) * 10
    threat_score += len(iocs["phones"]) * 10

    ml_label, ml_confidence = predict_spam(message)

    if ml_label == "spam":
        threat_score += 30

    threat_score = min(threat_score, 100)

    verdict = (
        "High Risk" if threat_score >= 70
        else "Medium Risk" if threat_score >= 40
        else "Low Risk"
    )

    return {
        "verdict": verdict,
        "threat_score": threat_score,
        "ml_prediction": ml_label,
        "ml_confidence": ml_confidence,
        "iocs": iocs
    }
