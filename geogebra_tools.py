# geogebra_integration.py
import streamlit as st
import streamlit.components.v1 as components

def geogebra_calculator(height=500):
    """Embed GeoGebra Calculator"""
    html_code = """
    <div style="border: 2px solid #3B82F6; border-radius: 10px; overflow: hidden; margin: 20px 0;">
        <iframe src="https://www.geogebra.org/calculator" 
                width="100%" 
                height="{height}px" 
                style="border: none;">
        </iframe>
        <div style="background: #3B82F6; color: white; padding: 10px; text-align: center;">
            <strong>GeoGebra Calculator</strong> | Drag points, create graphs, explore geometry
        </div>
    </div>
    """.format(height=height)
    
    components.html(html_code, height=height+50)

def geogebra_geometry(height=500):
    """Embed GeoGebra Geometry"""
    html_code = """
    <div style="border: 2px solid #10B981; border-radius: 10px; overflow: hidden; margin: 20px 0;">
        <iframe src="https://www.geogebra.org/geometry" 
                width="100%" 
                height="{height}px" 
                style="border: none;">
        </iframe>
        <div style="background: #10B981; color: white; padding: 10px; text-align: center;">
            <strong>GeoGebra Geometry</strong> | Construct figures, measure angles, prove theorems
        </div>
    </div>
    """.format(height=height)
    
    components.html(html_code, height=height+50)

def geogebra_graphing(height=500):
    """Embed GeoGebra Graphing Calculator"""
    html_code = """
    <div style="border: 2px solid #8B5CF6; border-radius: 10px; overflow: hidden; margin: 20px 0;">
        <iframe src="https://www.geogebra.org/graphing" 
                width="100%" 
                height="{height}px" 
                style="border: none;">
        </iframe>
        <div style="background: #8B5CF6; color: white; padding: 10px; text-align: center;">
            <strong>GeoGebra Graphing</strong> | Plot functions, sliders, analyze graphs
        </div>
    </div>
    """.format(height=height)
    
    components.html(html_code, height=height+50)

def create_custom_geogebra(app_id="calculator", width="100%", height=500):
    """Create custom GeoGebra app"""
    apps = {
        "calculator": "calculator",
        "geometry": "geometry", 
        "graphing": "graphing",
        "3d": "3d",
        "cas": "cas",
        "classic": "classic"
    }
    
    if app_id not in apps:
        app_id = "calculator"
    
    html = f"""
    <iframe src="https://www.geogebra.org/{apps[app_id]}"
            width="{width}"
            height="{height}px"
            allowfullscreen
            style="border: 1px solid #e0e0e0; border-radius: 10px;">
    </iframe>
    """
    
    return html
