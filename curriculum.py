# curriculum.py - MYP Mathematics Curriculum Database

MYP_CURRICULUM = {
    "MYP 1-3": {
        "Numerical and abstract reasoning": {
            "Number": [
                "Number operations (addition, subtraction, multiplication, division)",
                "Integers, fractions, decimals, percentages",
                "Estimation and rounding",
                "Number lines and simple inequalities",
                "Factors and multiples",
                "Prime numbers",
                "Squares and square roots"
            ],
            "Algebra": [
                "Find and verify rules for sequences",
                "Forming simple equations",
                "Substitution into expressions",
                "Expanding brackets",
                "Factorizing algebraic expressions",
                "Solving linear equations"
            ]
        },
        "Thinking with models": {
            "Functions": [
                "Linear functions f(x) = mx + c",
                "Domain and Range",
                "Function notation",
                "Mapping diagrams"
            ]
        },
        "Spatial reasoning": {
            "Geometry": [
                "Classifying shapes and angles",
                "Perimeter and area of 2D shapes",
                "Volume of 3D shapes",
                "Coordinates and plotting points",
                "Symmetry and reflection",
                "Angles in parallel lines"
            ],
            "Trigonometry": [
                "Triangle properties",
                "Pythagoras' theorem"
            ]
        },
        "Reasoning with data": {
            "Statistics": [
                "Data collection methods",
                "Bar charts, pie charts, pictograms",
                "Mean, median, mode",
                "Range as measure of dispersion"
            ],
            "Probability": [
                "Probability of simple events",
                "Probability scale (0 to 1)",
                "Sample spaces",
                "Theoretical vs experimental probability"
            ]
        }
    },
    "MYP 4-5 (standard)": {
        "Numerical and abstract reasoning": {
            "Number": [
                "Surds and radicals",
                "Logarithms and their laws",
                "Laws of exponents (integer, negative, fractional)",
                "Standard form (scientific notation)",
                "Recurring decimals",
                "Absolute values",
                "Lower and upper bounds"
            ],
            "Algebra": [
                "Solving quadratic equations (factorization, formula)",
                "Simultaneous equations",
                "Inequalities (including compound)",
                "Rearranging formulae",
                "Arithmetic and geometric sequences"
            ]
        },
        "Thinking with models": {
            "Functions": [
                "Quadratic functions",
                "Exponential functions",
                "Rational functions",
                "Transformations of functions",
                "Systems of equations graphically"
            ]
        },
        "Spatial reasoning": {
            "Geometry": [
                "Circle theorems",
                "Similarity and congruence",
                "Coordinate geometry (distance, midpoint, gradient)",
                "Volume and surface area of complex shapes",
                "Trigonometry in 3D"
            ],
            "Trigonometry": [
                "Sine rule and cosine rule",
                "Trigonometric ratios in right triangles",
                "Bearings"
            ]
        },
        "Reasoning with data": {
            "Statistics": [
                "Histograms for continuous data",
                "Box-and-whisker plots",
                "Scatter graphs and correlation",
                "Lines of best fit",
                "Standard deviation",
                "Cumulative frequency"
            ],
            "Probability": [
                "Probability calculations with Venn diagrams",
                "Tree diagrams",
                "Conditional probability",
                "Dependent and independent events"
            ]
        }
    },
    "MYP 4-5 (extended)": {
        "Numerical and abstract reasoning": {
            "Number": [
                "Rationalizing denominators",
                "Number bases",
                "Complex numbers (introductory)",
                "Sigma notation",
                "Convergence and divergence"
            ],
            "Algebra": [
                "Exponential equations",
                "Summation of sequences",
                "Polynomial functions",
                "Systems of non-linear equations",
                "Proof by induction (introductory)"
            ]
        },
        "Thinking with models": {
            "Functions": [
                "Logarithmic functions",
                "Trigonometric functions",
                "Composite functions",
                "Inverse functions",
                "Transformations of all function types"
            ]
        },
        "Spatial reasoning": {
            "Geometry": [
                "Vector notation and operations",
                "Polar coordinates",
                "3D coordinate geometry",
                "Fractals (informal)",
                "Radians and circular measure"
            ],
            "Trigonometry": [
                "Unit circle",
                "Trigonometric identities",
                "Radians",
                "Graphs of trigonometric functions"
            ]
        },
        "Reasoning with data": {
            "Statistics": [
                "Normal distribution",
                "Confidence intervals",
                "Regression analysis",
                "Hypothesis testing",
                "Chi-square tests"
            ],
            "Probability": [
                "Permutations and combinations",
                "Binomial distribution",
                "Normal distribution probability",
                "Expected value"
            ]
        }
    }
}

CRITERION_STRANDS = {
    "Criterion A: Knowing and understanding": {
        "i": "Select appropriate mathematics when solving problems in both familiar and unfamiliar situations",
        "ii": "Apply the selected mathematics successfully when solving problems",
        "iii": "Solve problems correctly in both familiar and unfamiliar situations"
    },
    "Criterion B: Investigating patterns": {
        "i": "Select and apply appropriate problem-solving strategies to recognize patterns",
        "ii": "Describe patterns as relationships or general rules consistent with findings",
        "iii": "Test and verify these rules",
        "iv": "Prove or justify and test the validity of their generalizations"
    },
    "Criterion C: Communicating": {
        "i": "Use appropriate mathematical language (notation, symbols, terminology)",
        "ii": "Use appropriate forms of mathematical representation",
        "iii": "Move between different forms of mathematical representation",
        "iv": "Communicate complete, coherent and concise mathematical lines of reasoning"
    },
    "Criterion D: Applying mathematics in real-life contexts": {
        "i": "Identify relevant elements of authentic real-life situations",
        "ii": "Select appropriate mathematical strategies when solving authentic real-life situations",
        "iii": "Apply the selected mathematical strategies successfully to reach a solution",
        "iv": "Justify the degree of accuracy of a solution",
        "v": "Justify whether a solution makes sense in the context of the authentic real-life situation"
    }
}

GLOBAL_CONTEXTS = [
    "Identities and relationships",
    "Orientation in space and time", 
    "Personal and cultural expression",
    "Scientific and technical innovation",
    "Globalization and sustainability",
    "Fairness and development"
]

KEY_CONCEPTS = [
    "Relationships", "Logic", "Change", "Systems", 
    "Patterns", "Form", "Function", "Creativity", "Culture"
]

COMMAND_TERMS = {
    "Describe": "Give a detailed account or picture of a situation, event, pattern or process.",
    "Explain": "Give a detailed account including reasons or causes.",
    "Investigate": "Observe, study, or make a detailed and systematic examination, in order to establish facts and reach new conclusions.",
    "Justify": "Give valid reasons or evidence to support an answer or conclusion.",
    "Verify": "Provide evidence that validates the result.",
    "Calculate": "Obtain a numerical answer showing the relevant stages in the working.",
    "Solve": "Obtain the answer(s) using algebraic and/or numerical and/or graphical methods.",
    "Sketch": "Represent by means of a diagram or graph (labelled as appropriate).",
    "Graph": "Represent by means of a graph.",
    "Find": "Obtain an answer showing relevant stages in the working.",
    "Show that": "Obtain the required result (possibly using information given) without the formality of proof.",
    "Determine": "Obtain the only possible answer.",
    "Prove": "Use a sequence of logical steps to obtain the required result in a formal way.",
    "Demonstrate": "Make clear by reasoning or evidence, illustrating with examples or practical application.",
    "Interpret": "Use knowledge and understanding to recognize trends and draw conclusions from given information.",
    "Analyze": "Interpret data to reach conclusions."
}
