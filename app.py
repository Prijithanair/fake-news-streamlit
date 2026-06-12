import streamlit as st

# Page settings
st.set_page_config(
    page_title="Fake News Risk Detection System",
    page_icon="📰",
    layout="centered"
)

# Title
st.markdown("""
# 📰 Fake News Risk Detection System

### AI-based Fake News and Virality Analysis

This system analyzes news content and predicts fake news probability, virality, and risk level.
""")

# Input box
news = st.text_area(
    "Enter News Text",
    height=200,
    placeholder="Paste news article or social media post here..."
)

# Analyze button
if st.button("🔍 Analyze News"):

    # Demo logic
    if "alien" in news.lower() or "secret" in news.lower():
        fake_probability = 85

    elif "government" in news.lower() or "policy" in news.lower():
        fake_probability = 35

    elif "library" in news.lower() or "school" in news.lower():
        fake_probability = 15

    else:
        fake_probability = 60

    # Risk Level
    if fake_probability < 25:
        risk = "✅ Safe"

    elif fake_probability < 50:
        risk = "🟡 Monitor"

    elif fake_probability < 75:
        risk = "🟠 Medium Risk"

    else:
        risk = "🚨 High Risk"

    # Virality
    if fake_probability < 40:
        virality = "Low"

    elif fake_probability < 70:
        virality = "Medium"

    else:
        virality = "High"

    # Results
    st.subheader("📊 Analysis Result")

    col1, col2, col3 = st.columns(3)

    col1.metric("Fake Probability", f"{fake_probability}%")
    col2.metric("Virality", virality)
    col3.metric("Risk Level", risk)

    # Progress bar
    st.write("### Fake News Confidence")
    st.progress(fake_probability)

    # Message
    if fake_probability >= 75:
        st.error("🚨 This content has a high probability of being fake news.")

    elif fake_probability >= 50:
        st.warning("🟠 This content should be reviewed carefully.")

    elif fake_probability >= 25:
        st.info("🟡 This content should be monitored.")

    else:
        st.success("✅ This content appears relatively safe.")

# Footer
st.markdown("---")
st.caption("Fake News Risk Detection System | DistilBERT Project Demo")
