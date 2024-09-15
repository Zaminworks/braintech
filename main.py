import streamlit as st
from datetime import datetime

# Function to get the current date, time, and year
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%d %B %Y, %H:%M:%S")

# Set up the main page layout
st.set_page_config(page_title="BrainTech Tools", layout="wide")

# Header with navbar
st.markdown(
    """
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            background-color: red;
        }
        .navbar h1 {
            margin: 0;
            font-size: 24px;
        }
        .footer {
            text-align: center;
            padding: 10px;
            background-color: red;
            position: absolute;
            bottom: 0;
            width: 100%;
        }
        .footer p {
            margin: 0;
            font-size: 14px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Navbar
st.markdown(
    """
    <div class="navbar">
        <h1>BrainTech</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Main content
st.title("Welcome to BrainTech Tools")

# Tool links with images
tools = [
    {"name": "Blog Title Generator", "file": "blog_title_generator_app.py", "image": "https://img.icons8.com/?size=50&id=31449&format=png"},
    {"name": "Blog Writer", "file": "blog_tool.py", "image": "https://img.icons8.com/?size=80&id=Ay9Ejs4KE0Vg&format=png"},
    {"name": "Tags Generator", "file": "tags_generator_app.py", "image": "https://img.icons8.com/?size=64&id=49483&format=png"},
    {"name": "Hashtags Generator", "file": "hashtags_generator.py", "image": "https://img.icons8.com/?size=80&id=Uv9gzShnRlY4&format=png"},
    {"name": "YouTube Video Script Generator", "file": "youtube_script_generator_app.py", "image": "https://img.icons8.com/?size=80&id=68707&format=png"},
    {"name": "YouTube Video Description Writer", "file": "youtube_description_generator_app.py", "image": "https://img.icons8.com/?size=64&id=QuEM7y66zzw4&format=png"},
]

# Display tool links with images
for tool in tools:
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <img src="{tool['image']}" alt="{tool['name']}" style="width: 100px; height: auto; margin-right: 20px;">
            <a href="{tool['file']}" target="_blank" style="font-size: 20px; text-decoration: none; color: white;">{tool['name']}</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
st.title("")

# Footer with current date, time, and copyright text
st.markdown(
    f"""
    <div class="footer">
        <p>{get_current_datetime()}</p>
        <p>All Rights Reserved By BrainTech | Zamin Raza</p>
    </div>
    """,
    unsafe_allow_html=True
)
