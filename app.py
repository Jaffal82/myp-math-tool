# app.py - SIMPLE WORKING VERSION
import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="MYP Math Pro",
    page_icon="🧮",
    layout="wide"
)

# ========== TRY TO IMPORT CURRICULUM ==========
try:
    from curriculum import MYP_CURRICULUM, CRITERION_STRANDS, GLOBAL_CONTEXTS, KEY_CONCEPTS, COMMAND_TERMS
    st.session_state.curriculum_loaded = True
    st.session_state.curriculum = MYP_CURRICULUM
    st.session_state.criteria = CRITERION_STRANDS
except ImportError as e:
    st.session_state.curriculum_loaded = False
    st.error(f"❌ Could not load curriculum: {e}")
    st.info("Make sure curriculum.py is in the same folder as app.py")

# ========== SIMPLE HEADER ==========
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin-bottom: 2rem;">
    <h1>🧮 MYP Mathematics Generator</h1>
    <p>Create curriculum-aligned math assessments</p>
</div>
""", unsafe_allow_html=True)

# ========== MAIN TABS ==========
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Curriculum",
    "🎯 Criteria", 
    "🛠️ Tools",
    "📝 Generate"
])

# ========== TAB 1: CURRICULUM ==========
with tab1:
    st.header("MYP Curriculum Framework")
    
    if not st.session_state.curriculum_loaded:
        st.error("Curriculum not loaded. Check curriculum.py file.")
        st.code("""
        # Fix: Make sure you have curriculum.py with:
        MYP_CURRICULUM = {
            "MYP 1-3": { ... },
            "MYP 4-5 (standard)": { ... }
        }
        """)
    else:
        # Level selection
        col1, col2, col3 = st.columns(3)
        
        with col1:
            selected_level = st.selectbox(
                "📊 MYP Level:",
                list(st.session_state.curriculum.keys()),
                key="level_selector"
            )
        
        if selected_level and selected_level in st.session_state.curriculum:
            with col2:
                branches = list(st.session_state.curriculum[selected_level].keys())
                selected_branch = st.selectbox(
                    "🎯 Mathematics Branch:",
                    branches,
                    key="branch_selector"
                )
            
            if selected_branch:
                with col3:
                    topics = list(st.session_state.curriculum[selected_level][selected_branch].keys())
                    selected_topic = st.selectbox(
                        "📝 Topic Area:",
                        topics,
                        key="topic_selector"
                    )
                
                # Display skills
                st.markdown("---")
                st.subheader("📋 Skills & Concepts")
                
                skills = st.session_state.curriculum[selected_level][selected_branch][selected_topic]
                selected_skills = st.multiselect(
                    "Select specific skills for your assessment:",
                    skills,
                    default=skills[:3] if len(skills) > 3 else skills
                )
                
                if selected_skills:
                    st.success(f"✅ Selected {len(selected_skills)} skills")
                    
                    # Display in nice boxes
                    cols = st.columns(2)
                    for i, skill in enumerate(selected_skills):
                        col = cols[i % 2]
                        with col:
                            st.markdown(f"""
                            <div style="background: #f0f9ff; padding: 15px; border-radius: 10px; border-left: 4px solid #3b82f6; margin: 5px 0;">
                                <strong>• {skill}</strong>
                            </div>
                            """, unsafe_allow_html=True)
                
                # Save to session
                st.session_state.selected_curriculum = {
                    "level": selected_level,
                    "branch": selected_branch,
                    "topic": selected_topic,
                    "skills": selected_skills
                }

# ========== TAB 2: CRITERIA ==========
with tab2:
    st.header("Assessment Criteria Selection")
    
    if not st.session_state.curriculum_loaded:
        st.warning("Load curriculum first")
    else:
        st.info("Select the specific criterion strands for assessment")
        
        # Criterion A
        with st.expander("🔵 **Criterion A: Knowing & Understanding**", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                a_i = st.checkbox("A-i: Select mathematics", value=True)
            with col2:
                a_ii = st.checkbox("A-ii: Apply mathematics", value=True)
            with col3:
                a_iii = st.checkbox("A-iii: Solve problems", value=True)
        
        # Criterion B
        with st.expander("🟢 **Criterion B: Investigating Patterns**", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                b_i = st.checkbox("B-i: Problem-solving strategies")
            with col2:
                b_ii = st.checkbox("B-ii: Describe patterns")
            with col3:
                b_iii = st.checkbox("B-iii: Test rules")
            with col4:
                b_iv = st.checkbox("B-iv: Justify generalizations")
        
        # Save selected criteria
        selected_criteria = []
        if a_i: selected_criteria.append("A-i: Select appropriate mathematics")
        if a_ii: selected_criteria.append("A-ii: Apply mathematics successfully")
        if a_iii: selected_criteria.append("A-iii: Solve problems correctly")
        if b_i: selected_criteria.append("B-i: Select problem-solving strategies")
        if b_ii: selected_criteria.append("B-ii: Describe patterns")
        if b_iii: selected_criteria.append("B-iii: Test and verify rules")
        if b_iv: selected_criteria.append("B-iv: Justify generalizations")
        
        st.session_state.selected_criteria = selected_criteria
        
        if selected_criteria:
            st.success(f"✅ Selected {len(selected_criteria)} criterion strands")
            for criterion in selected_criteria:
                st.write(f"• {criterion}")

# ========== TAB 3: MATH TOOLS ==========
with tab3:
    st.header("🛠️ Math Content Tools")
    
    tool_choice = st.selectbox(
        "Choose a tool:",
        ["GeoGebra Calculator", "Equation Editor", "Graph Generator", "LaTeX Preview"]
    )
    
    if tool_choice == "GeoGebra Calculator":
        st.subheader("📐 GeoGebra Calculator")
        html = """
        <div style="border: 3px solid #3b82f6; border-radius: 15px; overflow: hidden; margin: 20px 0;">
            <iframe src="https://www.geogebra.org/calculator" 
                    width="100%" 
                    height="500px" 
                    style="border: none;">
            </iframe>
        </div>
        """
        components.html(html, height=530)
        
    elif tool_choice == "Equation Editor":
        st.subheader("✏️ Equation Editor")
        latex_input = st.text_area(
            "Enter LaTeX equation:",
            value="\\[ x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a} \\]",
            height=100
        )
        
        if latex_input:
            # Preview
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
                <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
            </head>
            <body>
                <div style="padding: 30px; background: white; border-radius: 10px; text-align: center; font-size: 24px;">
                    {latex_input}
                </div>
            </body>
            </html>
            """
            components.html(html, height=200)
            
            # Download button
            st.download_button(
                "📥 Download Equation",
                latex_input,
                file_name="equation.tex"
            )

# ========== TAB 4: GENERATE ==========
with tab4:
    st.header("📝 Generate Assessment")
    
    # Check if ready
    ready = True
    if 'selected_curriculum' not in st.session_state:
        st.warning("⚠️ Please select curriculum in Tab 1")
        ready = False
    
    if 'selected_criteria' not in st.session_state:
        st.warning("⚠️ Please select criteria in Tab 2")
        ready = False
    
    if ready:
        # Assessment details
        st.subheader("Assessment Details")
        
        col1, col2 = st.columns(2)
        with col1:
            assessment_title = st.text_input("Title:", "MYP Mathematics Assessment")
            duration = st.selectbox("Duration:", ["45 minutes", "60 minutes", "90 minutes", "120 minutes"])
        
        with col2:
            context = st.selectbox("Global Context:", GLOBAL_CONTEXTS)
            format_type = st.selectbox("Format:", ["Written test", "Investigation", "Project"])
        
        # Generate button
        if st.button("🚀 GENERATE ASSESSMENT", type="primary", use_container_width=True):
            with st.spinner("Creating assessment..."):
                # Simple assessment template
                curriculum = st.session_state.selected_curriculum
                criteria = st.session_state.selected_criteria
                
                assessment = f"""
                # {assessment_title}
                
                ## Curriculum Alignment
                - **MYP Level:** {curriculum['level']}
                - **Branch:** {curriculum['branch']}
                - **Topic:** {curriculum['topic']}
                - **Skills:** {', '.join(curriculum['skills'][:3])}
                
                ## Assessment Criteria
                {chr(10).join(['• ' + c for c in criteria])}
                
                ## Global Context
                {context}
                
                ## Instructions
                Duration: {duration}
                Format: {format_type}
                
                Show all working. Calculators allowed unless specified.
                
                ## Part A: Knowledge and Understanding
                1. Solve the equation: 2x + 5 = 17
                2. Simplify: 3(x + 4) - 2(x - 1)
                
                ## Part B: Investigation
                3. Investigate the number pattern: 2, 5, 10, 17, 26, ...
                   a) Describe the pattern in words
                   b) Find the next two terms
                   c) Write a formula for the nth term
                
                ## Part C: Real-world Application
                4. A rectangular garden has length (x + 3) meters and width (x - 1) meters.
                   The area is 40 m².
                   a) Write an equation for the area
                   b) Solve for x
                   c) Find the dimensions of the garden
                """
                
                st.session_state.generated_assessment = assessment
                st.success("✅ Assessment generated successfully!")
        
        # Show generated assessment
        if 'generated_assessment' in st.session_state:
            st.markdown("---")
            st.subheader("📄 Generated Assessment")
            st.markdown(st.session_state.generated_assessment)
            
            # Download button
            st.download_button(
                "📥 Download Assessment",
                st.session_state.generated_assessment,
                file_name=f"{assessment_title}.txt",
                use_container_width=True
            )
    else:
        st.info("👈 Complete Tabs 1 & 2 first to generate assessment")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("**MYP Mathematics Assessment Generator** • Version 2.0 • All tools integrated")
