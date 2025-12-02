import streamlit as st
import openai

# Page setup
st.set_page_config(
    page_title="MYP Math AI",
    page_icon="🧮",
    layout="wide"
)

# Title
st.title("🧮 MYP Math Assessment Generator")
st.write("AI-powered tool for creating mathematics assessments")

# Sidebar for API key
with st.sidebar:
    st.header("🔐 Setup")
    
    # API Key input
    api_key = st.text_input(
        "Enter OpenAI API Key:",
        type="password",
        placeholder="sk-...",
        help="Get from https://platform.openai.com/api-keys"
    )
    
    # Store the key
    if api_key:
        st.session_state.api_key = api_key
        openai.api_key = api_key
        st.success("✅ Key saved!")
    
    # Test connection
    if st.button("Test Connection"):
        if not api_key:
            st.error("Please enter API key first")
        else:
            with st.spinner("Testing..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": "Say 'Hello'"}],
                        max_tokens=5
                    )
                    st.success(f"✅ Connected! Response: {response.choices[0].message.content}")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    st.divider()
    st.write("**Instructions:**")
    st.write("1. Get API key from OpenAI")
    st.write("2. Enter it above")
    st.write("3. Test connection")
    st.write("4. Create assessments below")

# Main app
st.header("Create Assessment")

# Simple form
with st.form("my_form"):
    topic = st.selectbox("Topic:", ["Algebra", "Geometry", "Statistics"])
    grade = st.selectbox("MYP Level:", [1, 2, 3, 4, 5])
    context = st.text_input("Real-world context:", "Sports statistics")
    
    submitted = st.form_submit_button("Generate Assessment")

# Handle form
if submitted:
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar first!")
    else:
        with st.spinner("AI is creating your assessment..."):
            # Create prompt
            prompt = f"""
            Create a MYP {grade} math assessment about {topic}.
            Real-world context: {context}
            
            Include:
            1. Title
            2. 3 questions
            3. Skills needed
            """
            
            try:
                # Call OpenAI
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=300
                )
                
                # Show result
                content = response.choices[0].message.content
                st.success("✅ Assessment created!")
                st.markdown("---")
                st.markdown(content)
                
                # Download button
                st.download_button(
                    "📥 Download as text",
                    content,
                    file_name=f"MYP{grade}_{topic}.txt"
                )
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.write("Made for MYP Math Teachers | Version 1.0")
