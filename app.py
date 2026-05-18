import streamlit as st

st.title("Fake News Risk Detection")

news = st.text_area("Enter News Text")

if st.button("Analyze"):
    st.subheader("Prediction Result")

    # Demo result
    st.write("Fake News Probability: 78%")
    st.write("Virality: High")
    st.write("Risk Level: High Risk 🚨")
