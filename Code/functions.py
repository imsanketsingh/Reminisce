import streamlit as st
from  PIL import Image
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import requests
from io import BytesIO
from streamlit_lottie import st_lottie
import json
import random
import base64
from streamlit_text_rating.st_text_rater import st_text_rater
import threading
import time
from dbMain import database

session_state = st.session_state.get('session_state', {})

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def lottieWork():
    lottie_hello = load_lottiefile("Code/lottieHi.json")

    st_lottie(
        lottie_hello,
        speed=1,
        loop=False,
        reverse=False,
        quality="high",
        height=70,
        width=300,
        key=None,
    )


def displayMessage(title, message):
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        
        st.markdown(f'<div style="text-align: center; position: relative; bottom: 10px; width: 100%;"> <span style="color: #046764; font-size: 33px; font-weight:Bold; font-style:helvetica;text-decoration: underline;">{title}</span> </div>', unsafe_allow_html=True)
    st.markdown(f"""{message}""", unsafe_allow_html=True)


def showthecontent(filepath):
    with open(filepath, "r") as f:
        html_string = f.read()
    components.html(html_string, scrolling = True, height = 700)


def displayWriting(uniqueKey, coverImageUrl, contentPath, heading, metaDescription, caption):
    coverImage = Image.open(coverImageUrl)
    coverImage = coverImage.resize((320, 240))
    with st.container():
        image_col, text_col = st.columns((2, 3))
        with image_col:
            st.image(coverImage)
        with text_col:
            st.markdown(""" <style> .font {
            font-size:22px ; font-family: 'Black'; color: #FFFFF;}
            </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">{heading}</p>', unsafe_allow_html=True)
            st.markdown(metaDescription, unsafe_allow_html=True)
        if st.button("Get into it", key=str(uniqueKey)+'1'):
            showthecontent(contentPath)
            st.button("Wrap it up!", help="Close it")

    textRator(uniqueKey, heading)
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
        lottieWork()
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
    return 'About this work', 'You are awesome', """<p>
Welcome!

As a student with a passion for writing, I have been actively involved in addressing a wide range of issues such as geopolitical matters, domestic affairs, current events, and historical events. I have had the opportunity to work with various platforms, including a blogging startup called The LookThrou Magazine and a YouTube channel called Gyan Jara Hatke.

During my time at LTM, I contributed numerous articles on diverse topics, showcasing my dedication to exploring complex issues and providing thought-provoking insights. Although LTM eventually closed down, I have preserved my articles here on this website, so you can explore and engage with them.

I also briefly worked with GJH, but due to conflicting priorities with my studies, I made the tough decision to leave. However, I have unpublished articles from my time at GJH that are available for you to read on this website.

My goal with this website is to share my passion for writing, offer unique perspectives on important issues, and engage with readers like you. I hope you find my articles informative, thought-provoking, and engaging. Thank you for visiting the website and being a part of my journey so far!</p>
<p style="color: #8f8e8c; font-size: 14px; font-style:helvetica;"><i>Note: The site is still in testing phase and some Chromium browsers may block the display of the PDF in the Reminisce tab. In that case Firefox would serve the purpose and work like a charm.<br>Inconvenience caused is deeply regretted.</p>""","""<p>
Thank you for visiting here and exploring my articles on geopolitics, domestic news, and historical events. As a writer, It's always my aim to offer thoughtful, informative, and nuanced perspectives on these complex issues.

While my writing focuses on specific topics and events, I believe that philosophical reflections can add depth and insight to any subject matter. Philosophy can help us ask critical questions, challenge and broaden our perspectives. For instance, when we analyze geopolitics, we can ask questions such as: What are the underlying values, interests, and power dynamics that shape international relations? Similarly, when we examine domestic news, we can ask questions such as: What are the ethical and political implications of current events and policies? How can we foster solidarity across diverse perspectives and interests? Finally, when we study historical events, we can ask questions such as: What are the root causes and consequences of historical conflicts? How can we learn from past mistakes and achievements to shape a better future? By asking these and other philosophical questions, we can deepen our understanding of the complex, dynamic, and interconnected nature of our world.

Finally, If you would like to connect with me further, I invite you to check me on various platforms. Thank you for your interest and engagement with my writing.</p>"""



def getQuoteAndSign():
    all_possible_categories = ['age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday', 'business', 'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation', 'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'men', 'mom', 'money', 'morning', 'movies', 'success']  #length= 67

    index = random.randint(0,(len(all_possible_categories)-1))
    category = all_possible_categories[index]
    # print(index, ": ", category)
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': st.secrets["QUOTES_API_KEY"]})
    if response.status_code == requests.codes.ok:
        st.sidebar.markdown("<p style='font-style: italic;'>{}</p>".format(response.json()[0]['quote']), unsafe_allow_html=True)
        st.sidebar.markdown("<p style='font-style: italic; text-align: right; margin-right: 2rem;'>{}</p>".format("- "+ response.json()[0]['author']), unsafe_allow_html=True)
    else:
        print("Error:", response.status_code, response.text)

    st.sidebar.markdown("""
<div style='text-align: center; position: relative; bottom: 0px; width: 100%;'>
    <span style='color: #04376e; font-family: Helvetica; font-weight: bold;'>Made with ✨ by Sanket</span>
</div>
""", unsafe_allow_html=True)
    
def userMessage():
        #     st.markdown(
    # """<style>
    #     .element-container:nth-of-type(n) button {
    #         display: flex;
    #         flex-direction: column;
    #         justify-content: center;
    #         align-items: center;
    #         height: 30px;
    #         width: 120px;
    #         background-color: #f0f5f4;
    #         border: none;
    #         border-radius: 8px;
    #         border-width: 1px;
    #         border-style: solid;
    #         border-color: #597a75;
    #         font-size: 20px;
    #         font-weight: bold;
    #         color: #333333;
    #         transition: all 0.2s ease-in-out;
    #     }
    #     .element-container:nth-of-type(n) button:hover {
    #         background-color: #333333;
    #         color: #f2f2f2;
    #         cursor: pointer;
    #     }
    #     </style>""",
    # unsafe_allow_html=True,
    # )
    #     message = st.text_area("Type your message here (Kindly mention topic name)")
    #     if st.button("Send"):
    #         if(message==""):
    #             st.write("Can't send empty message")
    #         else:
    #             details(message)
    #             st.write("Message sent successfully!")
    pass



def connectMedia():
    st.markdown("")

    css = """
            .navigation-button {
                display: inline-block;
                background-color: #f4f4f4;
                color: #000000;
                font-size: 10px;
                text-align: center;
                text-decoration: none;
                border-radius: 10px;
                padding: 8px 25px;
                margin: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
                transition: all 0.3s ease-in-out;
            }

            .navigation-button:hover {
                transform: translateY(-5px);
                box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.3);
                text-decoration: none;
            }

            .navigation-button img {
                vertical-align: middle;
                margin-right: 10px;
            }
        """

    st.write(f"<style>{css}</style>", unsafe_allow_html=True)
        
    github_button = """
            <a href="https://github.com/imsanketsingh" target="_blank" class="navigation-button">
                <img src="https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_960_720.png" alt="GitHub logo" width="20" height="20">
                GitHub
            </a>
        """

    linkedin_button = """
            <a href="https://www.linkedin.com/in/imsanketsingh/" target="_blank" class="navigation-button">
                <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-512.png" alt="LinkedIn logo" width="20" height="20">
                LinkedIn
            </a>
        """

    medium_button = """
            <a href="https://medium.com/@imsanketsingh" target="_blank" class="navigation-button">
                <img src="https://avatars.githubusercontent.com/u/923954?s=200&v=4" alt="Medium logo" width="20" height="20">
                Medium
            </a>
        """
    

    col1, col2, col3 = st.columns(3)

    with col1:
            st.markdown(github_button, unsafe_allow_html=True)

    with col2:
            st.markdown(linkedin_button, unsafe_allow_html=True)

    with col3:
            st.markdown(medium_button, unsafe_allow_html=True)

    st.write("___")


@st.cache_data
def hideFooter():
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)


@st.cache_data
def comingSoonDisplay(isEmpty):
    html_code = """"."""
    if(isEmpty):
        html_code = """
                    <style>
                        .coming-soon {
                            font-family: Arial, sans-serif;
                            font-size: 2rem;
                            font-weight: bold;
                            text-align: center;
                            animation: colorChange 3s infinite alternate;
                        }

                        @keyframes colorChange {
                            0% { color: red; }
                            25% { color: yellow; }
                            50% { color: grey; }
                            75% { color: orange; }
                            100% { color: purple; }
                        }
                    </style>

                    <div class="coming-soon">Coming Soon</div>
                """
    else:
        html_code = """
                    <style>
                        .coming-soon {
                            font-family: Arial, sans-serif;
                            font-size: 2rem;
                            font-weight: bold;
                            text-align: center;
                            animation: colorChange 3s infinite alternate;
                        }

                        @keyframes colorChange {
                            0% { color: red; }
                            25% { color: yellow; }
                            50% { color: grey; }
                            75% { color: orange; }
                            100% { color: purple; }
                        }
                    </style>

                    <div class="coming-soon">More Articles Coming Soon</div>
                """
    

    st.markdown(html_code, unsafe_allow_html=True)




def showPDF(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def displayImg(featureImagePath, title, metaDescription):
    feature_image = Image.open(featureImagePath)
    with st.container():
        image_col, text_col = st.columns((2, 3))
        with image_col:
            st.image(feature_image)
        with text_col:
            st.markdown(""" <style> .font {
            font-size:22px ; font-family: 'Black'; color: #FFFFF;}
            </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">{title}</p>', unsafe_allow_html=True)
            st.markdown(f'{metaDescription}', unsafe_allow_html=True)

def displayPDF(uniqueKey, featureImagePath, contentPath, title, metaDescription, caption):
    feature_image = Image.open(featureImagePath)
    with st.container():
        image_col, text_col = st.columns((2, 3))
        with image_col:
            st.image(feature_image, caption= caption)
        with text_col:
            st.markdown(""" <style> .font {
            font-size:22px ; font-family: 'Black'; color: #FFFFF;}
            </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">{title}</p>', unsafe_allow_html=True)
            st.markdown(f'{metaDescription}<b>[Read More👇]</b>', unsafe_allow_html=True)

    col1, col2,col3= st.columns(3)
    with col1:  
        if st.button('Open Article',key = str(uniqueKey)+'1'):            
            showPDF(contentPath)
    with col2:
        st.button('Close Article',key= str(uniqueKey)+'2')             
    with col3:
        with open(contentPath, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download PDF Article", key= str(uniqueKey)+'3',
                data=PDFbyte,
                file_name= str(title)+".pdf",
                mime='application/octet-stream')

    textRator(uniqueKey, title)
    st.write('---')


def textRator(uniqueKey, articleName):
    key = f"{uniqueKey}_rating"
    
    # Display text rating component
    response = st_text_rater(text="Did you like the article?", key=str(uniqueKey)+'4')
    
    # Handle response from text rater
    if response in ['liked', 'disliked']:
        session_state[key] = not session_state.get(key, False)
        
        # Deactivate all other keys if this key is activated
        for k in session_state:
            if k != key:
                session_state[k] = False
                
        # Example database function call with rating parameter
        countFromDB = database(articleName, response == 'liked')
        
        # Display feedback based on database response
        if countFromDB[2]:
            if response == 'liked':
                st.balloons()
                st.markdown(f"Thank you🖤, Now _{articleName}_ has _{countFromDB[0]}_ likes and _{countFromDB[1]}_ dislikes.")
            else:
                st.markdown(f"Thank you, Now _{articleName}_ has _{countFromDB[0]}_ likes and _{countFromDB[1]}_ dislikes.")
        else:
            if response == 'liked':
                st.markdown(f"_Database hourly limit exceeded, this like won't be counted_")
            else:
                st.markdown(f"_Database hourly limit exceeded, this dislike won't be counted_")






def reminisceTopics():
    return option_menu(None, ["Geopolitics", "India", "History", "Others"],
                         icons=['book', 'book','book','book'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#080000"},
        },orientation='horizontal'
        ) 

def compendiaTopics():
    return option_menu(None, ["Books", "Tech", "Philosophy", "BeyondThePages", "Special"],
                         icons=['book', 'laptop','lightning','journal-plus'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "10!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "10px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"15px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#080000"},
        },orientation='horizontal'
        )

def specialSubtopics():
    return option_menu(None, ["Climate", "Guests"],
            icons=['shield-shaded', 'person-fill'],
            menu_icon="list", default_index=0,
            styles={
                "container": {"background-color": "#f0f0f0", "border-radius": "8px", "width" : "80%"},
                "icon": {"color": "#FF5733", "font-size": "14px", },
                "nav": {"width" : "90"},
                "nav-link": {"font-size": "16px", "text-align": "left", "border-radius": "6px", "transition": "background-color 0.3s ease", "color": "#eee", "background-color": "#1a4513"},
                "nav-link-selected": {"background-color": "#0b2907", "color": "#fff"},
                "nav-link:hover": {"background-color": "#FFC300", "color": "#fff"}
            },
            orientation='horizontal'
            )