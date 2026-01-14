import streamlit as st
from ti_model import analyze_message

st.set_page_config(page_title="Threat Intelligence Analyzer", layout="centered")

st.title("🛡️ Threat Intelligence Analyzer")
st.write("Paste an email or SMS message to analyze potential threats.")

message = st.text_area(
    "Message to analyze",
    placeholder="Paste an email or SMS here...",
    height=150
)

if st.button("Analyze Threat"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        result = analyze_message(message)

        st.subheader("📊 Analysis Result")
        st.metric("Threat Score", f"{result['threat_score']}/100")
        st.write(f"**Verdict:** {result['verdict']}")

        # Display ML prediction and IOCs
        st.subheader("🤖 Machine Learning Analysis")
        st.write(f"Prediction: **{result['ml_prediction'].upper()}**")
        st.write(f"Confidence: **{result['ml_confidence']}%**")

        st.subheader("🔎 Indicators of Compromise (IOCs)")
        st.json(result["iocs"])
