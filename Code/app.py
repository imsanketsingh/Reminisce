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

def showthecontent(filepath):
    with open(filepath, "r") as f:
        html_string = f.read()
    components.html(html_string, scrolling = True, height=700)



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
                showthecontent('./New/Books/Rashmirathi.html')
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
                showthecontent('./New/Philosophy/Charvaka.html')
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
                showthecontent('./New/Beyondthepages/The Pain of People.html')
                st.button("Wrap it up!", help="Close it")
                

        for text in ["Did you like the article?"]:
                response = st_text_rater(text=text, key='4')
        st.write('---')
        

    
    #Topic 5
    elif topic == "BeMyGuest":

        #Topic 5 Content 1

        st.markdown("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Coming Soon</title>
        <style>
        body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 5vh;
        margin: 0;
        }

        h4 {
        animation: fadeIn 2s;
        }

        @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
        }
        </style>
        </head>
        <body>
        <h4>Coming Soon</h4>
        </body>
        </html>
        """, unsafe_allow_html=True)















































##############################################################################################################################################################


elif choose == "Home":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p style="color: #767196; font-size: 33px; font-weight:Bold; font-style:helvetica;">About this work</p>', unsafe_allow_html=True)    
    st.markdown("""<p>
Welcome!

As a student with a passion for writing, I have been actively involved in addressing a wide range of issues such as geopolitical matters, domestic affairs, current events, and historical events. I have had the opportunity to work with various platforms, including a blogging startup called The LookThrou Magazine and a YouTube channel called Gyan Jara Hatke.

During my time at LTM, I contributed numerous articles on diverse topics, showcasing my dedication to exploring complex issues and providing thought-provoking insights. Although LTM eventually closed down, I have preserved my articles here on this website, so you can explore and engage with them.

I also briefly worked with GJH, but due to conflicting priorities with my studies, I made the tough decision to leave. However, I have unpublished articles from my time at GJH that are available for you to read on this website.

My goal with this website is to share my passion for writing, offer unique perspectives on important issues, and engage with readers like you. I hope you find my articles informative, thought-provoking, and engaging. Thank you for visiting the website and being a part of my journey so far!</p>
<p style="color: #8f8e8c; font-size: 14px; font-style:helvetica;"><i>Note: The site is still in testing phase and some Chromium browsers may block the display of the PDF in the Reminisce tab. In that case Firefox would serve the purpose and work like a charm.<br>Inconvenience caused is deeply regretted.</p>""", unsafe_allow_html=True)


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
