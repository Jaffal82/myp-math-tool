# math_tools_page.py
import streamlit as st
import streamlit.components.v1 as components

def math_tools_dashboard():
    """Complete math tools dashboard"""
    
    st.title("🛠️ Math Tools for Assessments")
    st.markdown("Create interactive math content for your assessments")
    
    # Tool selector
    tool = st.selectbox(
        "Choose a tool:",
        [
            "📐 GeoGebra Calculator",
            "📏 GeoGebra Geometry", 
            "📈 GeoGebra Graphing",
            "✏️ Equation Editor",
            "📝 LaTeX Editor",
            "🎨 Graph Generator",
            "📊 Statistical Tools"
        ]
    )
    
    if "GeoGebra Calculator" in tool:
        st.subheader("GeoGebra Calculator")
        st.write("Interactive calculator for algebra and functions")
        
        html = """
        <div style="border: 3px solid #3B82F6; border-radius: 15px; overflow: hidden; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <iframe src="https://www.geogebra.org/calculator" 
                    width="100%" 
                    height="600px" 
                    style="border: none;">
            </iframe>
            <div style="background: linear-gradient(135deg, #3B82F6, #1D4ED8); color: white; padding: 15px; text-align: center;">
                <strong style="font-size: 1.2em;">GeoGebra Scientific Calculator</strong>
                <p style="margin: 5px 0 0 0; opacity: 0.9;">Drag points, sliders, create functions, explore derivatives</p>
            </div>
        </div>
        """
        
        components.html(html, height=650)
        
        # Customization options
        st.subheader("Customize")
        col1, col2 = st.columns(2)
        with col1:
            show_grid = st.checkbox("Show Grid", True)
            show_axes = st.checkbox("Show Axes", True)
        with col2:
            x_range = st.slider("X-axis range", -20, 20, (-10, 10))
            y_range = st.slider("Y-axis range", -20, 20, (-10, 10))
        
        st.info("💡 **Teacher Tip:** Create an interactive example for students to explore")
    
    elif "GeoGebra Geometry" in tool:
        st.subheader("GeoGebra Geometry")
        st.write("Interactive geometry construction tool")
        
        html = """
        <div style="border: 3px solid #10B981; border-radius: 15px; overflow: hidden; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <iframe src="https://www.geogebra.org/geometry" 
                    width="100%" 
                    height="600px" 
                    style="border: none;">
            </iframe>
            <div style="background: linear-gradient(135deg, #10B981, #047857); color: white; padding: 15px; text-align: center;">
                <strong style="font-size: 1.2em;">GeoGebra Geometry</strong>
                <p style="margin: 5px 0 0 0; opacity: 0.9;">Construct figures, measure angles, prove theorems, transformations</p>
            </div>
        </div>
        """
        
        components.html(html, height=650)
        
        # Geometry task ideas
        with st.expander("📋 Geometry Task Ideas"):
            st.write("""
            **MYP Geometry Tasks:**
            1. **Construct** a triangle with given side lengths
            2. **Prove** that angles in a triangle sum to 180°
            3. **Explore** properties of quadrilaterals
            4. **Investigate** circle theorems interactively
            5. **Transform** shapes and analyze properties
            """)
    
    elif "Equation Editor" in tool:
        st.subheader("Math Equation Editor")
        st.write("Create beautiful mathematical equations")
        
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
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background: #f8f9fa;
                }
                
                .container {
                    max-width: 900px;
                    margin: 0 auto;
                    background: white;
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                
                .editor-container {
                    border: 2px solid #e0e0e0;
                    border-radius: 10px;
                    padding: 20px;
                    margin: 20px 0;
                    min-height: 150px;
                    font-size: 18px;
                }
                
                .button-group {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 10px;
                    margin: 20px 0;
                }
                
                .math-button {
                    padding: 10px 15px;
                    background: #4F46E5;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    font-size: 14px;
                    transition: background 0.2s;
                }
                
                .math-button:hover {
                    background: #4338CA;
                }
                
                .output {
                    background: #f3f4f6;
                    padding: 20px;
                    border-radius: 8px;
                    margin-top: 20px;
                    font-family: 'Courier New', monospace;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                }
                
                .preview {
                    background: #f8fafc;
                    padding: 20px;
                    border-radius: 8px;
                    margin-top: 20px;
                    font-size: 20px;
                    text-align: center;
                    border: 1px dashed #cbd5e1;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2 style="color: #1F2937; margin-bottom: 10px;">Math Equation Editor</h2>
                <p style="color: #6B7280; margin-bottom: 30px;">Create professional mathematical notation</p>
                
                <div class="editor-container" id="math-editor">
                    <!-- MathQuill editor will appear here -->
                </div>
                
                <div class="button-group">
                    <button class="math-button" onclick="insertFraction()">Fraction (a/b)</button>
                    <button class="math-button" onclick="insertSquareRoot()">Square Root (√)</button>
                    <button class="math-button" onclick="insertExponent()">Exponent (x²)</button>
                    <button class="math-button" onclick="insertSubscript()">Subscript (x₁)</button>
                    <button class="math-button" onclick="insertIntegral()">Integral (∫)</button>
                    <button class="math-button" onclick="insertSummation()">Summation (∑)</button>
                    <button class="math-button" onclick="insertLimit()">Limit (lim)</button>
                    <button class="math-button" onclick="insertMatrix()">Matrix</button>
                    <button class="math-button" onclick="insertGreek()">Greek Letters</button>
                    <button class="math-button" onclick="clearEditor()" style="background: #EF4444;">Clear</button>
                </div>
                
                <div>
                    <h3 style="color: #1F2937; margin-top: 30px;">LaTeX Output</h3>
                    <div class="output" id="latex-output">x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}</div>
                    
                    <div style="margin-top: 20px;">
                        <button class="math-button" onclick="copyToClipboard()" style="background: #10B981;">Copy LaTeX</button>
                        <button class="math-button" onclick="insertIntoAssessment()" style="background: #F59E0B;">Insert into Assessment</button>
                    </div>
                </div>
                
                <div>
                    <h3 style="color: #1F2937; margin-top: 30px;">Live Preview</h3>
                    <div class="preview" id="math-preview">
                        <!-- MathJax preview will appear here -->
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
                    mathField.write('\\\\begin{bmatrix}  &  \\\\\\\\  &  \\\\end{bmatrix}');
                    mathField.keystroke('Left');
                    mathField.keystroke('Left');
                    mathField.keystroke('Left');
                    mathField.keystroke('Left');
                    mathField.keystroke('Left');
                }
                
                function insertGreek() {
                    mathField.write('\\\\alpha \\\\beta \\\\gamma \\\\Delta \\\\theta \\\\pi \\\\omega');
                }
                
                function clearEditor() {
                    mathField.latex('');
                }
                
                function copyToClipboard() {
                    var latex = mathField.latex();
                    navigator.clipboard.writeText(latex).then(function() {
                        alert('LaTeX copied to clipboard!');
                    });
                }
                
                function insertIntoAssessment() {
                    // This would communicate with Streamlit
                    alert('Equation would be inserted into assessment (requires Streamlit integration)');
                }
                
                function updatePreview(latex) {
                    var preview = document.getElementById('math-preview');
                    preview.innerHTML = '\\\\( ' + latex + ' \\\\)';
                    
                    // Re-render MathJax
                    if (window.MathJax) {
                        MathJax.typesetPromise([preview]);
                    }
                }
                
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
            </script>
        </body>
        </html>
        """
        
        components.html(html, height=900)

# Add to your main app
def add_to_main_app():
    """Add math tools to your main app"""
    
    # Add a tab for math tools
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Generate", 
        "📐 Geometry", 
        "📈 Graphing", 
        "✏️ Equations", 
        "⚙️ Tools"
    ])
    
    with tab5:  # Tools tab
        math_tools_dashboard()
