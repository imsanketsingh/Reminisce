import streamlit as st
from  PIL import Image
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import requests
from io import BytesIO


def homePage(title, message):
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown(f'<p style="color: #767196; font-size: 33px; font-weight:Bold; font-style:helvetica;">{title}</p>', unsafe_allow_html=True)
    st.markdown(f"""{message}""", unsafe_allow_html=True)


def showthecontent(filepath):
    with open(filepath, "r") as f:
        html_string = f.read()
    components.html(html_string, scrolling = True, height = 700)


def displayWriting(uniqueKey, coverImageUrl, heading, metaDescription, contentPath):
    response = requests.get(coverImageUrl)
    image_data = BytesIO(response.content)
    learningCoverImage1 = Image.open(image_data)
    learningCoverImage1 = learningCoverImage1.resize((320, 240))
    with st.container():
        image_col, text_col = st.columns((2, 3))
        with image_col:
            st.image(learningCoverImage1)
        with text_col:
            st.markdown(""" <style> .font {
            font-size:22px ; font-family: 'Black'; color: #FFFFF;}
            </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">{heading}</p>', unsafe_allow_html=True)
            st.markdown(metaDescription, unsafe_allow_html=True)
        if st.button("Get into it", key=uniqueKey):
            showthecontent(contentPath)
            st.button("Wrap it up!", help="Close it")
    st.write('---')

def sidebar():
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .sidebar .sidebar-content:hover {
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    .option-menu li {
        border-radius: 8px;
        margin: 5px 0;
        transition: background-color 0.3s ease;
    }
    .option-menu li:hover {
        background-color: #e0e0e0;
    }
    .icon {
        color: #ff7f50 !important;
        font-size: 28px !important;
    }
    .nav-link {
        font-size: 16px !important;
        color: #333 !important;
        font-weight: bold !important;
    }
    .nav-link-selected {
        background-color: #28a745 !important;
        color: #fff !important;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)
    
    with st.sidebar:
        choose = option_menu("", ["Home", "Reminisce", "Compendia",  "Connect"],
                         icons=['house', 'bookmarks-fill','file-text', 'person lines fill'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#24A608"},
    }
    ) 
    return choose


def message():
    return 'About this work', """<p>
Welcome!

As a student with a passion for writing, I have been actively involved in addressing a wide range of issues such as geopolitical matters, domestic affairs, current events, and historical events. I have had the opportunity to work with various platforms, including a blogging startup called The LookThrou Magazine and a YouTube channel called Gyan Jara Hatke.

During my time at LTM, I contributed numerous articles on diverse topics, showcasing my dedication to exploring complex issues and providing thought-provoking insights. Although LTM eventually closed down, I have preserved my articles here on this website, so you can explore and engage with them.

I also briefly worked with GJH, but due to conflicting priorities with my studies, I made the tough decision to leave. However, I have unpublished articles from my time at GJH that are available for you to read on this website.

My goal with this website is to share my passion for writing, offer unique perspectives on important issues, and engage with readers like you. I hope you find my articles informative, thought-provoking, and engaging. Thank you for visiting the website and being a part of my journey so far!</p>
<p style="color: #8f8e8c; font-size: 14px; font-style:helvetica;"><i>Note: The site is still in testing phase and some Chromium browsers may block the display of the PDF in the Reminisce tab. In that case Firefox would serve the purpose and work like a charm.<br>Inconvenience caused is deeply regretted.</p>"""