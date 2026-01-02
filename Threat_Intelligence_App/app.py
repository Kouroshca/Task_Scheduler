import streamlit as st
from ti_model import analyze_message

st.set_page_config(page_title="Threat Intelligence Analyzer")

st.title("🛡️ Threat Intelligence Analyzer")

message = st.text_area(
    "Enter a message to analyze",
    placeholder="Paste an email or SMS here..."
)

if st.button("Analyze Threat"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        result = analyze_message(message)

        st.subheader("Results")
        st.write(f"**Verdict:** {result['verdict']}")
        st.write(f"**Threat Score:** {result['threat_score']} / 100")

        st.subheader("Indicators of Compromise (IOCs)")
        st.json(result["iocs"])