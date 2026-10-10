import streamlit as st
st.set_page_config(page_title="Haqeeq App", page_icon="📰")
st.title("Haqeeq - Urdu Fake News Detection")
st.write("Thesis Project - Attaullah Khan")
text = st.text_area("Urdu Khabar Likhen:")
if st.button("Check"):
    if "حیران" in text or "فوری" in text:
        st.error("🔴 Fake News")
    else:
        st.success("🟢 Real News")
