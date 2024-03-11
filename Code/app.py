import streamlit as st
from streamlit_option_menu import option_menu
from  PIL import Image
import numpy as np
import pandas as pd
import base64
import requests
from streamlit_text_rating.st_text_rater import st_text_rater
import streamlit.components.v1 as components
import random
from streamlit_lottie import st_lottie 
import json
from emailit import secretdetails

st.set_page_config(page_title="Reminisce", page_icon="💎")





##########################################################################################################################################################

with st.sidebar:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_7psw7qge.json")

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
    
################################################################COMPENDIA######################################################################################

def showthecontent(filepath, height):
    with open(filepath, "r") as f:
        html_string = f.read()
    components.html(html_string, height=height)



if choose == "Compendia":
    topic = option_menu(None, ["Books", "Tech", "Philosophy", "BeyondThePages", "BeMyGuest"],
                         icons=['book', 'laptop','lightning','journal-plus'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "10!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "10px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"15px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#080000"},
        },orientation='horizontal'
        )
    st.markdown(
    """<style>
        .element-container:nth-of-type(n) button {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 30px;
            width: 120px;
            background-color: #f0f5f4;
            border: none;
            border-radius: 8px;
            border-width: 1px;
            border-style: solid;
            border-color: #597a75;
            font-size: 20px;
            font-weight: bold;
            color: #333333;
            transition: all 0.2s ease-in-out;
        }
        .element-container:nth-of-type(n) button:hover {
            background-color: #333333;
            color: #f2f2f2;
            cursor: pointer;
        }
        </style>""",
    unsafe_allow_html=True,
    )

    st.markdown(
    """<style>
        .animate-charcter
    {
      background-image: linear-gradient(
        -225deg,
        #231557 0%,
        #44107a 29%,
        #ff1361 67%,
        #fff800 100%
      );
      background-size: auto auto;
      background-clip: border-box;
      background-size: 200% auto;
      color: #fff;
      background-clip: text;
      text-fill-color: transparent;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: textclip 2s linear infinite;
      display: inline-block;
      margin-left: 200px;
          font-size: 50px;
    }

    @keyframes textclip {
      to {
        background-position: 200% center;
      }
    }
        </style>""",
    unsafe_allow_html=True,
    )

    

    
    st.write('\n')


    #Topic 1
    if topic == "Books":

        #Topic1 Book1
        feature_image1 = Image.open(r'./Cover Images/Rashmirathi.jpg')
        with st.container():
            image_col, text_col = st.columns((2,3))
            with image_col:
                st.image(feature_image1)
            with text_col:
                st.markdown(""" <style> .font {
                font-size:22px ; font-family: 'Black'; color: #FFFFF;}
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">Rashmirathi : Part 1</p>', unsafe_allow_html=True)    
                st.markdown('This is the first article of the series "Rashmirathi" that explores the great epic "Rashmirathi" by Ramdhari Singh Dinkar, delving into its philosophical and literary themes, offering insights into duty, morality, and the complexities of the Mahabharata character, Karna.', unsafe_allow_html=True)
            if st.button("Get into it", key="mybutton"):
                showthecontent('./New/Books/Rashmirathi.html', 4960)
                st.button("Wrap it up!", help="Close it")
                

        for text in ["Did you like the article?"]:
                response = st_text_rater(text=text, key='4')
        st.write('---')







    
    #Topic 2
    elif topic == "Tech":

        #Topic 2 Tech 1
        st.markdown('<div class="container"> <div class="row"> <div class="col-md-12 text-center"> <h4 class="animate-charcter"> Coming Soon </h4> </div> </div> </div>', unsafe_allow_html=True)












    #Topic 3
    elif topic == "Philosophy":

        #Topic 3 Philosophy 1
        feature_image1 = Image.open(r'./Cover Images/Charvakas.jpg')
        with st.container():
            image_col, text_col = st.columns((2,3))
            with image_col:
                st.image(feature_image1)
            with text_col:
                st.markdown(""" <style> .font {
                font-size:22px ; font-family: 'Black'; color: #FFFFF;}
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">The Charvaka Philosophy</p>', unsafe_allow_html=True)    
                st.markdown('This article explores the philosophy of Charvaka, an ancient Indian school of thought. The article provides an overview of the Charvaka worldview, including their beliefs about the nature of reality, consciousness, and ethics.', unsafe_allow_html=True)
            if st.button("Get into it", key="mybutton"):
                showthecontent('./New/Philosophy/Charvaka.html', 7180)
                st.button("Wrap it up!", help="Close it")
                

        for text in ["Did you like the article?"]:
                response = st_text_rater(text=text, key='4')
        st.write('---')







    
    #Topic 4
    elif topic == "BeyondThePages":

        #Topic 4 Content 1
        feature_image1 = Image.open(r'./Cover Images/painofpeople.jpg')
        with st.container():
            image_col, text_col = st.columns((2,3))
            with image_col:
                st.image(feature_image1)
            with text_col:
                st.markdown(""" <style> .font {
                font-size:22px ; font-family: 'Black'; color: #FFFFF;}
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">The Pain of People</p>', unsafe_allow_html=True)    
                st.markdown('Pain is a prevalent issue that can affect people from all walks of life. Acknowledging the pain of others is essential for building empathy and understanding, as it helps us to connect with others on a deeper level.', unsafe_allow_html=True)
            if st.button("Get into it", key="mybutton"):
                showthecontent('./New/Beyondthepages/The Pain of People.html', 3533)
                st.button("Wrap it up!", help="Close it")
                

        for text in ["Did you like the article?"]:
                response = st_text_rater(text=text, key='4')
        st.write('---')
        

    
    #Topic 5
    elif topic == "BeMyGuest":

        #Topic 5 Content 1
        st.markdown('<div class="container"> <div class="row"> <div class="col-md-12 text-center"> <h4 class="animate-charcter"> Coming Soon </h4> </div> </div> </div>', unsafe_allow_html=True)













































##############################################################################################################################################################


elif choose == "Home":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p style="color: #767196; font-size: 33px; font-weight:Bold; font-style:helvetica;">About this work</p>', unsafe_allow_html=True)    
    st.markdown("""<p style="margin: 0cm 0cm 8pt; font-size: 11pt; font-family: Calibri, sans-serif; text-align: center;"><strong><u><span style="font-size: 26px; color: rgb(184, 49, 47); font-family: Georgia, serif;">About Rashmirathi</span></u></strong></p>
<p style="margin: 0cm 0cm 8pt; font-size: 11pt; font-family: Calibri, sans-serif; text-align: center;"><br></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><strong><span style="font-size: 16px;">Rashmirathi</span></strong></span><span style="font-size: 16px; font-family: Georgia, serif;">, whose literal meaning is <em>&ldquo;The Suns charioteer&rdquo;</em>, is an epic that retells the story of <strong>Karna</strong>, a significant character from the Indian epic, the Mahabharata.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">The poem primarily revolves around the life of Karna, who is known as <em>Surya-Putra</em> (The son of the Sun god, Surya). It explorers Karna&rsquo;s character, his struggles and his tragic destiny.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Dinkar presents Karna as a noble and tragic hero who faces numerous challenges and ethical dilemmas. &nbsp;The poem delves into Karna&rsquo;s loyalty, sense of honor, and his unwavering commitment to his principles.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Rashmirathi is not just a narration but also contains profound philosophical reflections on life, duty and destiny. Dinkar weaves philosophical elements in to the storyline, offering readers a deeper understanding of the human condition.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Dinkar&rsquo;s poetic style in Rashmirathi is marked by its rich language and powerful versus. It creates a captivating and emotionally charge narrative of Karna&rsquo;s complex and pivotal character in Mahabharata.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">At its essence, Rashmirathi acknowledges the recognition of high qualities in an individual. It emphasizes that the true recognition of an individual&rsquo;s elevated virtues can only be attained through one&rsquo;s actions and conduct.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Rashmirathi is not only a poetry exploration of mythical character&rsquo;s life, but also a work that addresses universal themes and resonates with readers for its literary and philosophical depth. The poem&rsquo;s impact extends beyond literature, influencing discussions on morality, duty, and human values.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;">&nbsp;</span></p>
<p style="margin: 0cm 0cm 8pt; font-size: 11pt; font-family: Calibri, sans-serif; text-align: center;"><span style="font-family: Georgia, serif;"><strong><u><span style="font-size: 26px; color: rgb(184, 49, 47);">A Beacon of Social Transformation in a Caste-Entrenched Society</span></u></strong></span></p>
<p style="margin: 0cm 0cm 8pt; font-size: 11pt; font-family: Calibri, sans-serif; text-align: center;"><br></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><strong><span style="font-size: 16px;">Rashmirathi</span></strong></span><span style="font-size: 16px; font-family: Georgia, serif;">&nbsp;gains increased relevance when viewed in the historical context of a society deeply entrenched in casteism. During the time when caste divisions were prevalent in Indian society, and people&apos;s lives were profoundly influenced by caste considerations, Dinkar&apos;s epic takes on a transformative role. The poem goes beyond the traditional boundaries set by caste and encourages a broader understanding of human values and character.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Despite being from an upper caste himself, Dinkar&apos;s work reflects a progressive and inclusive vision. He uses the character of Karna, who is traditionally considered to be from a lower caste, to challenge the rigid caste structures and prejudices. Karna&apos;s struggle and virtues, as portrayed in Rashmirathi, become a metaphor of breaking free from the shackles of caste-based discrimination.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Dinkar, through his poetry, motivates Indians to transcend the darkness of ignorance associated with casteism. He emphasizes the importance of recognizing individuals based on their merits, actions, and character rather than their caste background. The epic serves as a powerful call for unity, equality, and a collective rise above the divisive barriers of caste.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Rashmirathi becomes a literary tool to inspire social change, encouraging people to question and challenge the prevailing caste norms and prejudices. Dinkar&apos;s message resonates with a timeless appeal for a more inclusive and egalitarian society, urging individuals to rise above the limitations imposed by caste distinctions and focus on the shared humanity that binds them together.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><br></span></p>
<p style="margin: 0cm 0cm 8pt; font-size: 11pt; font-family: Calibri, sans-serif; text-align: center;"><span style="font-family: Georgia, serif;"><strong><u><span style="font-size: 26px; color: rgb(184, 49, 47);">About Ramdhari Singh Dinkar</span></u></strong></span></p>
<p style="margin: 0cm 0cm 8pt; font-size: 11pt; font-family: Calibri, sans-serif; text-align: center;"><br></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Ramdhari Singh Dinkar, 23 Sept. 1908 - 24 Apr 1974, was an influential poet, essayist, and academic. He is considered one of the great Hindi poets of all time.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Dinkar was born in Simaria, a small village at the shore of the river Ganga in Bihar. He had the alma mater of the Patna University.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Dinkar&rsquo;s poetry is known for its powerful and evocative verses. His works include not only poetry but also essays, plays, and critiques. Some of his notable works include <em>Rashmirathi, Urvashi, Sanskriti Ke Chaar Adhyay</em>. He was honoured with the Sahitya Akademy Award in 1959 for his work <em>Sanskriti Ke Chaar Adhyay</em>. He also received the Padma Bhushan, India&apos;s third highest civilian award in 1959.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Ramdhari Singh Dinkar&rsquo;s legacy continues through his literary contributions, which have left a lasting impact on Hindi literature. His poems are still recited and admired and he is remembered as a poet who brought a unique blend of intellectual depth and emotional intensity to his work.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><br></span></p>
<p style="margin: 0cm 0cm 8pt; font-size: 11pt; font-family: Calibri, sans-serif; text-align: center;"><span style="font-family: Georgia, serif;"><strong><u><span style="font-size: 26px; color: rgb(184, 49, 47);">A Little Background on Mahabharata</span></u></strong></span></p>
<p style="margin: 0cm 0cm 8pt; font-size: 11pt; font-family: Calibri, sans-serif; text-align: center;"><br></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">The Mahabharata is one of the two major Sanskrit epics of ancient India, the other being the Ramayana. Attributed to the sage Vyasa, the Mahabharata is a colossal epic that consists of over 100,000 slokas (verses), and is divided into 18 sections.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">The Mahabharata primarily revolves around the conflict between two groups of cousins, the <strong>Pandavas</strong> and the <strong>Kauravas</strong>. The central theme is the Kurukshetra was a great battle between these two factions.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><br></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><strong><u><span style="font-size: 20px; color: rgb(40, 50, 78);">Background</span></u></strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">King <strong>Shantanu</strong> of Kuru dynasty and the ruler of Hastinapur marries the river goddess Ganga, who gives birth to <strong>Devavrata</strong>. After several tragic events, including the death of Shantanu&apos;s 7 children and the departure of Ganga, Shantanu wanted to marry Satyavati, whose father demanded that she will marry the king Shantanu only when the king promises to pass on the throne to Satyavati&rsquo;s child that would be born after the marriage and then the lineage should pass on accordingly. But according to tradition, the throne must be passed to the eldest son if he is capable of ruling the empire and then the lineage should continue passing on.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">King Shantanu refused this demand as he already had made his son Devavrata the prince of Hastinapura. But when Devavrata got to know about this from other sources that his father is sacrificing the wish to marry Satyavati, he went to Satyavati&apos;s father and took an oath known as the <strong>Bhishma Pratigya</strong> (Bhishma&apos;s vow). He vowed lifelong celibacy i.e. Brahmacharya, never to marry or have children and relinquished the right to the throne for the sake of his father&apos;s happiness and the stability of kingdom.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">This selfless vow earned him the name Bhishma which means formidable. Bhishma&apos;s vow, while ensuring the stability of throne also set the stage for the complex events leading to the great holy war at Kurukshetra where Krishna would recite the Gita and Karna would sacrifice his life in the battlefield.&nbsp;</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><br></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><strong><u><span style="font-size: 20px; color: rgb(40, 50, 78);">The Lineage</span></u></strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">The lineage of rulers in <strong>Aryavrata</strong> (Indian subcontinent), as per the Mahabharata, begins with King <strong>Bharata</strong>, through which the country of India gets her name <strong>Bharat</strong>.&nbsp;</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">This is the list of rulers from King Bharata onwards.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>1. Bharata:&nbsp;</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:36.0pt;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Bharata was the son of King Dushyant and Queen Shakuntala. Here, an important thing that should not get unnoticed is that Shakuntala is the daughter of sage Vishwamitra and Menaka an apsara. Now, a great link between Ramayana and Mahabharata can be seen here. Vishwamitra is the same sage who had brought Rama and Lakshmana to the forest in order to kill the demons who disturbed the holy rituals.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>2. Bhumanyu:</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:36.0pt;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Bharata was succeeded by Bhumanyu. Bhumanyu was not the son of Bharata. He was a young deserving warrior, whom Bharata appointed to be the king, since the king deemed his son unfit to rule the country.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>3.&nbsp;</strong><strong>Suhotra</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>4. Hasti:</strong> The founder of Hastinapur, the capital of dynasty</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>5.&nbsp;</strong><strong>Ajamidha</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>6. Ruru</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>7. Sunaka</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>8. Kritirata</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>9. Maharoma</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>10. Sudhriti</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>11. Ganda</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>12. Sarvabhauma</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>13. Jayatsena</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>14. Ratthavarman</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>15. Divodasa</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>16. Pratardana</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>17. Vrihadrathi</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>18. Yudhajit</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>19. Kuru:&nbsp;</strong>The founder of the Kuru dynasty</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>20. Shantanu</strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><br></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">After King Shantanu, the lineage of rulers in Hastinapur continued with his descendants.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>Chitrangada</strong>, the elder son of Shantanu, succeeded him as the ruler of Hastinapur. However, he died young and had no heirs. With the death of Chitrangada, Shantanu&apos;s next son, <strong>Vichitravirya</strong>, ascended the throne. Vichitravirya married <strong>Ambika</strong> and <strong>Ambalika</strong>, but he also died without producing an heir. Now, as Vichitravirya had no heirs, Bhishma sought the help of sage Vyasadeva, who performed a special ritual to impregnate the queens, Ambika and Ambalika. During that ritual, some misfortunes happened, leading to Ambika giving birth to <strong>Dhritarashtra</strong>, who was blind from birth, and Ambalika giving birth to <strong>Pandu</strong>, who had health issues.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Dhritarashtra was the elder one, but since he was blind, Pandu was crowned as the king of Hastinapur. However, due to the curse of sage Kindama, Pandu was unable to father child naturally. His queens, <strong>Kunti</strong> and Madri, bore children through divine boons.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Dhritarashtra&apos;s sons were Kauravas <em>(including Duryodhana, the main antagonist in Mahabharata, and 99 other sons)</em>, while Pandu&apos;s sons were the Pandavas <em>(Yudhishthira, Bhima, Arjuna, Nakula and Sahadeva)</em>.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Pandu&apos;s reign took a tragic turn when he faced an untimely death. Consequently, Dhritarashtra, despite of being blind, was crowned as the king of Hastinapur.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">The Mahabharata epic narrates the conflicts and events that unfolded between the Kauravas and Pandavas, leading to the great Kurukshetra war. The Kurukshetra war was a major conflict that took place between the Kauravas and the Pandavas, with <strong>Lord Krishna</strong> serving as the charioteer for Arjuna. The war resulted in the destruction of Kauravas and Pandavas emerged victorious.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><br></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><strong><u><span style="font-size: 20px; color: rgb(40, 50, 78);">About Karna</span></u></strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Kunti, the princess of Kunti kingdom, who later became the wife of Pandu, was given a special boon by the sage Durvasa during her premarital life. This boon granted her the ability to invoke any deity and have children by then. Curious about the power of boon, Kunti tested it and invoked the sun god, Surya. Karna is the son of Kunti and Surya and hence called <strong>Surya-Putra</strong> <em>(The son of Surya)</em>.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Faced with the challenges of being an unwed mother, Kunti decided to place Karna in a basket and set him afloat on the river Ganga. The infant Karna was discovered and adopted by Adhiratha, a charioteer, and his wife Radha. Later on, Karna was also being known as <strong>Radhey&nbsp;</strong><em>(The son of Radha)</em>.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Karna, unaware of his royal lineage, grew up as the son of a charioteer. Despite facing societal prejudices due to his humble upbringing, Karna displayed exceptional skills and earned respect for his virtues and talents. Duryodhana, recognizing Karna&apos;s prowess, befriended him, offering him the throne of Anga Kingdom. Karna, grateful for the friendship and recognition denied by others, pledged his unwavering loyalty to Duryodhana.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Despite knowing his true lineage lately (That too from Kunti herself), and the opportunity to side with his half-brothers, the Pandavas, Karna chooses to fight for Duryodhana in the Kurukshetra war. His loyalty to his friend and his sense of duty prevails over familial bonds.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">Karna&apos;s tragic fate becomes a symbol of consequences of societal vices and a poignant reflection on loyalty, identity, and destiny. Gradually and subtly, Rashmirathi brings Karma&apos;s fate into revelation.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;">&nbsp;</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><strong><u><span style="font-size: 20px; color: rgb(40, 50, 78);">The Righteous Struggle</span></u></strong></span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">In the context of Dharma, the Pandavas are often considered to represent righteousness. They faced numerous injustices, including the infamous game of dice in which they lost their kingdom, their exile in the forest, and various attempts on their lives. Lord Krishna served as a guide and advisor to the Pandavas.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">On the other hand, the Kauravas, particularly led by Duryodhana, engaged in deceitful tactics and unfair strategies. The Kauravas&apos; refusal to return the Pandavas their rightful share of the kingdom after their exile in the forest for 13 years, and their role in plotting against them, contribute to the growing animosity between the two factions.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;"><strong>Cheerharan</strong>, that has a literal meaning of disrobing, is a significant episode in Mahabharata where Draupadi, the wife of Pandavas, is humiliated and nearly disrobed by Dushasana, a Kaurava, in the Kauravas&apos; court during the game of dice (Pasha). This degrading incident highlights the erosion of righteousness and becomes a turning point in the epic, leading to the eventual Kurukshetra war. Lord Krishna intervenes to protect Draupadi and guide the Pandavas through their trials.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-size: 16px; font-family: Georgia, serif;">&nbsp;</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;'><span style="font-family: Georgia, serif;"><strong><u><span style="font-size: 20px; color: rgb(40, 50, 78);">Important Characters</span></u></strong></span></p>
<div style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom: 0cm;">
        <li style="margin: 0cm 0cm 8pt; font-size: 16px; font-family: Georgia, serif;"><strong>Dronacharya:</strong></li>
    </ul>
</div>
<ul style="margin-left: 72px ;">
    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; font-size: 16px; font-family: Georgia, serif; text-align: justify;">Dronacharya was the royal teacher (guru) of Kuru princes, including the Pandavas and the Kauravas. Arjuna, one of the Pandavas&apos; brothers, was Dronacharya&apos;s most notable pupil. He played a pivotal role in Kurukshetra war. Despite being a virtuous and skilled teacher, he fought on the side of Kauravas due to his loyalty to Hastinapur.</li>
</ul>
<div style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom: 0cm;">
        <li style="margin: 0cm 0cm 8pt; font-size: 16px; font-family: Georgia, serif;"><strong>Kripacharya</strong></li>
    </ul>
</div>
<ul style="margin-left: 72px ;">
    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; font-size: 16px; font-family: Georgia, serif; text-align: justify;">Kripacharya, like Dronacharya, was an accomplished warrior and teacher. He was known for his expertise in various weapons and combat skills. Kripacharya was especially close to Kauravas, being their martial teacher and advisor.</li>
</ul>
<div style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom: 0cm;">
        <li style="margin: 0cm 0cm 8pt; font-size: 16px; font-family: Georgia, serif;"><strong>Krishna</strong></li>
    </ul>
</div>
<ul style="margin-left: 72px ;">
    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; font-size: 16px; font-family: Georgia, serif; text-align: justify;">The eighth avatar of Lord Vishnu and central character in the Mahabharata, Krishna serves as the charioteer and advisor to Arjuna during the Kurukshetra war. He delivers the <strong>Bhagavad Gita</strong>, a discourse on duty and spirituality, addressing Arjuna&apos;s moral dilemmas that comes at the holy land of Kurukshetra when he realizes that he has to kill all of his cousins, teachers, grandparents, uncles, relatives for the throne of Hastinapur. Krishna, also plays a key role in diplomatic efforts trying to prevent the war, and his divine nature is revealed throughout the epic.</li>
</ul>
<div style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom: 0cm;">
        <li style="margin: 0cm 0cm 8pt; font-size: 16px; font-family: Georgia, serif;"><strong>Gandhari</strong></li>
    </ul>
</div>
<ul style="margin-left: 72px ;">
    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; font-size: 16px; font-family: Georgia, serif; text-align: justify;">The wife of Dhritarashtra and the mother of Kauravas, she voluntarily blindfolds herself throughout her married life to share in her husband&apos;s blindness.</li>
</ul>
<div style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom: 0cm;">
        <li style="margin: 0cm 0cm 8pt; font-size: 16px; font-family: Georgia, serif;"><strong>Shakuni</strong></li>
    </ul>
</div>
<ul style="margin-left: 72px ;">
    <li style="margin-top: 0cm; margin-right: 0cm; margin-bottom: 8pt; font-size: 16px; font-family: Georgia, serif; text-align: justify;">The maternal uncle of Kauravas and the master manipulator, he is the brother of Gandhari and he came along with her to Hastinapur after the marriage of her sister. Shakuni is often portrayed as the instigator of the conflict between the Kauravas and the Pandavas.</li>
</ul>""", unsafe_allow_html=True)


###############################################################################################################################################################

elif choose == "Reminisce": 
        topic = option_menu(None, ["Geopolitics", "India", "History", "Others"],
                         icons=['book', 'book','book','book'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#080000"},
        },orientation='horizontal'
        ) 


######################################################DISPLAYING THE PDF#######################################################################################

        def show_pdf(file_path):
            with open(file_path,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
        

###############################################################################################################################################################

        st.write('\n')
        #Topic 1
        if topic=='Geopolitics':
            #Topic 1 Article 1
            feature_image1 = Image.open(r'./Cover Images/LT_IranUS_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Joe Biden and the future of Iran</p>', unsafe_allow_html=True)    
                    st.markdown('During his campaign, President Biden expressed a desire to return to the Joint Comprehensive Plan of Action (JCPOA), also known as the Iran nuclear deal, signed in 2015 under the Obama administration... <b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='1'):            
                    show_pdf('./Published/LT_IranUS_compressed.pdf')
            with col2:
                st.button('Close Article',key='2')             
            with col3:
                with open("./Published/LT_IranUS_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='3',
                        data=PDFbyte,
                        file_name="Joe Biden and the future of Iran.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='4')

            st.write('---')

            #Topic 1 Article 2
            feature_image1 = Image.open(r'./Cover Images/LT_Armenia_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Armenia vs Azerbaijan : The Nagorno-Karabakh conflict</p>', unsafe_allow_html=True)    
                    st.markdown('A long-standing dispute between Armenia and Azerbaijan over the Nagorno-Karabakh region, which is internationally recognized as part of Azerbaijan but...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='5'):            
                    show_pdf('./Published/LT_Armenia_compressed.pdf')
            with col2:
                st.button('Close Article',key='6')             
            with col3:
                with open("./Published/LT_Armenia_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='7',
                        data=PDFbyte,
                        file_name="Armenia vs Azerbaijan : The Nagorno-Karabakh conflict.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='8')

            st.write('---')

            #Topic 1 Article 3
            feature_image1 = Image.open(r'./Cover Images/LT_Taliban_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">The rising terror of Taliban and other nations ignoring it?</p>', unsafe_allow_html=True)    
                    st.markdown("The Taliban's resurgence in Afghanistan and the increase in violence and terrorism is a cause for concern for the global community. Since the US withdrawal...<b>[Read More👇]</b>", unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='9'):            
                    show_pdf('./Published/LT_Taliban_compressed.pdf')
            with col2:
                st.button('Close Article',key='10')             
            with col3:
                with open("./Published/LT_Taliban_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='11',
                        data=PDFbyte,
                        file_name="The rising terror of Taliban and other nations ignoring it?.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='12')

            st.write('---')

            #Topic 1 Article 4
            feature_image1 = Image.open(r'./Cover Images/LT_WarExtremisim_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown("<p class='font'>Europe's War Against Radical Extremism</p>", unsafe_allow_html=True)    
                    st.markdown("From the beheading of a school teacher in Paris followed by an attack in Nice and the same in Vienna, the whole of Europe is in shock amid...<b>[Read More👇]</b>", unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='13'):            
                    show_pdf('./Published/LT_WarExtremisim_compressed.pdf')
            with col2:
                st.button('Close Article',key='14')             
            with col3:
                with open("./Published/LT_WarExtremisim_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='15',
                        data=PDFbyte,
                        file_name="Europe's War Against Radical Extremism.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='16')

            st.write('---')

            #Topic 1 Article 5
            feature_image1 = Image.open(r'./Cover Images/LT_TalibanVsISIS_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown("<p class='font'>Taliban's rivalry with ISIS is shaping Afghan peace talks</p>", unsafe_allow_html=True)    
                    st.markdown("The ongoing rivalry between the Taliban and ISIS is playing a significant role in shaping the current Afghan peace talks. The two groups have different objectives and...<b>[Read More👇]</b>", unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='17'):            
                    show_pdf('./Published/LT_TalibanVsISIS_compressed.pdf')
            with col2:
                st.button('Close Article',key='18')             
            with col3:
                with open("./Published/LT_TalibanVsISIS_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='19',
                        data=PDFbyte,
                        file_name="Taliban's rivalry with ISIS is shaping Afghan peace talks.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='20')

            st.write('---')


            #Topic 1 Article 6
            feature_image1 = Image.open(r'./Cover Images/Boris Johnson survived the No confidence vote.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1, caption='Unpublished')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown("<p class='font'>Boris Johnsons survived the No confidence vote</p>", unsafe_allow_html=True)    
                    st.markdown("Boris Johnson, the British Prime Minister, faced a no-confidence vote in September 2019, shortly after taking office. However, he survived the vote, which was...<b>[Read More👇]</b>", unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='21'):            
                    show_pdf('./Unpublished/Boris Johnson survived the No confidence vote.pdf')
            with col2:
                st.button('Close Article',key='22')             
            with col3:
                with open("./Unpublished/Boris Johnson survived the No confidence vote.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='23',
                        data=PDFbyte,
                        file_name="Boris Johnson survived the No confidence vote.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='24')

            st.write('---')


            #Topic 1 Article 7
            feature_image1 = Image.open(r'./Cover Images/Imran Khan carried out Suicide Bombings throughout Pakistan.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1, caption='Unpublished')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown("<p class='font'>Imran Khan carried out 'Suicide Bombings' throughout Pakistan</p>", unsafe_allow_html=True)    
                    st.markdown("Former Pak prime minister and leader of Pakistan Muslim League-Nawaz (PML-N), Shahid Khaqan Abbasi, launched a blistering attack...<b>[Read More👇]</b>", unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='25'):            
                    show_pdf("./Unpublished/Imran Khan carried out Suicide Bombings throughout Pakistan.pdf")
            with col2:
                st.button('Close Article',key='26')             
            with col3:
                with open("./Unpublished/Imran Khan carried out Suicide Bombings throughout Pakistan.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='27',
                        data=PDFbyte,
                        file_name="Imran Khan carried out Suicide Bombings throughout Pakistan.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='28')

            st.write('---')

            #Topic 1 Article 8
            feature_image1 = Image.open(r'./Cover Images/UN must ensure Human Rights in Kashmir.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1, caption='Unpublished')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown("<p class='font'>UN must ensure 'Human Rights' in Kashmir</p>", unsafe_allow_html=True)    
                    st.markdown("At a joint press conference with his Pakistani counterpart Bilawal Bhutto in Islamabad on Tuesday, Baerbock assured journalists that the UN has a role to play in ensuring 'human rights' in Kashmir...<b>[Read More👇]</b>", unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='29'):            
                    show_pdf("./Unpublished/UN must ensure Human Rights in Kashmir.pdf")
            with col2:
                st.button('Close Article',key='30')             
            with col3:
                with open("./Unpublished/UN must ensure Human Rights in Kashmir.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='31',
                        data=PDFbyte,
                        file_name="UN must ensure Human Rights in Kashmir.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='32')

            st.write('---')


        #Topic 2
        elif topic=='India':
            #Topic 2 Article 1
            feature_image1 = Image.open(r'./Cover Images/LT_Covid_Havoc_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Is PM Modi Responsible for the COVID Havoc?</p>', unsafe_allow_html=True)    
                    st.markdown('Almost everyone in this country had seen Pictures of PM Modi addressing huge crowds who were mostly without masks or social distancing, gathered for his recent election rallies in West Bengal...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='1'):            
                    show_pdf('./Published/LT_Covid_Havoc_compressed.pdf')
            with col2:
                st.button('Close Article',key='2')             
            with col3:
                with open("./Published/LT_Covid_Havoc_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='3',
                        data=PDFbyte,
                        file_name="Is PM Modi Responsible for the COVID Havoc?.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='4')

            st.write('---')


            #Topic 2 Article 2
            feature_image1 = Image.open(r'./Cover Images/Dutch Minister slams Arab Nations over the controversial remarks on Prophet Mohammad.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1, caption='Unpublished')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Dutch Minister Slams Arab Nations Over the Controversial Remarks on Prophet Mohammad</p>', unsafe_allow_html=True)    
                    st.markdown('The matter of the controversial statement of former BJP spokesperson Nupur Sharma on Prophet Mohammad PBUH has spread all over the world. Many Arab and Islamic countries condemned this statement...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='5'):            
                    show_pdf('./Unpublished/Dutch Minister slams Arab Nations over the controversial remarks on Prophet Mohammad.pdf')
            with col2:
                st.button('Close Article',key='6')             
            with col3:
                with open("./Unpublished/Dutch Minister slams Arab Nations over the controversial remarks on Prophet Mohammad.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='7',
                        data=PDFbyte,
                        file_name="Dutch Minister Slams Arab Nations Over Controversial Remarks on Prophet Mohammad.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='8')

            st.write('---')

            #Topic 2 Article 3
            feature_image1 = Image.open(r'./Cover Images/India Qatar Relations.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1, caption='Unpublished')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">India Qatar Relations</p>', unsafe_allow_html=True)    
                    st.markdown('The foreign ministry awared Qatar by stating "vested interests that are against India-Qatar relations have been inciting the people using these derogatory comments. We should work together against such mischievous elements who aim to undercut the strength of our bilateral ties"...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='9'):            
                    show_pdf('./Unpublished/India Qatar Relations.pdf')
            with col2:
                st.button('Close Article',key='10')             
            with col3:
                with open("./Unpublished/India Qatar Relations.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='11',
                        data=PDFbyte,
                        file_name="India Qatar Relations.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='12')

            st.write('---')

            #Topic 2 Article 4
            feature_image1 = Image.open(r'./Cover Images/Taliban-India.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1, caption='Unpublished')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">The growing ties between India and The Afghanistan Taliban</p>', unsafe_allow_html=True)    
                    st.markdown("Most decisions in international relations are for long-term gains. India may not get any benefit, but there should be no loss. It's because India's two enemies, China and Pakistan, are engaged in making their hold in Afghanistan...<b>[Read More👇]</b>", unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='13'):            
                    show_pdf('./Unpublished/Taliban-India.pdf')
            with col2:
                st.button('Close Article',key='14')             
            with col3:
                with open("./Unpublished/Taliban-India.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='15',
                        data=PDFbyte,
                        file_name="The growing ties between India and The Afghanistan Taliban.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='16')

            st.write('---')
        

        #Topic 3
        elif topic=='History':
            #Topic 3 Article 1
            feature_image1 = Image.open(r'./Cover Images/LT_Congress_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">The Fall of Indian National Congress: Then and Now</p>', unsafe_allow_html=True)    
                    st.markdown('Indian National Congress, founded in 1885 is believed to be one of the oldest political parties in the world. An organization that has the distinction of cooperation in providing independence to India...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='1'):            
                    show_pdf('./Published/LT_Congress_compressed.pdf')
            with col2:
                st.button('Close Article',key='2')             
            with col3:
                with open("./Published/LT_Congress_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='3',
                        data=PDFbyte,
                        file_name="The Fall of Indian National Congress: Then and Now.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='4')

            st.write('---')

            #Topic 3 Article 2
            feature_image1 = Image.open(r'./Cover Images/LT_Naxal_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">A Brief History of Naxalism in India</p>', unsafe_allow_html=True)    
                    st.markdown('Charu Majumdar was not only a political leader but a great writer also. His “Historic Eight Documents” formed the basis of Naxalite ideology in India. This was a big reason that not only Rural or Tribal but Urban elites were also attracted towards this ideology...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='5'):            
                    show_pdf('./Published/LT_Naxal_compressed.pdf')
            with col2:
                st.button('Close Article',key='6')             
            with col3:
                with open("./Published/LT_Naxal_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='7',
                        data=PDFbyte,
                        file_name="A Brief History of Naxalism in India.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='8')

            st.write('---')


            #Topic 3 Article 3
            feature_image1 = Image.open(r'./Cover Images/Israel-Arab.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1, caption='Unpublished')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Israel & Arab: A Beginning of Normalisation of Relationship</p>', unsafe_allow_html=True)    
                    st.markdown('One of the most protracted and bloody dispute of the post WW II Era, based on the claims of two religious communities over one piece land. The Arab-Israeli conflict is one of the major concerns in the field of security and stability in the Middle East...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='9'):            
                    show_pdf('./Unpublished/Israel-Arab.pdf')
            with col2:
                st.button('Close Article',key='10')             
            with col3:
                with open("./Unpublished/Israel-Arab.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='11',
                        data=PDFbyte,
                        file_name="Israel & Arab: A Beginning of Normalisation of Relationship.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='12')

            st.write('---')



        #Topic 4
        elif topic=='Others':

            #Topic 4 Article 1
            feature_image1 = Image.open(r'./Cover Images/Certificate.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1, caption="Certificate")
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Certificate of Appreciation</p>', unsafe_allow_html=True)    
                    st.markdown('A Certificate of Appreciation from the co-founders and Editor-in-Chief of The LookThrou Magazine.', unsafe_allow_html=True)          

            st.write('---')
            
            #Topic 4 Article 2
            feature_image1 = Image.open(r'./Cover Images/LT_BiharElection_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Bihar Assembly Elections 2020: An Analysis</p>', unsafe_allow_html=True)    
                    st.markdown('A Full-Page advertisements in different newspapers in the mid of March 2020 caught the attention of many, with a young lady staring at readers along with the caption…CM Candidate of Bihar 2020...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='3'):            
                    show_pdf('./Published/LT_BiharElection_compressed.pdf')
            with col2:
                st.button('Close Article',key='4')             
            with col3:
                with open("./Published/LT_BiharElection_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='5',
                        data=PDFbyte,
                        file_name="Bihar Assembly Elections 2020: An Analysis.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='6')

            st.write('---')

            #Topic 4 Article 3
            feature_image1 = Image.open(r'./Cover Images/LT_CalifornianWildfire_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Deadly Climatic Extremes: The Californian Wildfire</p>', unsafe_allow_html=True)    
                    st.markdown('It’s the changing Climate. Thousands of lightning strikes have sparked hundreds of fires across California. The average daily temperature are about 3° or 4° F warmer..<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='7'):            
                    show_pdf('./Published/LT_CalifornianWildfire_compressed.pdf')
            with col2:
                st.button('Close Article',key='8')             
            with col3:
                with open("./Published/LT_CalifornianWildfire_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='9',
                        data=PDFbyte,
                        file_name="Deadly Climatic Extremes: The Californian Wildfire.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='10')

            st.write('---')


            #Topic 4 Article 4
            feature_image1 = Image.open(r'./Cover Images/LT_SetuBharatam_compressed.jpg')
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Setu Bharatam Project</p>', unsafe_allow_html=True)    
                    st.markdown('The Setu Bharatam Project is a government initiative in India that aims to make all national highways free of railway crossings by the year 2024. The project was launched by Prime Minister Narendra Modi in March 2016...<b>[Read More👇]</b>', unsafe_allow_html=True)

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Open Article',key='11'):            
                    show_pdf('./Published/LT_SetuBharatam_compressed.pdf')
            with col2:
                st.button('Close Article',key='12')             
            with col3:
                with open("./Published/LT_SetuBharatam_compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Article", key='13',
                        data=PDFbyte,
                        file_name="Setu Bharatam Project.pdf",
                        mime='application/octet-stream')

            for text in ["Did you like the article?"]:
                    response = st_text_rater(text=text, key='14')

            st.write('---')



elif choose == "Connect": 
        st.markdown("""
        <div style='text-align: center; position: relative; bottom: 10px; width: 100%;'>
        <span style='color: #046764; font-family: cursive; font-weight: bold;font-size:20px; text-decoration: underline;'>You are awesome</span>
        </div>
""", unsafe_allow_html=True)
        
        st.markdown("""<p>
Thank you for visiting here and exploring my articles on geopolitics, domestic news, and historical events. As a writer, It's always my aim to offer thoughtful, informative, and nuanced perspectives on these complex issues.

While my writing focuses on specific topics and events, I believe that philosophical reflections can add depth and insight to any subject matter. Philosophy can help us ask critical questions, challenge and broaden our perspectives. For instance, when we analyze geopolitics, we can ask questions such as: What are the underlying values, interests, and power dynamics that shape international relations? Similarly, when we examine domestic news, we can ask questions such as: What are the ethical and political implications of current events and policies? How can we foster solidarity across diverse perspectives and interests? Finally, when we study historical events, we can ask questions such as: What are the root causes and consequences of historical conflicts? How can we learn from past mistakes and achievements to shape a better future? By asking these and other philosophical questions, we can deepen our understanding of the complex, dynamic, and interconnected nature of our world.

Finally, If you would like to connect with me further, I invite you to check me on various platforms. If you have any feedbacks, questions, or suggestions, you can <b>use the message box below</b> to send me a message 😇. I value your input and would love to hear from you.

Once again, thank you for your interest and engagement with my writing.</p>""", unsafe_allow_html=True)


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

        instagram_button = """
            <a href="https://instagram.com/imsanketsingh" target="_blank" class="navigation-button">
                <img src="https://raw.githubusercontent.com/github/explore/06c46459e7947c8a25f72798af696d66e202ac39/topics/instagram/instagram.png" alt="Instagram logo" width="20" height="20">
                Instagram
            </a>
        """

        medium_button = """
            <a href="https://medium.com/@imsanketsingh" target="_blank" class="navigation-button">
                <img src="https://avatars.githubusercontent.com/u/923954?s=200&v=4" alt="Medium logo" width="20" height="20">
                Medium
            </a>
        """
    

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(github_button, unsafe_allow_html=True)

        with col2:
            st.markdown(linkedin_button, unsafe_allow_html=True)

        with col3:
            st.markdown(instagram_button, unsafe_allow_html=True)

        with col4:
            st.markdown(medium_button, unsafe_allow_html=True)

        st.write("___")

        st.markdown(
    """<style>
        .element-container:nth-of-type(n) button {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 30px;
            width: 120px;
            background-color: #f0f5f4;
            border: none;
            border-radius: 8px;
            border-width: 1px;
            border-style: solid;
            border-color: #597a75;
            font-size: 20px;
            font-weight: bold;
            color: #333333;
            transition: all 0.2s ease-in-out;
        }
        .element-container:nth-of-type(n) button:hover {
            background-color: #333333;
            color: #f2f2f2;
            cursor: pointer;
        }
        </style>""",
    unsafe_allow_html=True,
    )
        message = st.text_area("Type your message here (Kindly mention topic name)")
        if st.button("Send"):
            if(message==""):
                st.write("Can't send empty message")
            else:
                secretdetails(message)
                st.write("Message sent successfully!")

##############################################################################QUOTES###############################################################################


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

###################################################################################################################################################################


hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


###################################################################################################################################################################
