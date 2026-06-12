import streamlit as st

# Page settings
st.set_page_config(
    page_title="Fake News Risk Detection",
    page_icon="📰",
    layout="centered"
)

# Title
st.markdown("""
# 📰 Fake News Risk Detection System
### AI-based Fake News and Virality Analysis
""")

st.write("This system analyzes news content and predicts fake news probability, virality, and risk level.")

# Input
news = st.text_area(
    "Enter News Text",
    height=200,
    placeholder="Paste news article or social media post here..."
)

# Analyze button
if st.button("🔍 Analyze News"):

    st.subheader("📊 Analysis Result")

    # Demo outputs
    if "alien" in news.lower() or "secret" in news.lower():
    fake_probability = 85

elif "government" in news.lower() or "policy" in news.lower():
    fake_probability = 35

else:
    fake_probability = 60
    
if fake_probability < 25:
    risk = "✅ Safe"
elif fake_probability < 50:
    risk = "🟡 Monitor"
elif fake_probability < 75:
    risk = "🟠 Medium Risk"
else:
    risk = "🚨 High Risk"

if fake_probability < 40:
    virality = "Low"
elif fake_probability < 70:
    virality = "Medium"
else:
    virality = "High"
    
    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Fake Probability", f"{fake_probability}%")
    col2.metric("Virality", virality)
    col3.metric("Risk Level", risk)

    # Progress bar
    st.write("### Fake News Confidence")
    st.progress(fake_probability)

    # Risk message
    if fake_probability > 70:
        st.error("⚠️ This news has a high chance of being fake and viral.")
    elif fake_probability > 40:
        st.warning("⚠️ This news should be monitored carefully.")
    else:
        st.success("✅ This news appears relatively safe.")

# Footer
st.markdown("---")
st.caption("Capstone Project | Fake News Risk Detection using NLP and Transformers")
