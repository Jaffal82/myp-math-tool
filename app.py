import streamlit as st

# Page setup
st.set_page_config(
    page_title="MYP Math Tool",
    page_icon="🧮",
    layout="centered"
)

# Simple app to test
st.title("🧮 MYP Math Assessment Generator")
st.write("Welcome! This is a tool to create math assessments.")

st.success("✅ If you can see this, the app is working!")
st.info("Next step: We'll add AI features.")

# Simple input
topic = st.selectbox("Choose a topic:", ["Algebra", "Geometry", "Statistics"])
name = st.text_input("Your name:")

if name:
    st.write(f"Hello {name}! Let's create a {topic} assessment.")