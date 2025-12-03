# app.py - MYP Math Professional Generator
import streamlit as st
from openai import OpenAI
from datetime import datetime
import json

# Import curriculum database
try:
    from curriculum import MYP_CURRICULUM, CRITERION_STRANDS, GLOBAL_CONTEXTS, KEY_CONCEPTS, COMMAND_TERMS
except:
    # Fallback if curriculum.py doesn't exist yet
    MYP_CURRICULUM = {}
    CRITERION_STRANDS = {}
    GLOBAL_CONTEXTS = []
    KEY_CONCEPTS = []
    COMMAND_TERMS = {}

# Page configuration
st.set_page_config(
    page_title="MYP Math Pro",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Main styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .criterion-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #007bff;
        transition: transform 0.2s;
    }
    
    .criterion-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .curriculum-item {
        background: #e9ecef;
        padding: 0.75rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 4px solid #28a745;
    }
    
    .strand-selected {
        background: #d4edda !important;
        border-color: #155724 !important;
    }
    
    .assessment-output {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 2px solid #dee2e6;
        margin: 1.5rem 0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #e9ecef;
        border-radius: 5px;
        padding: 1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'assessments' not in st.session_state:
    st.session_state.assessments = []
if 'selected_strands' not in st.session_state:
    st.session_state.selected_strands = []
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

# ========== HEADER ==========
st.markdown("""
<div class="main-header">
    <h1>🧮 MYP Mathematics Assessment Generator</h1>
    <h3>Professional Edition • Curriculum-Aligned • AI-Powered</h3>
    <p>Create MYP math assessments with proper criterion strands and curriculum alignment</p>
</div>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API Key
    api_key = st.text_input(
        "OpenAI API Key:",
        type="password",
        placeholder="sk-...",
        help="Required for AI generation. Get from platform.openai.com",
        key="api_input"
    )
    
    if api_key:
        st.session_state.api_key = api_key
        st.success("✅ API key saved")
    
    st.divider()
    
    # Quick Start Guide
    st.header("🚀 Quick Start")
    with st.expander("How to use this tool"):
        st.write("""
        1. **Select Curriculum** - Choose MYP level and topics
        2. **Choose Criteria** - Select specific criterion strands
        3. **Set Context** - Add real-world relevance
        4. **Generate** - Click to create assessment
        5. **Download** - Get your assessment file
        """)
    
    st.divider()
    
    # Assessment Counter
    st.metric("Assessments Created", len(st.session_state.assessments))

# ========== MAIN CONTENT - TABS ==========
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Curriculum", 
    "🎯 Criteria", 
    "🌍 Context", 
    "🚀 Generate"
])

# ========== TAB 1: CURRICULUM SELECTOR ==========
with tab1:
    st.header("Select MYP Curriculum Framework")
    
    if not MYP_CURRICULUM:
        st.error("❌ Curriculum database not loaded. Please create curriculum.py file.")
        st.code("""
        # Create a file called curriculum.py with:
        MYP_CURRICULUM = {
            "MYP 1-3": {...},
            "MYP 4-5 (standard)": {...},
            "MYP 4-5 (extended)": {...}
        }
        """)
    else:
        # MYP Level Selection
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            selected_level = st.selectbox(
                "MYP Level:",
                list(MYP_CURRICULUM.keys()),
                index=0,
                help="Choose based on student age and ability"
            )
        
        with col2:
            selected_branch = st.selectbox(
                "Mathematics Branch:",
                list(MYP_CURRICULUM[selected_level].keys()),
                index=0
            )
        
        with col3:
            selected_topic = st.selectbox(
                "Topic Area:",
                list(MYP_CURRICULUM[selected_level][selected_branch].keys()),
                index=0
            )
        
        # Display Selected Curriculum
        st.markdown(f"""
        ### Selected Curriculum:
        **Level:** {selected_level}  
        **Branch:** {selected_branch}  
        **Topic:** {selected_topic}
        """)
        
        # Skills/Concepts Selection
        st.subheader("Specific Skills & Concepts")
        
        skills = MYP_CURRICULUM[selected_level][selected_branch][selected_topic]
        selected_skills = []
        
        cols = st.columns(2)
        for i, skill in enumerate(skills):
            col = cols[i % 2]
            if col.checkbox(skill, key=f"skill_{i}"):
                selected_skills.append(skill)
        
        if selected_skills:
            st.success(f"✅ Selected {len(selected_skills)} skills/concepts")
            with st.expander("View selected skills"):
                for skill in selected_skills:
                    st.markdown(f'<div class="curriculum-item">• {skill}</div>', unsafe_allow_html=True)
        
        # Store in session
        st.session_state.curriculum = {
            "level": selected_level,
            "branch": selected_branch,
            "topic": selected_topic,
            "skills": selected_skills
        }

# ========== TAB 2: CRITERIA SELECTOR ==========
with tab2:
    st.header("Select Assessment Criteria")
    st.write("Choose specific criterion strands for your assessment")
    
    # Initialize selected strands in session
    if 'selected_strands' not in st.session_state:
        st.session_state.selected_strands = []
    
    # Display all criteria in columns
    col1, col2, col3, col4 = st.columns(4)
    
    all_strands = []
    
    with col1:
        st.markdown("### Criterion A")
        st.write("*Knowing & Understanding*")
        
        for strand, description in CRITERION_STRANDS.get("Criterion A: Knowing and understanding", {}).items():
            key = f"A_{strand}"
            is_selected = st.checkbox(f"A-{strand}: {description[:60]}...", key=key)
            if is_selected:
                all_strands.append(f"A-{strand}: {description}")
    
    with col2:
        st.markdown("### Criterion B")
        st.write("*Investigating Patterns*")
        
        for strand, description in CRITERION_STRANDS.get("Criterion B: Investigating patterns", {}).items():
            key = f"B_{strand}"
            is_selected = st.checkbox(f"B-{strand}: {description[:60]}...", key=key)
            if is_selected:
                all_strands.append(f"B-{strand}: {description}")
    
    with col3:
        st.markdown("### Criterion C")
        st.write("*Communicating*")
        
        for strand, description in CRITERION_STRANDS.get("Criterion C: Communicating", {}).items():
            key = f"C_{strand}"
            is_selected = st.checkbox(f"C-{strand}: {description[:60]}...", key=key)
            if is_selected:
                all_strands.append(f"C-{strand}: {description}")
    
    with col4:
        st.markdown("### Criterion D")
        st.write("*Applying Mathematics*")
        
        for strand, description in CRITERION_STRANDS.get("Criterion D: Applying mathematics in real-life contexts", {}).items():
            key = f"D_{strand}"
            is_selected = st.checkbox(f"D-{strand}: {description[:60]}...", key=key)
            if is_selected:
                all_strands.append(f"D-{strand}: {description}")
    
    # Update session state
    st.session_state.selected_strands = all_strands
    
    # Display selected strands
    if st.session_state.selected_strands:
        st.success(f"✅ Selected {len(st.session_state.selected_strands)} criterion strands")
        
        with st.expander("📋 View Selected Strands"):
            for strand in st.session_state.selected_strands:
                # Extract criterion and description
                parts = strand.split(": ", 1)
                if len(parts) == 2:
                    criterion, desc = parts
                    st.markdown(f"""
                    <div class="strand-selected curriculum-item">
                        <strong>{criterion}</strong><br>
                        {desc}
                    </div>
                    """, unsafe_allow_html=True)
    else:
        st.info("👈 Select at least one criterion strand to continue")

# ========== TAB 3: CONTEXT BUILDER ==========
with tab3:
    st.header("Real-world Context & Settings")
    
    # Context Builder
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("MYP Framework")
        global_context = st.selectbox(
            "Global Context:",
            GLOBAL_CONTEXTS if GLOBAL_CONTEXTS else ["Select...", "Scientific innovation", "Fairness"],
            index=0
        )
        
        key_concept = st.selectbox(
            "Key Concept:",
            KEY_CONCEPTS if KEY_CONCEPTS else ["Select...", "Relationships", "Change"],
            index=0
        )
    
    with col2:
        st.subheader("Command Terms")
        command_terms = st.multiselect(
            "Select Command Terms:",
            list(COMMAND_TERMS.keys()) if COMMAND_TERMS else ["Describe", "Explain", "Justify"],
            default=["Explain", "Justify"]
        )
        
        # Show descriptions
        if command_terms:
            with st.expander("Command Term Definitions"):
                for term in command_terms:
                    desc = COMMAND_TERMS.get(term, "No definition available")
                    st.write(f"**{term}:** {desc}")
    
    # Real-world Context
    st.subheader("Real-world Situation")
    context_description = st.text_area(
        "Describe the authentic real-world situation for this assessment:",
        height=120,
        placeholder="Example: 'Students will analyze public transportation data to optimize bus routes in their city, considering factors like population density, traffic patterns, and environmental impact...'",
        help="Make it authentic and relevant to students' lives"
    )
    
    # Assessment Settings
    st.subheader("Assessment Settings")
    col1, col2 = st.columns(2)
    
    with col1:
        duration = st.selectbox(
            "Estimated Duration:",
            ["30 minutes", "45 minutes", "60 minutes", "90 minutes", "120 minutes", "Extended project"]
        )
        
        format_type = st.selectbox(
            "Assessment Format:",
            ["Written test", "Investigation", "Project", "Presentation", "Portfolio"]
        )
    
    with col2:
        group_size = st.selectbox(
            "Group/Individual:",
            ["Individual", "Pairs", "Small groups (3-4)", "Whole class"]
        )
        
        resources = st.multiselect(
            "Required Resources:",
            ["Calculator", "Graph paper", "Ruler/Protractor", "Computer", "Graphing software", "Measuring tools", "Internet access"]
        )
    
    # Store in session
    st.session_state.context = {
        "global_context": global_context,
        "key_concept": key_concept,
        "command_terms": command_terms,
        "description": context_description,
        "duration": duration,
        "format": format_type,
        "group_size": group_size,
        "resources": resources
    }

# ========== TAB 4: GENERATE ASSESSMENT ==========
with tab4:
    st.header("Generate Assessment")
    
    # Check if ready to generate
    ready_to_generate = True
    warnings = []
    
    # Check API key
    if not st.session_state.api_key:
        warnings.append("❌ OpenAI API key not configured")
        ready_to_generate = False
    
    # Check curriculum selected
    if 'curriculum' not in st.session_state or not st.session_state.curriculum.get('skills'):
        warnings.append("⚠️ No curriculum skills selected")
        ready_to_generate = False
    
    # Check criteria selected
    if not st.session_state.selected_strands:
        warnings.append("⚠️ No criterion strands selected")
        ready_to_generate = False
    
    # Check context
    if 'context' not in st.session_state or not st.session_state.context.get('description'):
        warnings.append("⚠️ Real-world context not provided")
    
    # Display warnings
    if warnings:
        st.warning("Please address the following:")
        for warning in warnings:
            st.write(warning)
    
    # Assessment Title
    assessment_title = st.text_input(
        "Assessment Title:",
        placeholder="e.g., 'Optimizing Urban Transportation: A Data Analysis Project'",
        help="Create an engaging title that reflects the real-world context"
    )
    
    # Generate Button
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col2:
        generate_clicked = st.button(
            "✨ GENERATE ASSESSMENT",
            type="primary",
            use_container_width=True,
            disabled=not ready_to_generate
        )
    
    with col3:
        if st.button("🔄 Reset All", use_container_width=True):
            st.session_state.selected_strands = []
            st.session_state.curriculum = {}
            st.session_state.context = {}
            st.rerun()
    
    # Generate Assessment
    if generate_clicked and ready_to_generate:
        with st.spinner("🤖 Creating your curriculum-aligned assessment... (20-30 seconds)"):
            try:
                # Build the prompt
                curriculum = st.session_state.curriculum
                context = st.session_state.context
                
                prompt = f"""
                CREATE A COMPREHENSIVE MYP MATHEMATICS ASSESSMENT
                
                ====== CURRICULUM ALIGNMENT ======
                MYP Level: {curriculum.get('level', 'Not specified')}
                Mathematics Branch: {curriculum.get('branch', 'Not specified')}
                Topic Area: {curriculum.get('topic', 'Not specified')}
                Specific Skills/Concepts:
                {chr(10).join(['• ' + skill for skill in curriculum.get('skills', [])])}
                
                ====== ASSESSMENT CRITERIA ======
                {chr(10).join(['• ' + strand for strand in st.session_state.selected_strands])}
                
                ====== REAL-WORLD CONTEXT ======
                Global Context: {context.get('global_context', 'Not specified')}
                Key Concept: {context.get('key_concept', 'Not specified')}
                Command Terms to Use: {', '.join(context.get('command_terms', []))}
                
                Authentic Situation: {context.get('description', 'Not specified')}
                
                ====== ASSESSMENT DETAILS ======
                Title: {assessment_title}
                Format: {context.get('format', 'Written test')}
                Duration: {context.get('duration', '60 minutes')}
                Grouping: {context.get('group_size', 'Individual')}
                Resources: {', '.join(context.get('resources', []))}
                
                ====== REQUIREMENTS ======
                Create a complete, ready-to-use assessment that:
                
                1. Is age-appropriate for the MYP level
                2. Clearly targets EACH selected criterion strand
                3. Uses the specified command terms appropriately
                4. Has clear, scaffolded instructions
                5. Includes varied question types (calculation, explanation, application, justification)
                6. Connects authentically to the real-world context
                7. Provides opportunities for differentiation
                8. Includes extension questions for advanced students
                9. Specifies assessment criteria clearly for students
                10. Suggests implementation guidance for teachers
                
                ====== OUTPUT FORMAT ======
                Please structure your response as follows:
                
                ASSESSMENT TITLE
                [The assessment title]
                
                CURRICULUM CONNECTION
                [Explain how this assessment connects to the MYP curriculum]
                
                REAL-WORLD CONTEXT
                [Describe the authentic situation students will engage with]
                
                LEARNING OBJECTIVES
                • [Objective 1]
                • [Objective 2]
                • [Objective 3]
                
                ASSESSMENT CRITERIA
                [List and explain which criteria strands are being assessed]
                
                TASK INSTRUCTIONS
                [Clear, student-friendly instructions]
                
                ASSESSMENT TASKS
                Part 1: [Task focusing on Criterion A if selected]
                Part 2: [Task focusing on Criterion B if selected]
                Part 3: [Task focusing on Criterion C if selected]
                Part 4: [Task focusing on Criterion D if selected]
                
                MARKING GUIDANCE
                [Suggestions for assessing each criterion]
                
                DIFFERENTIATION STRATEGIES
                Support: [For students needing help]
                Extension: [For advanced students]
                
                TEACHER NOTES
                [Implementation tips, common misconceptions, resources]
                """
                
                # Call OpenAI
                client = OpenAI(api_key=st.session_state.api_key)
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system", 
                            "content": """You are an expert IB MYP Mathematics curriculum developer with 20 years experience. 
                            You create engaging, authentic, curriculum-aligned assessments that develop mathematical thinking.
                            You are meticulous about proper criterion alignment and real-world relevance."""
                        },
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=2500
                )
                
                # Get the generated assessment
                assessment_content = response.choices[0].message.content
                
                # Create assessment object
                assessment = {
                    "id": len(st.session_state.assessments) + 1,
                    "title": assessment_title if assessment_title else f"MYP {curriculum.get('topic', 'Math')} Assessment",
                    "content": assessment_content,
                    "metadata": {
                        "curriculum": curriculum,
                        "strands": st.session_state.selected_strands,
                        "context": context,
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "tokens": response.usage.total_tokens
                    }
                }
                
                # Save to session
                st.session_state.assessments.append(assessment)
                
                # Display success
                st.success("✅ Assessment Generated Successfully!")
                st.balloons()
                
                # Display assessment
                st.markdown("---")
                st.markdown(f"## 📄 {assessment['title']}")
                st.markdown(f"*Generated: {assessment['metadata']['date']}*")
                st.markdown("---")
                
                # Show in a nice box
                st.markdown(f'<div class="assessment-output">{assessment_content}</div>', unsafe_allow_html=True)
                
                # Create downloadable content
                full_content = f"""
                MYP MATHEMATICS ASSESSMENT
                ===========================
                
                TITLE: {assessment['title']}
                
                GENERATED: {assessment['metadata']['date']}
                
                CURRICULUM ALIGNMENT:
                • Level: {curriculum.get('level', 'N/A')}
                • Branch: {curriculum.get('branch', 'N/A')}
                • Topic: {curriculum.get('topic', 'N/A')}
                • Skills: {', '.join(curriculum.get('skills', []))}
                
                ASSESSMENT CRITERIA:
                {chr(10).join(['• ' + strand for strand in st.session_state.selected_strands])}
                
                CONTEXT:
                • Global Context: {context.get('global_context', 'N/A')}
                • Key Concept: {context.get('key_concept', 'N/A')}
                • Command Terms: {', '.join(context.get('command_terms', []))}
                • Real-world Situation: {context.get('description', 'N/A')}
                
                ASSESSMENT DETAILS:
                • Format: {context.get('format', 'N/A')}
                • Duration: {context.get('duration', 'N/A')}
                • Grouping: {context.get('group_size', 'N/A')}
                • Resources: {', '.join(context.get('resources', []))}
                
                {'='*50}
                
                {assessment_content}
                
                {'='*50}
                
                AI-GENERATED ASSESSMENT
                MYP Mathematics Professional Generator
                Generated with OpenAI GPT-4
                """
                
                # Download button
                st.download_button(
                    "📥 Download Complete Assessment",
                    full_content,
                    file_name=f"MYP_{curriculum.get('topic', 'Math')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"❌ Error generating assessment: {str(e)}")
                st.info("Common issues: 1) API key invalid 2) No credits 3) Network error")

# ========== PREVIOUS ASSESSMENTS ==========
if st.session_state.assessments:
    st.markdown("---")
    st.header("📚 Your Assessment Library")
    
    for assessment in reversed(st.session_state.assessments):
        with st.expander(f"📄 {assessment['title']} - {assessment['metadata']['date']}"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(f"**Topic:** {assessment['metadata']['curriculum'].get('topic', 'N/A')}")
                st.write(f"**Level:** {assessment['metadata']['curriculum'].get('level', 'N/A')}")
                st.write(f"**Criteria:** {len(assessment['metadata']['strands'])} strands")
            
            with col2:
                st.download_button(
                    "Download",
                    assessment['content'],
                    file_name=f"assessment_{assessment['id']}.txt",
                    key=f"dl_{assessment['id']}",
                    use_container_width=True
                )
            
            st.markdown("---")
            st.markdown(assessment['content'])

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p><strong>MYP Mathematics Professional Generator</strong> • Curriculum-Aligned • Criterion-Focused • AI-Powered</p>
    <p>Designed for IB MYP Mathematics Teachers • Version 2.0</p>
</div>
""", unsafe_allow_html=True)# Add imports at top
from math_tools import equation_editor, latex_editor_with_preview, render_mathjax
from geogebra_tools import geogebra_calculator, geogebra_geometry, geogebra_graphing

# Add a new tab for tools
def show_math_tools():
    st.header("🛠️ Math Content Tools")
    
    tool_choice = st.selectbox(
        "Choose Tool:",
        [
            "GeoGebra Calculator",
            "GeoGebra Geometry",
            "Equation Editor", 
            "LaTeX Editor",
            "Graph Generator"
        ]
    )
    
    if tool_choice == "GeoGebra Calculator":
        geogebra_calculator()
        
    elif tool_choice == "GeoGebra Geometry":
        geogebra_geometry()
        
    elif tool_choice == "Equation Editor":
        equation_editor()
        
    elif tool_choice == "LaTeX Editor":
        latex_code = latex_editor_with_preview()
        # You can save this to use in assessments
        
    # Add to your tabs
    tabs = st.tabs(["Generate", "Library", "Tools", "Settings"])
    with tabs[2]:  # Tools tab
        show_math_tools()
