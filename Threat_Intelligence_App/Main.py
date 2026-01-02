from ti_model import analyze_message

message = input("Enter the message to analyze: ")
result = analyze_message(message)

print("\n--- Threat Intelligence Report ---")
print(f"Verdict: {result['verdict']}")
print(f"Threat Score: {result['threat_score']}/100")
print("IOCs Found:")
print(result["iocs"])


