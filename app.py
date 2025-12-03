# app.py - UPDATED TO SHOW ALL CURRICULUM COMPONENTS
import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="MYP Math Complete",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== LOAD COMPLETE CURRICULUM ==========
try:
    from curriculum import (
        MYP_CURRICULUM, 
        CRITERION_STRANDS, 
        GLOBAL_CONTEXTS, 
        KEY_CONCEPTS, 
        COMMAND_TERMS,
        ACHIEVEMENT_LEVELS,
        CONTEXT_EXAMPLES,
        COMMAND_TERMS_BY_CRITERION,
        DIFFERENTIATION_STRATEGIES
    )
    
    st.session_state.curriculum_loaded = True
    st.session_state.curriculum = MYP_CURRICULUM
    st.session_state.criteria = CRITERION_STRANDS
    st.session_state.all_terms = COMMAND_TERMS
    st.session_state.achievement = ACHIEVEMENT_LEVELS
    
except ImportError as e:
    st.session_state.curriculum_loaded = False
    st.error(f"❌ Error loading curriculum: {e}")

# ========== HEADER ==========
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #1e3a8a 0%, #3b0764 100%); border-radius: 15px; color: white; margin-bottom: 2rem; box-shadow: 0 10px 25px rgba(0,0,0,0.2);">
    <h1 style="font-size: 2.8rem; margin-bottom: 0.5rem;">🧮 MYP MATHEMATICS PROFESSIONAL SUITE</h1>
    <h3 style="font-weight: 300; opacity: 0.9;">Complete Curriculum • All Criteria Strands • Full Command Terms</h3>
</div>
""", unsafe_allow_html=True)

# ========== SIDEBAR - QUICK STATS ==========
with st.sidebar:
    st.markdown("### 📊 Curriculum Stats")
    
    if st.session_state.curriculum_loaded:
        total_skills = 0
        for level in st.session_state.curriculum:
            for branch in st.session_state.curriculum[level]:
                for topic in st.session_state.curriculum[level][branch]:
                    total_skills += len(st.session_state.curriculum[level][branch][topic])
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("MYP Levels", len(st.session_state.curriculum))
            st.metric("Criteria", len(st.session_state.criteria))
        with col2:
            st.metric("Total Skills", total_skills)
            st.metric("Command Terms", len(st.session_state.all_terms))
    else:
        st.error("Curriculum not loaded")
    
    st.divider()
    
    # Quick navigation
    st.markdown("### 🚀 Quick Navigation")
    if st.button("📚 Go to Curriculum", use_container_width=True):
        st.session_state.current_tab = "Curriculum"
    if st.button("🎯 Go to Criteria", use_container_width=True):
        st.session_state.current_tab = "Criteria"
    if st.button("📝 Go to Command Terms", use_container_width=True):
        st.session_state.current_tab = "Command Terms"

# ========== MAIN TABS ==========
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📚 Complete Curriculum",
    "🎯 All Criteria Strands", 
    "📝 Command Terms",
    "🛠️ Math Tools",
    "📊 Achievement Levels"
])

# ========== TAB 1: COMPLETE CURRICULUM ==========
with tab1:
    st.header("📚 Complete MYP Mathematics Curriculum")
    
    if not st.session_state.curriculum_loaded:
        st.error("Curriculum database not loaded. Check curriculum.py file.")
    else:
        # Curriculum Explorer
        col1, col2, col3 = st.columns([2, 3, 2])
        
        with col1:
            st.subheader("MYP Level")
            selected_level = st.selectbox(
                "Select Level:",
                list(st.session_state.curriculum.keys()),
                key="tab1_level"
            )
        
        with col2:
            if selected_level:
                st.subheader("Mathematics Branch")
                branches = list(st.session_state.curriculum[selected_level].keys())
                selected_branch = st.selectbox(
                    "Select Branch:",
                    branches,
                    key="tab1_branch"
                )
        
        with col3:
            if selected_branch:
                st.subheader("Topic Area")
                topics = list(st.session_state.curriculum[selected_level][selected_branch].keys())
                selected_topic = st.selectbox(
                    "Select Topic:",
                    topics,
                    key="tab1_topic"
                )
        
        # Display Skills
        if selected_topic:
            st.markdown("---")
            st.subheader(f"📋 Skills & Concepts: {selected_topic}")
            
            skills = st.session_state.curriculum[selected_level][selected_branch][selected_topic]
            
            # Group skills into columns
            cols = st.columns(2)
            for i, skill in enumerate(skills):
                col = cols[i % 2]
                with col:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); 
                                padding: 15px; 
                                border-radius: 10px; 
                                margin: 8px 0;
                                border-left: 4px solid #0ea5e9;">
                        <strong>• {skill}</strong>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.info(f"✅ **{len(skills)} skills** in {selected_topic} for {selected_level}")
            
            # Skill selector for assessment
            st.markdown("---")
            st.subheader("🎯 Select Skills for Assessment")
            selected_skills = st.multiselect(
                "Choose specific skills to include:",
                skills,
                default=skills[:min(5, len(skills))]
            )
            
            if selected_skills:
                st.session_state.selected_skills = selected_skills
                st.success(f"Selected {len(selected_skills)} skills for assessment")
        
        # Show all curriculum structure
        with st.expander("📖 View Complete Curriculum Structure"):
            for level in st.session_state.curriculum:
                st.markdown(f"### {level}")
                for branch in st.session_state.curriculum[level]:
                    st.markdown(f"**{branch}**")
                    for topic in st.session_state.curriculum[level][branch]:
                        count = len(st.session_state.curriculum[level][branch][topic])
                        st.markdown(f"- {topic} ({count} skills)")

# ========== TAB 2: ALL CRITERIA STRANDS ==========
with tab2:
    st.header("🎯 Complete Assessment Criteria")
    
    if not st.session_state.curriculum_loaded:
        st.error("Curriculum not loaded")
    else:
        st.info("Select specific criterion strands for your assessment. Each strand corresponds to different achievement levels.")
        
        # Display all criteria with expanders
        selected_strands = []
        
        for criterion, strands in st.session_state.criteria.items():
            with st.expander(f"🔵 **{criterion}**", expanded=True):
                st.markdown(f"*{criterion.split(':')[1].strip()}*")
                
                # Display strands
                cols = st.columns(len(strands))
                for i, (strand_code, description) in enumerate(strands.items()):
                    with cols[i]:
                        if st.checkbox(f"{criterion[:1]}-{strand_code}", 
                                     help=description,
                                     key=f"{criterion}_{strand_code}"):
                            selected_strands.append(f"{criterion[:1]}-{strand_code}: {description}")
                
                # Show achievement levels
                if criterion in st.session_state.achievement:
                    with st.expander("📊 Achievement Level Descriptors"):
                        for level, descriptor in st.session_state.achievement[criterion].items():
                            st.markdown(f"**Level {level}:** {descriptor}")
        
        # Summary
        if selected_strands:
            st.markdown("---")
            st.success(f"✅ Selected {len(selected_strands)} criterion strands")
            st.session_state.selected_strands = selected_strands
            
            # Show summary
            for strand in selected_strands:
                st.markdown(f"• {strand}")
        
        # Command terms by criterion
        st.markdown("---")
        st.subheader("📝 Recommended Command Terms by Criterion")
        if 'COMMAND_TERMS_BY_CRITERION' in locals():
            cols = st.columns(len(COMMAND_TERMS_BY_CRITERION))
            for i, (criterion_name, terms) in enumerate(COMMAND_TERMS_BY_CRITERION.items()):
                with cols[i]:
                    st.markdown(f"**{criterion_name}**")
                    for term in terms[:5]:  # Show first 5 terms
                        st.write(f"• {term}")

# ========== TAB 3: COMMAND TERMS ==========
with tab3:
    st.header("📝 Complete Command Terms Dictionary")
    
    if not st.session_state.curriculum_loaded:
        st.error("Curriculum not loaded")
    else:
        # Search command terms
        search_term = st.text_input("🔍 Search command terms:", "")
        
        # Filter terms
        filtered_terms = {}
        if search_term:
            for term, definition in st.session_state.all_terms.items():
                if search_term.lower() in term.lower() or search_term.lower() in definition.lower():
                    filtered_terms[term] = definition
        else:
            filtered_terms = st.session_state.all_terms
        
        # Display in categories
        st.subheader(f"Found {len(filtered_terms)} command terms")
        
        # Categorize
        knowledge_terms = {}
        application_terms = {}
        synthesis_terms = {}
        
        knowledge_keywords = ["calculate", "describe", "determine", "draw", "label", "list", "measure", "state", "write down"]
        application_keywords = ["analyze", "apply", "comment", "compare", "construct", "demonstrate", "derive", "design", "estimate", "find", "identify", "interpret", "investigate", "plot", "show", "sketch", "solve"]
        
        for term, definition in filtered_terms.items():
            if any(keyword in term.lower() for keyword in knowledge_keywords):
                knowledge_terms[term] = definition
            elif any(keyword in term.lower() for keyword in application_keywords):
                application_terms[term] = definition
            else:
                synthesis_terms[term] = definition
        
        # Display in columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🎓 Knowledge & Comprehension")
            for term, definition in list(knowledge_terms.items())[:10]:
                with st.expander(term):
                    st.write(definition)
        
        with col2:
            st.markdown("### 🧪 Application & Analysis")
            for term, definition in list(application_terms.items())[:10]:
                with st.expander(term):
                    st.write(definition)
        
        with col3:
            st.markdown("### 💡 Synthesis & Evaluation")
            for term, definition in list(synthesis_terms.items())[:10]:
                with st.expander(term):
                    st.write(definition)
        
        # Show all terms in expander
        with st.expander("📋 View All Command Terms"):
            for term, definition in st.session_state.all_terms.items():
                st.markdown(f"**{term}**")
                st.write(f"{definition}")
                st.write("---")

# ========== TAB 4: MATH TOOLS ==========
with tab4:
    st.header("🛠️ Mathematics Content Tools")
    
    tool_choice = st.selectbox(
        "Select Tool:",
        ["GeoGebra Calculator", "GeoGebra Geometry", "Equation Editor", "Graph Generator", "Differentiation Strategies"]
    )
    
    if tool_choice == "GeoGebra Calculator":
        st.subheader("📐 GeoGebra Scientific Calculator")
        html = """
        <div style="border: 3px solid #3b82f6; border-radius: 15px; overflow: hidden; margin: 20px 0; box-shadow: 0 5px 15px rgba(59, 130, 246, 0.1);">
            <iframe src="https://www.geogebra.org/calculator" 
                    width="100%" 
                    height="600px" 
                    style="border: none;"
                    allowfullscreen>
            </iframe>
        </div>
        """
        components.html(html, height=630)
        
    elif tool_choice == "Differentiation Strategies":
        st.subheader("🎯 Differentiation Strategies")
        
        if 'DIFFERENTIATION_STRATEGIES' in locals():
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🆘 Support Strategies")
                for strategy in DIFFERENTIATION_STRATEGIES["Support strategies"]:
                    st.markdown(f"""
                    <div style="background: #f0f9ff; padding: 12px; border-radius: 8px; margin: 8px 0; border-left: 4px solid #0ea5e9;">
                        • {strategy}
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### 🚀 Extension Strategies")
                for strategy in DIFFERENTIATION_STRATEGIES["Extension strategies"]:
                    st.markdown(f"""
                    <div style="background: #f0f7ff; padding: 12px; border-radius: 8px; margin: 8px 0; border-left: 4px solid #6366f1;">
                        • {strategy}
                    </div>
                    """, unsafe_allow_html=True)
    
    elif tool_choice == "Equation Editor":
        st.subheader("✏️ LaTeX Equation Editor")
        
        # Sample equations
        col1, col2 = st.columns(2)
        with col1:
            equation = st.text_area(
                "LaTeX Code:",
                value="\\[ \\int_{a}^{b} f(x) \\, dx = F(b) - F(a) \\]",
                height=100
            )
            
            # Quick templates
            template = st.selectbox("Quick Templates:", [
                "Quadratic Formula",
                "Circle Equation",
                "Trig Identity",
                "Derivative",
                "Limit",
                "Matrix"
            ])
            
            if template == "Quadratic Formula":
                equation = "\\[ x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a} \\]"
            elif template == "Circle Equation":
                equation = "\\[ (x-h)^2 + (y-k)^2 = r^2 \\]"
        
        with col2:
            # Preview
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
                <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
            </head>
            <body>
                <div style="padding: 30px; background: white; border-radius: 10px; text-align: center; font-size: 20px; border: 2px solid #e5e7eb;">
                    {equation}
                </div>
            </body>
            </html>
            """
            components.html(html, height=150)
            
            # Actions
            st.download_button(
                "📥 Download Equation",
                equation,
                file_name="equation.tex"
            )

# ========== TAB 5: ACHIEVEMENT LEVELS ==========
with tab5:
    st.header("📊 Achievement Level Descriptors")
    
    if not st.session_state.curriculum_loaded:
        st.error("Curriculum not loaded")
    else:
        criterion_choice = st.selectbox(
            "Select Criterion:",
            list(st.session_state.achievement.keys())
        )
        
        if criterion_choice:
            st.subheader(f"{criterion_choice}")
            
            # Display achievement levels
            cols = st.columns(4)
            levels = ["0", "1-2", "3-4", "5-6", "7-8"]
            
            for i, level in enumerate(levels):
                if i < 4:  # Spread across 4 columns
                    with cols[i]:
                        if level in st.session_state.achievement[criterion_choice]:
                            descriptor = st.session_state.achievement[criterion_choice][level]
                            color = "#dc2626" if level == "0" else "#ea580c" if level == "1-2" else "#ca8a04" if level == "3-4" else "#16a34a" if level == "5-6" else "#059669"
                            
                            st.markdown(f"""
                            <div style="background: {color}; color: white; padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 15px;">
                                <h3 style="margin: 0;">Level {level}</h3>
                            </div>
                            <div style="background: #f8fafc; padding: 15px; border-radius: 8px; height: 300px; overflow-y: auto;">
                                {descriptor}
                            </div>
                            """, unsafe_allow_html=True)
            
            # Level 7-8 in full width
            if "7-8" in st.session_state.achievement[criterion_choice]:
                st.markdown("---")
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #059669 0%, #047857 100%); color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
                    <h2 style="margin: 0;">🎯 Level 7-8: Excellence</h2>
                </div>
                <div style="background: #f0fdf4; padding: 25px; border-radius: 10px; border: 2px solid #bbf7d0; font-size: 1.1rem;">
                    {st.session_state.achievement[criterion_choice]["7-8"]}
                </div>
                """, unsafe_allow_html=True)

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 2rem;">
    <p><strong>MYP Mathematics Professional Suite</strong> • Complete Curriculum Database • All IB Standards</p>
    <p>Version 3.0 • Includes ALL MYP levels, ALL criteria strands, ALL command terms</p>
</div>
""", unsafe_allow_html=True)

# ========== GENERATE ASSESSMENT BUTTON ==========
st.markdown("---")
if st.button("🚀 GENERATE COMPLETE ASSESSMENT", type="primary", use_container_width=True):
    if not st.session_state.curriculum_loaded:
        st.error("Curriculum not loaded")
    else:
        # Check what's selected
        curriculum_selected = 'selected_skills' in st.session_state and st.session_state.selected_skills
        criteria_selected = 'selected_strands' in st.session_state and st.session_state.selected_strands
        
        if curriculum_selected and criteria_selected:
            st.success("✅ Ready to generate assessment with complete curriculum alignment!")
            st.balloons()
            
            # Show summary
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**Curriculum:** {len(st.session_state.selected_skills)} skills selected")
            with col2:
                st.info(f"**Criteria:** {len(st.session_state.selected_strands)} strands selected")
            
            # Add generation logic here
            st.write("Assessment generation would include:")
            st.write("1. Complete curriculum alignment")
            st.write("2. Targeted criterion strands")
            st.write("3. Appropriate command terms")
            st.write("4. Differentiation strategies")
            st.write("5. Achievement level descriptors")
        else:
            st.warning("Please select curriculum skills and criteria strands first!")
