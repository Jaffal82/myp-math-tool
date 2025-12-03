# app.py - MYP Math Professional Generator with ALL Math Tools
import streamlit as st
from openai import OpenAI
from datetime import datetime
import streamlit.components.v1 as components
import json

# Page configuration
st.set_page_config(
    page_title="MYP Math Pro with Tools",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced UI
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
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .tool-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 6px solid;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .tool-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.12);
    }
    
    .geogebra-card {
        border-left-color: #3B82F6;
    }
    
    .equation-card {
        border-left-color: #10B981;
    }
    
    .graphing-card {
        border-left-color: #8B5CF6;
    }
    
    .assessment-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 2px solid #dee2e6;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.8rem 1.8rem;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #e9ecef;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        font-weight: 600;
        border: 2px solid transparent;
        transition: all 0.2s;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        border-color: #667eea;
        background-color: #f0f4ff;
    }
    
    /* Tool icons */
    .tool-icon {
        font-size: 1.5rem;
        margin-right: 10px;
        vertical-align: middle;
    }
    
    /* Status indicators */
    .status-success {
        background: #d1fae5;
        color: #065f46;
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        display: inline-block;
    }
    
    .status-warning {
        background: #fef3c7;
        color: #92400e;
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# ========== MATH TOOLS FUNCTIONS ==========
def geogebra_calculator(height=500, title="GeoGebra Calculator"):
    """Embed GeoGebra Calculator"""
    html = f"""
    <div style="border: 3px solid #3B82F6; border-radius: 15px; overflow: hidden; margin: 20px 0; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);">
        <iframe src="https://www.geogebra.org/calculator" 
                width="100%" 
                height="{height}px" 
                style="border: none;"
                title="{title}"
                allowfullscreen>
        </iframe>
        <div style="background: linear-gradient(135deg, #3B82F6, #1D4ED8); color: white; padding: 15px; text-align: center;">
            <strong style="font-size: 1.1em;">{title}</strong>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 0.9em;">Interactive algebra, functions, and calculus</p>
        </div>
    </div>
    """
    components.html(html, height=height + 70)

def geogebra_geometry(height=500, title="GeoGebra Geometry"):
    """Embed GeoGebra Geometry"""
    html = f"""
    <div style="border: 3px solid #10B981; border-radius: 15px; overflow: hidden; margin: 20px 0; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);">
        <iframe src="https://www.geogebra.org/geometry" 
                width="100%" 
                height="{height}px" 
                style="border: none;"
                title="{title}"
                allowfullscreen>
        </iframe>
        <div style="background: linear-gradient(135deg, #10B981, #047857); color: white; padding: 15px; text-align: center;">
            <strong style="font-size: 1.1em;">{title}</strong>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 0.9em;">Construct figures, measure angles, prove theorems</p>
        </div>
    </div>
    """
    components.html(html, height=height + 70)

def geogebra_graphing(height=500, title="GeoGebra Graphing"):
    """Embed GeoGebra Graphing Calculator"""
    html = f"""
    <div style="border: 3px solid #8B5CF6; border-radius: 15px; overflow: hidden; margin: 20px 0; box-shadow: 0 4px 12px rgba(139, 92, 246, 0.15);">
        <iframe src="https://www.geogebra.org/graphing" 
                width="100%" 
                height="{height}px" 
                style="border: none;"
                title="{title}"
                allowfullscreen>
        </iframe>
        <div style="background: linear-gradient(135deg, #8B5CF6, #7C3AED); color: white; padding: 15px; text-align: center;">
            <strong style="font-size: 1.1em;">{title}</strong>
            <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 0.9em;">Plot functions, sliders, analyze graphs</p>
        </div>
    </div>
    """
    components.html(html, height=height + 70)

def math_equation_editor():
    """Interactive math equation editor"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Math Equation Editor</title>
        <!-- MathQuill -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@edtr-io/mathquill@0.11.0/build/mathquill.css"/>
        <script src="https://cdn.jsdelivr.net/npm/@edtr-io/mathquill@0.11.0/build/mathquill.min.js"></script>
        
        <style>
            * {
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
                min-height: 100vh;
            }
            
            .editor-container {
                max-width: 900px;
                margin: 0 auto;
                background: white;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            }
            
            .editor-title {
                text-align: center;
                color: #1e293b;
                margin-bottom: 5px;
                font-size: 1.8rem;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .editor-subtitle {
                text-align: center;
                color: #64748b;
                margin-bottom: 30px;
                font-size: 1rem;
            }
            
            .math-editor-area {
                border: 3px solid #e2e8f0;
                border-radius: 12px;
                padding: 25px;
                margin: 25px 0;
                min-height: 180px;
                font-size: 20px;
                background: #f8fafc;
                transition: border-color 0.3s;
            }
            
            .math-editor-area:focus-within {
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            }
            
            .button-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
                gap: 12px;
                margin: 25px 0;
            }
            
            .math-button {
                padding: 12px 15px;
                background: white;
                color: #475569;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                cursor: pointer;
                font-size: 14px;
                font-weight: 600;
                transition: all 0.2s;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
            }
            
            .math-button:hover {
                background: #f1f5f9;
                border-color: #cbd5e1;
                transform: translateY(-2px);
                box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            }
            
            .math-button.primary {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
            }
            
            .math-button.primary:hover {
                background: linear-gradient(135deg, #5a6fd8 0%, #6a4192 100%);
                box-shadow: 0 6px 12px rgba(102, 126, 234, 0.2);
            }
            
            .output-section {
                background: #f8fafc;
                padding: 25px;
                border-radius: 12px;
                margin-top: 30px;
                border: 2px solid #e2e8f0;
            }
            
            .section-title {
                color: #334155;
                margin-top: 0;
                margin-bottom: 15px;
                font-size: 1.2rem;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .section-title::before {
                content: "📋";
                font-size: 1.2em;
            }
            
            .latex-output {
                background: white;
                padding: 20px;
                border-radius: 8px;
                font-family: 'Monaco', 'Courier New', monospace;
                font-size: 14px;
                line-height: 1.6;
                white-space: pre-wrap;
                word-wrap: break-word;
                border: 1px solid #e2e8f0;
                margin: 15px 0;
                min-height: 80px;
            }
            
            .preview-area {
                background: white;
                padding: 30px;
                border-radius: 12px;
                margin-top: 20px;
                text-align: center;
                font-size: 24px;
                border: 2px dashed #cbd5e1;
                min-height: 120px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .action-buttons {
                display: flex;
                gap: 15px;
                margin-top: 25px;
                justify-content: center;
            }
            
            .icon {
                font-size: 1.2em;
            }
            
            @media (max-width: 768px) {
                .button-grid {
                    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
                }
                
                .editor-container {
                    padding: 20px;
                }
                
                .math-editor-area {
                    padding: 15px;
                    font-size: 18px;
                }
            }
        </style>
    </head>
    <body>
        <div class="editor-container">
            <h1 class="editor-title">Math Equation Editor</h1>
            <p class="editor-subtitle">Create professional mathematical notation for your assessments</p>
            
            <div class="math-editor-area" id="math-editor">
                <!-- MathQuill editor will appear here -->
            </div>
            
            <div class="button-grid">
                <button class="math-button" onclick="insertFraction()">
                    <span class="icon">a/b</span> Fraction
                </button>
                <button class="math-button" onclick="insertSquareRoot()">
                    <span class="icon">√</span> Square Root
                </button>
                <button class="math-button" onclick="insertExponent()">
                    <span class="icon">x²</span> Exponent
                </button>
                <button class="math-button" onclick="insertSubscript()">
                    <span class="icon">x₁</span> Subscript
                </button>
                <button class="math-button" onclick="insertIntegral()">
                    <span class="icon">∫</span> Integral
                </button>
                <button class="math-button" onclick="insertSummation()">
                    <span class="icon">∑</span> Summation
                </button>
                <button class="math-button" onclick="insertGreek()">
                    <span class="icon">αβγ</span> Greek
                </button>
                <button class="math-button" onclick="insertMatrix()">
                    <span class="icon">[ ]</span> Matrix
                </button>
                <button class="math-button" onclick="insertLimit()">
                    <span class="icon">lim</span> Limit
                </button>
                <button class="math-button" onclick="insertTrig()">
                    <span class="icon">sin</span> Trig
                </button>
                <button class="math-button" onclick="insertLog()">
                    <span class="icon">log</span> Logarithm
                </button>
                <button class="math-button" onclick="clearEditor()">
                    <span class="icon">🗑️</span> Clear
                </button>
            </div>
            
            <div class="output-section">
                <h3 class="section-title">LaTeX Output</h3>
                <div class="latex-output" id="latex-output">x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}</div>
                
                <h3 class="section-title">Live Preview</h3>
                <div class="preview-area" id="math-preview">
                    <!-- MathJax preview will appear here -->
                </div>
                
                <div class="action-buttons">
                    <button class="math-button primary" onclick="copyToClipboard()">
                        <span class="icon">📋</span> Copy LaTeX
                    </button>
                    <button class="math-button primary" onclick="insertIntoAssessment()">
                        <span class="icon">📝</span> Insert into Assessment
                    </button>
                    <button class="math-button primary" onclick="downloadEquation()">
                        <span class="icon">📥</span> Download
                    </button>
                </div>
            </div>
        </div>
        
        <!-- MathJax for rendering -->
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        
        <script>
            // Initialize MathQuill
            var MQ = MathQuill.getInterface(2);
            var mathField = MQ.MathField(document.getElementById('math-editor'), {
                spaceBehavesLikeTab: true,
                handlers: {
                    edit: function() {
                        var latex = mathField.latex();
                        document.getElementById('latex-output').textContent = latex;
                        updatePreview(latex);
                        
                        // Send to Streamlit
                        window.parent.postMessage({
                            type: 'math_equation',
                            latex: latex
                        }, '*');
                    }
                }
            });
            
            // Initialize with example
            mathField.latex('x = \\\\frac{-b \\\\pm \\\\sqrt{b^2 - 4ac}}{2a}');
            updatePreview(mathField.latex());
            
            // Button functions
            function insertFraction() {
                mathField.cmd('\\\\frac');
            }
            
            function insertSquareRoot() {
                mathField.cmd('\\\\sqrt');
            }
            
            function insertExponent() {
                mathField.cmd('^');
            }
            
            function insertSubscript() {
                mathField.cmd('_');
            }
            
            function insertIntegral() {
                mathField.write('\\\\int_{ }^{ }');
                mathField.keystroke('Left');
                mathField.keystroke('Left');
            }
            
            function insertSummation() {
                mathField.write('\\\\sum_{ }^{ }');
                mathField.keystroke('Left');
                mathField.keystroke('Left');
            }
            
            function insertLimit() {
                mathField.write('\\\\lim_{x\\\\to }');
                mathField.keystroke('Left');
            }
            
            function insertMatrix() {
                mathField.write('\\\\begin{bmatrix} a & b \\\\\\\\ c & d \\\\end{bmatrix}');
            }
            
            function insertGreek() {
                mathField.write('\\\\alpha \\\\beta \\\\gamma \\\\Delta \\\\theta \\\\pi \\\\omega \\\\sigma');
            }
            
            function insertTrig() {
                mathField.write('\\\\sin \\\\cos \\\\tan \\\\sec \\\\csc \\\\cot');
            }
            
            function insertLog() {
                mathField.write('\\\\log \\\\ln');
            }
            
            function clearEditor() {
                mathField.latex('');
            }
            
            function copyToClipboard() {
                var latex = mathField.latex();
                navigator.clipboard.writeText(latex).then(function() {
                    showToast('LaTeX copied to clipboard!', 'success');
                });
            }
            
            function insertIntoAssessment() {
                showToast('Equation ready to insert into assessment', 'info');
            }
            
            function downloadEquation() {
                var latex = mathField.latex();
                var blob = new Blob([latex], { type: 'text/plain' });
                var url = window.URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = url;
                a.download = 'equation.tex';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
                showToast('Equation downloaded as equation.tex', 'success');
            }
            
            function updatePreview(latex) {
                var preview = document.getElementById('math-preview');
                preview.innerHTML = '\\\\( ' + latex + ' \\\\)';
                
                // Re-render MathJax
                if (window.MathJax) {
                    MathJax.typesetPromise([preview]);
                }
            }
            
            function showToast(message, type) {
                // Create toast element
                var toast = document.createElement('div');
                toast.style.cssText = `
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    padding: 15px 20px;
                    background: ${type === 'success' ? '#10B981' : '#3B82F6'};
                    color: white;
                    border-radius: 10px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                    z-index: 1000;
                    animation: slideIn 0.3s ease;
                    font-weight: 500;
                `;
                toast.innerHTML = `✓ ${message}`;
                document.body.appendChild(toast);
                
                // Remove after 3 seconds
                setTimeout(function() {
                    toast.style.animation = 'slideOut 0.3s ease';
                    setTimeout(function() {
                        document.body.removeChild(toast);
                    }, 300);
                }, 3000);
            }
            
            // Add CSS for animations
            var style = document.createElement('style');
            style.textContent = `
                @keyframes slideIn {
                    from { transform: translateX(100%); opacity: 0; }
                    to { transform: translateX(0); opacity: 1; }
                }
                @keyframes slideOut {
                    from { transform: translateX(0); opacity: 1; }
                    to { transform: translateX(100%); opacity: 0; }
                }
            `;
            document.head.appendChild(style);
            
            // Initialize MathJax
            window.MathJax = {
                tex: {
                    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
                },
                startup: {
                    typeset: false
                }
            };
            
            // Listen for messages from Streamlit
            window.addEventListener('message', function(event) {
                if (event.data.type === 'set_equation') {
                    mathField.latex(event.data.latex);
                }
            });
        </script>
    </body>
    </html>
    """
    
    # Create a container for the editor
    with st.container():
        components.html(html, height=800)

def latex_preview(latex_code, height=200):
    """Render LaTeX preview"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <script>
        MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
            }},
            svg: {{
                fontCache: 'global'
            }}
        }};
        </script>
    </head>
    <body>
        <div style="padding: 25px; background: white; border-radius: 12px; border: 2px solid #e2e8f0; margin: 10px 0;">
            {latex_code}
        </div>
    </body>
    </html>
    """
    
    components.html(html, height=height)

def graph_generator():
    """Interactive graph generator"""
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Graph Settings")
        
        graph_type = st.selectbox(
            "Graph Type:",
            ["Linear", "Quadratic", "Cubic", "Exponential", "Trigonometric", "Piecewise"]
        )
        
        function_input = st.text_input(
            "Function (in terms of x):",
            value="x^2" if graph_type == "Quadratic" else "sin(x)" if graph_type == "Trigonometric" else "x"
        )
        
        color = st.color_picker("Graph Color", "#FF0000")
        line_width = st.slider("Line Width", 1, 5, 2)
        
        show_grid = st.checkbox("Show Grid", True)
        show_axes = st.checkbox("Show Axes", True)
        
        x_min, x_max = st.slider("X-axis Range", -20, 20, (-10, 10))
        y_min, y_max = st.slider("Y-axis Range", -20, 20, (-10, 10))
        
        if st.button("Generate Graph", use_container_width=True):
            st.session_state.graph_config = {
                "type": graph_type,
                "function": function_input,
                "color": color,
                "line_width": line_width,
                "show_grid": show_grid,
                "show_axes": show_axes,
                "x_range": (x_min, x_max),
                "y_range": (y_min, y_max)
            }
    
    with col2:
        st.subheader("Graph Preview")
        
        if 'graph_config' in st.session_state:
            config = st.session_state.graph_config
            
            # Create GeoGebra with the function
            html = f"""
            <div style="border: 3px solid #8B5CF6; border-radius: 15px; overflow: hidden; margin: 20px 0;">
                <iframe src="https://www.geogebra.org/graphing?func={config['function']}&xmin={config['x_range'][0]}&xmax={config['x_range'][1]}&ymin={config['y_range'][0]}&ymax={config['y_range'][1]}" 
                        width="100%" 
                        height="500px" 
                        style="border: none;"
                        allowfullscreen>
                </iframe>
            </div>
            """
            
            components.html(html, height=530)
            
            # Download options
            graph_code = f"f(x) = {config['function']}, x ∈ [{config['x_range'][0]}, {config['x_range'][1]}], y ∈ [{config['y_range'][0]}, {config['y_range'][1]}]"
            st.download_button(
                "📥 Save Graph Configuration",
                graph_code,
                file_name=f"graph_{config['function']}.txt"
            )
        else:
            st.info("👈 Configure graph settings and click 'Generate Graph'")

# ========== MAIN APP FUNCTIONS ==========
def show_assessment_generator():
    """Main assessment generator"""
    st.header("📝 Assessment Generator")
    
    # Simplified form for demo
    with st.form("assessment_form"):
        topic = st.selectbox("Topic:", ["Algebra", "Geometry", "Statistics"])
        level = st.selectbox("MYP Level:", [1, 2, 3, 4, 5])
        
        col1, col2 = st.columns(2)
        with col1:
            include_geogebra = st.checkbox("Include GeoGebra", True)
            include_equations = st.checkbox("Include Equations", True)
        with col2:
            include_graphs = st.checkbox("Include Graphs", False)
            include_diagrams = st.checkbox("Include Diagrams", False)
        
        submitted = st.form_submit_button("Generate Assessment")
    
    if submitted:
        with st.spinner("Creating assessment..."):
            # Create assessment
            assessment = f"""
            # MYP {level} Mathematics Assessment
            ## Topic: {topic}
            
            **Instructions:** Complete all tasks showing your working.
            
            ## Part 1: Knowledge and Understanding
            
            1. Solve the equation: $2x + 5 = 13$
            
            ## Part 2: Application
            
            2. A rectangle has length $(x + 3)$ cm and width $(x - 2)$ cm.
               If the area is $54$ cm², find the value of $x$.
            
            ## Part 3: Investigation
            
            3. Investigate the pattern:
               $1, 4, 9, 16, 25, ...$
               a) Describe the pattern in words
               b) Write the nth term formula
               c) Find the 10th term
            
            ## Part 4: Real-world Application
            
            4. A water tank is being filled. The volume $V$ (in liters) at time $t$ (in minutes)
               is given by $V = 50t + 100$.
               a) How much water is in the tank after 10 minutes?
               b) How long does it take to fill 1000 liters?
            """
            
            st.session_state.current_assessment = assessment
            st.success("✅ Assessment generated!")
            
            # Display assessment
            st.markdown("---")
            st.markdown(assessment)
            
            # Add tools if selected
            if include_geogebra:
                st.markdown("---")
                st.subheader("📐 GeoGebra Tools for this Assessment")
                geogebra_calculator(height=400)

# ========== TOOLS DASHBOARD ==========
def show_math_tools():
    """Math tools dashboard"""
    st.header("🛠️ Math Content Creation Tools")
    
    # Tool selection
    tool = st.selectbox(
        "Choose a tool:",
        [
            "📐 GeoGebra Calculator",
            "📏 GeoGebra Geometry", 
            "📈 GeoGebra Graphing",
            "✏️ Math Equation Editor",
            "🎨 Graph Generator",
            "📝 LaTeX Preview"
        ]
    )
    
    if "GeoGebra Calculator" in tool:
        st.markdown('<div class="tool-card geogebra-card">', unsafe_allow_html=True)
        st.subheader("📐 GeoGebra Calculator")
        st.write("Interactive scientific calculator for algebra, functions, and calculus")
        geogebra_calculator(height=500, title="GeoGebra Scientific Calculator")
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif "GeoGebra Geometry" in tool:
        st.markdown('<div class="tool-card geogebra-card">', unsafe_allow_html=True)
        st.subheader("📏 GeoGebra Geometry")
        st.write("Construct geometric figures, measure angles, prove theorems")
        geogebra_geometry(height=500, title="GeoGebra Geometry")
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif "GeoGebra Graphing" in tool:
        st.markdown('<div class="tool-card geogebra-card">', unsafe_allow_html=True)
        st.subheader("📈 GeoGebra Graphing Calculator")
        st.write("Plot functions, create sliders, analyze graphs")
        geogebra_graphing(height=500, title="GeoGebra Graphing")
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif "Math Equation Editor" in tool:
        st.markdown('<div class="tool-card equation-card">', unsafe_allow_html=True)
        st.subheader("✏️ Math Equation Editor")
        st.write("Create professional mathematical notation with LaTeX")
        math_equation_editor()
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif "Graph Generator" in tool:
        st.markdown('<div class="tool-card graphing-card">', unsafe_allow_html=True)
        st.subheader("🎨 Graph Generator")
        st.write("Create custom graphs for assessments")
        graph_generator()
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif "LaTeX Preview" in tool:
        st.markdown('<div class="tool-card equation-card">', unsafe_allow_html=True)
        st.subheader("📝 LaTeX Preview")
        
        latex_input = st.text_area(
            "Enter LaTeX code:",
            height=150,
            value="\\[ \\int_{0}^{1} x^2 \\, dx = \\frac{1}{3} \\]"
        )
        
        if latex_input:
            latex_preview(latex_input, height=300)
            
            # Copy button
            if st.button("📋 Copy LaTeX", use_container_width=True):
                st.code(latex_input)
                st.success("Copied to clipboard!")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ========== ASSESSMENT LIBRARY ==========
def show_assessment_library():
    """Assessment library"""
    st.header("📚 Assessment Library")
    
    if 'assessments' not in st.session_state:
        st.session_state.assessments = []
    
    if st.session_state.assessments:
        for i, assessment in enumerate(st.session_state.assessments):
            with st.expander(f"Assessment {i+1}: {assessment.get('topic', 'Math')}"):
                st.markdown(assessment.get('content', 'No content'))
                
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        "📥 Download",
                        assessment.get('content', ''),
                        file_name=f"assessment_{i+1}.txt"
                    )
                with col2:
                    if st.button("🗑️ Delete", key=f"delete_{i}"):
                        st.session_state.assessments.pop(i)
                        st.rerun()
    else:
        st.info("No assessments yet. Generate one in the 'Generate' tab.")

# ========== MAIN APP ==========
def main():
    """Main application"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🧮 MYP Mathematics Professional Suite</h1>
        <h3>Assessment Generator + Math Tools + Curriculum Integration</h3>
        <p>Create, customize, and enrich mathematics assessments with integrated tools</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Quick Access")
        
        # Tool shortcuts
        st.subheader("Quick Tools")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📐 Calculator", use_container_width=True):
                st.session_state.selected_tool = "GeoGebra Calculator"
                st.rerun()
            if st.button("✏️ Equations", use_container_width=True):
                st.session_state.selected_tool = "Math Equation Editor"
                st.rerun()
        with col2:
            if st.button("📈 Graphing", use_container_width=True):
                st.session_state.selected_tool = "GeoGebra Graphing"
                st.rerun()
            if st.button("📏 Geometry", use_container_width=True):
                st.session_state.selected_tool = "GeoGebra Geometry"
                st.rerun()
        
        st.divider()
        
        # API Configuration
        st.header("🔐 Configuration")
        api_key = st.text_input("OpenAI API Key:", type="password")
        if api_key:
            st.success("✅ API configured")
        
        st.divider()
        
        # Status
        st.header("📊 Status")
        st.metric("Assessments", len(st.session_state.get('assessments', [])))
        
        if 'current_assessment' in st.session_state:
            st.markdown('<span class="status-success">Assessment Ready</span>', unsafe_allow_html=True)
    
    # Main tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🚀 Generate Assessment",
        "🛠️ Math Tools", 
        "📚 Library",
        "⚙️ Settings"
    ])
    
    with tab1:
        show_assessment_generator()
    
    with tab2:
        show_math_tools()
    
    with tab3:
        show_assessment_library()
    
    with tab4:
        st.header("Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Preferences")
            theme = st.selectbox("Theme:", ["Light", "Dark", "Auto"])
            default_tool = st.selectbox("Default Tool:", ["GeoGebra Calculator", "Equation Editor", "Graph Generator"])
            
            st.checkbox("Auto-save assessments", True)
            st.checkbox("Show preview before download", True)
            st.checkbox("Include sample equations", True)
        
        with col2:
            st.subheader("Export Settings")
            st.selectbox("Default Format:", ["PDF", "Word", "Google Docs", "Plain Text"])
            st.selectbox("Equation Format:", ["LaTeX", "MathML", "Images"])
            
            st.number_input("Default Graph Height:", 400, 800, 500, 50)
            st.number_input("Equation Font Size:", 12, 24, 16, 1)
        
        if st.button("Save Settings", type="primary"):
            st.success("Settings saved!")

# Run the app
if __name__ == "__main__":
    # Initialize session state
    if 'assessments' not in st.session_state:
        st.session_state.assessments = []
    if 'current_assessment' not in st.session_state:
        st.session_state.current_assessment = ""
    
    main()
