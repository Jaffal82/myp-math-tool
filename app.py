import streamlit as st
from openai import OpenAI
from datetime import datetime

# Page setup
st.set_page_config(
    page_title="MYP Math AI",
    page_icon="🧮",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        color: #1E3A8A;
        text-align: center;
        font-size: 2.5rem;
    }
    .assessment-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">🧮 MYP Math Assessment Generator</h1>', unsafe_allow_html=True)
st.write("AI-powered tool for creating MYP mathematics assessments")

# Initialize session state
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'assessments' not in st.session_state:
    st.session_state.assessments = []

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("🔐 API Configuration")
    
    # API Key input
    api_key = st.text_input(
        "OpenAI API Key:",
        type="password",
        placeholder="sk-...",
        help="Get from https://platform.openai.com/api-keys",
        key="api_input"
    )
    
    # Save API key
    if api_key:
        st.session_state.api_key = api_key
        st.success("✅ Key saved")
    
    st.divider()
    
    # Test connection button
    if st.button("🔌 Test Connection", use_container_width=True):
        if not api_key:
            st.error("❌ Please enter API key first")
        else:
            with st.spinner("Testing connection..."):
                try:
                    # Initialize client with new API
                    client = OpenAI(api_key=api_key)
                    
                    # Test call
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": "Say 'Connected!' in 2 words"}],
                        max_tokens=5
                    )
                    
                    st.success("✅ **Connection Successful!**")
                    st.info(f"Response: {response.choices[0].message.content}")
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"❌ Connection failed: {str(e)}")
    
    st.divider()
    
    # Quick help
    st.write("**Need help?**")
    st.write("1. Get API key from OpenAI")
    st.write("2. Enter it above")
    st.write("3. Click 'Test Connection'")
    st.write("4. Create assessment below")

# ========== MAIN APP ==========
st.header("📝 Create New Assessment")

# Check if API key is set
if not st.session_state.api_key:
    st.warning("⚠️ **Please enter your OpenAI API key in the sidebar first**")
    st.info("You'll get $5 free credits when you sign up at platform.openai.com")

# Assessment form
with st.form("assessment_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        myp_level = st.selectbox("MYP Level", [1, 2, 3, 4, 5], index=2)
        topic = st.selectbox("Topic", [
            "Algebra", "Number", "Geometry", 
            "Statistics", "Probability", "Functions"
        ])
    
    with col2:
        criteria = st.multiselect(
            "Criteria Focus",
            ["Criterion A", "Criterion B", "Criterion C", "Criterion D"],
            default=["Criterion B"]
        )
        difficulty = st.select_slider(
            "Difficulty Level",
            options=["Beginner", "Intermediate", "Advanced"]
        )
    
    # Context
    context = st.text_area(
        "Real-world Context",
        placeholder="Example: 'Analyzing sports statistics', 'Designing sustainable packaging', 'Planning a school budget'...",
        height=60
    )
    
    # Submit button
    submitted = st.form_submit_button(
        "🚀 Generate Assessment with AI",
        type="primary",
        use_container_width=True
    )

# Handle form submission
if submitted:
    if not st.session_state.api_key:
        st.error("🔑 **Please enter your OpenAI API key in the sidebar first!**")
    else:
        with st.spinner("🤖 AI is creating your assessment... This takes 10-20 seconds"):
            try:
                # Initialize OpenAI client with NEW API
                client = OpenAI(api_key=st.session_state.api_key)
                
                # Create prompt
                prompt = f"""
                Create a complete MYP {myp_level} Mathematics assessment with these specifications:
                
                TOPIC: {topic}
                CRITERIA: {', '.join(criteria)}
                DIFFICULTY: {difficulty}
                REAL-WORLD CONTEXT: {context if context else 'General application'}
                GRADE LEVEL: MYP {myp_level} (students aged {myp_level + 10}-{myp_level + 11})
                
                Please format your response as:
                
                ====== ASSESSMENT TITLE ======
                [Creative title linking topic to context]
                
                ====== TASK STATEMENT ======
                [Clear, engaging task description for students]
                
                ====== QUESTIONS ======
                1. [Question 1 - Focus on basic understanding/recall]
                2. [Question 2 - Focus on application of skills]
                3. [Question 3 - Focus on analysis and justification]
                4. [Question 4 - Focus on evaluation/creation]
                
                ====== EXPECTED MATHEMATICAL SKILLS ======
                • [Skill 1]
                • [Skill 2]
                • [Skill 3]
                
                ====== TEACHER NOTES ======
                [Brief notes on implementation, common misconceptions, extension ideas]
                """
                
                # Call OpenAI API with NEW syntax
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert IB MYP Mathematics teacher with 10+ years experience."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=1200
                )
                
                # Get the content
                assessment_content = response.choices[0].message.content
                
                # Create assessment object
                assessment = {
                    "id": len(st.session_state.assessments) + 1,
                    "title": f"MYP {myp_level} {topic} Assessment",
                    "content": assessment_content,
                    "metadata": {
                        "level": myp_level,
                        "topic": topic,
                        "criteria": criteria,
                        "difficulty": difficulty,
                        "context": context,
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "tokens": response.usage.total_tokens
                    }
                }
                
                # Save to session
                st.session_state.assessments.append(assessment)
                
                # Show success
                st.success("✅ Assessment generated successfully!")
                st.balloons()
                
                # Display assessment
                st.markdown("---")
                st.markdown(f"### 📄 {assessment['title']}")
                st.markdown(f"*Generated: {assessment['metadata']['date']}*")
                st.markdown("---")
                
                # Show in a nice box
                st.markdown(f'<div class="assessment-box">{assessment_content}</div>', unsafe_allow_html=True)
                
                # Action buttons
                st.markdown("---")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.download_button(
                        "📥 Download as .txt",
                        assessment_content,
                        file_name=f"MYP{myp_level}_{topic}_{datetime.now().strftime('%Y%m%d')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col2:
                    if st.button("📋 Copy to Clipboard", use_container_width=True):
                        st.code(assessment_content)
                        st.success("✅ Copied to clipboard!")
                
                with col3:
                    if st.button("🔄 Generate Another", use_container_width=True):
                        st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error generating assessment: {str(e)}")
                st.info("Common fixes: 1) Check API key 2) Ensure you have credits 3) Test connection first")

# ========== ASSESSMENT LIBRARY ==========
if st.session_state.assessments:
    st.header("📚 Your Assessment Library")
    
    for i, assessment in enumerate(st.session_state.assessments):
        with st.expander(f"📄 {assessment['title']} - {assessment['metadata']['date']}"):
            st.write(f"**Level:** MYP {assessment['metadata']['level']}")
            st.write(f"**Topic:** {assessment['metadata']['topic']}")
            st.write(f"**Criteria:** {', '.join(assessment['metadata']['criteria'])}")
            st.download_button(
                "Download",
                assessment['content'],
                file_name=f"assessment_{assessment['id']}.txt",
                key=f"dl_{i}",
                use_container_width=True
            )
            st.markdown("---")
            st.markdown(assessment['content'])

# Footer
st.markdown("---")
st.markdown("**MYP Math AI Generator** • Powered by OpenAI • Made for IB Teachers")
