import streamlit as st
from functions import displayMessage, displayWriting, sidebar, message, getQuoteAndSign, connectMedia, hideFooter, comingSoonDisplay, displayPDF, reminisceTopics, compendiaTopics, displayImg


st.set_page_config(page_title="Reminisce", page_icon="💎")
choose = sidebar()

####################################################################################################

if choose == "Home":
    titleHome, titleEnd, messageHome, messageEnd = message()
    displayMessage(titleHome, messageHome)

####################################################################################################

elif choose == "Reminisce": 
        topic = reminisceTopics()

        #Topic 1
        if topic=='Geopolitics':
            #Topic 1 Article 1         
            displayPDF("RG1", './Cover Images/LT_IranUS_compressed.jpg', './Published/LT_IranUS_compressed.pdf', 'Joe Biden and the future of Iran', 'During his campaign, President Biden expressed a desire to return to the Joint Comprehensive Plan of Action (JCPOA), also known as the Iran nuclear deal, signed in 2015 under the Obama administration...', None)

            #Topic 1 Article 2
            displayPDF("RG2", './Cover Images/LT_Armenia_compressed.jpg', './Published/LT_Armenia_compressed.pdf', 'Armenia vs Azerbaijan : The Nagorno-Karabakh conflict', 'A long-standing dispute between Armenia and Azerbaijan over the Nagorno-Karabakh region, which is internationally recognized as part of Azerbaijan but...', None)

            #Topic 1 Article 3
            displayPDF("RG3", './Cover Images/LT_Taliban_compressed.jpg', './Published/LT_Taliban_compressed.pdf', 'The rising terror of Taliban and other nations ignoring it?', 'The Taliban\'s resurgence in Afghanistan and the increase in violence and terrorism is a cause for concern for the global community. Since the US withdrawal...', None)

            #Topic 1 Article 4
            displayPDF("RG4", './Cover Images/LT_WarExtremisim_compressed.jpg', './Published/LT_WarExtremisim_compressed.pdf', 'Europe\'s War Against Radical Extremism', 'From the beheading of a school teacher in Paris followed by an attack in Nice and the same in Vienna, the whole of Europe is in shock amid...', None)

            #Topic 1 Article 5
            displayPDF("RG5", './Cover Images/LT_TalibanVsISIS_compressed.jpg', './Published/LT_TalibanVsISIS_compressed.pdf', 'Taliban\'s rivalry with ISIS is shaping Afghan peace talks', 'The ongoing rivalry between the Taliban and ISIS is playing a significant role in shaping the current Afghan peace talks. The two groups have different objectives and...', None)


            #Topic 1 Article 6
            displayPDF("RG6", './Cover Images/Boris Johnson survived the No confidence vote.jpg', './Unpublished/Boris Johnson survived the No confidence vote.pdf', 'Boris Johnsons survived the No confidence vote', 'Boris Johnson, the British Prime Minister, faced a no-confidence vote in September 2019, shortly after taking office. However, he survived the vote, which was...', 'Unpublished')

            #Topic 1 Article 7
            displayPDF("RG7", './Cover Images/Imran Khan carried out Suicide Bombings throughout Pakistan.jpg', './Unpublished/Imran Khan carried out Suicide Bombings throughout Pakistan.pdf', 'Imran Khan carried out \'Suicide Bombings\' throughout Pakistan', 'Former Pak prime minister and leader of Pakistan Muslim League-Nawaz (PML-N), Shahid Khaqan Abbasi, launched a blistering attack...', 'Unpublished')

            #Topic 1 Article 8
            displayPDF("RG8", './Cover Images/UN must ensure Human Rights in Kashmir.jpg', './Unpublished/UN must ensure Human Rights in Kashmir.pdf', 'UN must ensure \'Human Rights\' in Kashmir', 'At a joint press conference with his Pakistani counterpart Bilawal Bhutto in Islamabad on Tuesday, Baerbock assured journalists that the UN has a role to play in ensuring \'human rights\' in Kashmir...', 'Unpublished')



        #Topic 2
        elif topic=='India':
            #Topic 2 Article 1
            displayPDF("RI1", './Cover Images/LT_Covid_Havoc_compressed.jpg', './Published/LT_Covid_Havoc_compressed.pdf', 'Is PM Modi Responsible for the COVID Havoc?', 'Almost everyone in this country had seen Pictures of PM Modi addressing huge crowds who were mostly without masks or social distancing, gathered for his recent election rallies in West Bengal...', None)

            #Topic 2 Article 2
            displayPDF("RI2", './Cover Images/Dutch Minister slams Arab Nations over the controversial remarks on Prophet Mohammad.jpg', './Unpublished/Dutch Minister slams Arab Nations over the controversial remarks on Prophet Mohammad.pdf', 'Dutch Minister Slams Arab Nations Over the Controversial Remarks on Prophet Mohammad', 'The matter of the controversial statement of former BJP spokesperson Nupur Sharma on Prophet Mohammad PBUH has spread all over the world. Many Arab and Islamic countries condemned this statement...', 'Unpublished')

            #Topic 2 Article 3
            displayPDF("RI3", './Cover Images/India Qatar Relations.jpg', './Unpublished/India Qatar Relations.pdf', 'India Qatar Relations', 'The foreign ministry awared Qatar by stating "vested interests that are against India-Qatar relations have been inciting the people using these derogatory comments. We should work together against such mischievous elements who aim to undercut the strength of our bilateral ties"...', 'Unpublished')

            #Topic 2 Article 4
            displayPDF("RI4", './Cover Images/Taliban-India.jpg', './Unpublished/Taliban-India.pdf', 'The growing ties between India and The Afghanistan Taliban', 'Most decisions in international relations are for long-term gains. India may not get any benefit, but there should be no loss. It\'s because India\'s two enemies, China and Pakistan, are engaged in making their hold in Afghanistan...', 'Unpublished')



        #Topic 3
        elif topic=='History':
            #Topic 3 Article 1
            displayPDF("RH1", './Cover Images/LT_Congress_compressed.jpg', './Published/LT_Congress_compressed.pdf', 'The Fall of Indian National Congress: Then and Now', 'Indian National Congress, founded in 1885 is believed to be one of the oldest political parties in the world. An organization that has the distinction of cooperation in providing independence to India...', None)

            #Topic 3 Article 2
            displayPDF("RH2", './Cover Images/LT_Naxal_compressed.jpg', './Published/LT_Naxal_compressed.pdf', 'A Brief History of Naxalism in India', 'Charu Majumdar was not only a political leader but a great writer also. His “Historic Eight Documents” formed the basis of Naxalite ideology in India. This was a big reason that not only Rural or Tribal but Urban elites were also attracted towards this ideology...', None)

            #Topic 3 Article 3
            displayPDF("RH3", './Cover Images/Israel-Arab.jpg', './Unpublished/Israel-Arab.pdf', 'Israel & Arab: A Beginning of Normalisation of Relationship', 'One of the most protracted and bloody dispute of the post WW II Era, based on the claims of two religious communities over one piece land. The Arab-Israeli conflict is one of the major concerns in the field of security and stability in the Middle East...', 'Unpublished')



        #Topic 4
        elif topic=='Others':

            #Topic 4 Article 1
            displayPDF("RO1", './Cover Images/LT_BiharElection_compressed.jpg', './Published/LT_BiharElection_compressed.pdf', 'Bihar Assembly Elections 2020: An Analysis', 'A Full-Page advertisements in different newspapers in the mid of March 2020 caught the attention of many, with a young lady staring at readers along with the caption…CM Candidate of Bihar 2020...', None)

            #Topic 4 Article 2
            displayPDF("RO2", './Cover Images/LT_CalifornianWildfire_compressed.jpg', './Published/LT_CalifornianWildfire_compressed.pdf', 'Deadly Climatic Extremes: The Californian Wildfire', 'It\'s the changing Climate. Thousands of lightning strikes have sparked hundreds of fires across California. The average daily temperature are about 3° or 4° F warmer..', None)

            #Topic 4 Article 3
            displayPDF("RO3", './Cover Images/LT_SetuBharatam_compressed.jpg', './Published/LT_SetuBharatam_compressed.pdf', 'Setu Bharatam Project', 'The Setu Bharatam Project is a government initiative in India that aims to make all national highways free of railway crossings by the year 2024. The project was launched by Prime Minister Narendra Modi in March 2016...', None)

            #Topic 4 Certificate
            displayImg('./Cover Images/Certificate.jpg','Certificate of Appreciation', 'A Certificate of Appreciation from the co-founders and Editor-in-Chief of The LookThrou Magazine.')


####################################################################################################

elif choose == "Compendia":
    topic = compendiaTopics()
    
    #Topic 1
    if topic == "Bookisss":
        #Topic1 Book 1
        displayWriting("CB1", './Cover Images/Rashmirathi.jpg', './New/Books/Rashmirathi.html', 'Rashmirathi : Part 1', 'The first article of the series that explores the great epic **Rashmirathi** by Ramdhari Singh Dinkar, delving into its Philiterary themes, offering insights into duty, morality, and the complexities of the Mahabharata character, Karna.', None)

        comingSoonDisplay(False)

        





    
    #Topic 2
    elif topic == "Tech":

        #Topic 2 Tech 1
        feature_image1 = Image.open(r'./Cover Images/statistics.jpg')
        with st.container():
            image_col, text_col = st.columns((2,3))
            with image_col:
                st.image(feature_image1)
            with text_col:
                st.markdown(""" <style> .font {
                font-size:22px ; font-family: 'Black'; color: #FFFFF;}
                </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">The Role of Statistics in Data Science</p>', unsafe_allow_html=True)    
                st.markdown('Discover the crucial role of statistics in Data Science. Explore how statistical techniques empower data exploration, cleaning, hypothesis testing, predictive modeling, feature selection, and model evaluation.', unsafe_allow_html=True)
            if st.button("Get into it", key="mybutton"):
                showthecontent('./New/Tech/RoleofStats.html')
                st.button("Wrap it up!", help="Close it")
                

        for text in ["Did you like the article?"]:
                response = st_text_rater(text=text, key='4')
        st.write('---')

        comingSoonDisplay(False)






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

        comingSoonDisplay(False)







    
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

        comingSoonDisplay(False)
        

    
    #Topic 5
    elif topic == "BeMyGuest":

        #Topic 5 Content 1
        comingSoonDisplay(True)

####################################################################################################

elif choose == "Connect":
    titleHome, titleEnd, messageHome, messageEnd = message()
    displayMessage(titleEnd, messageEnd)
    connectMedia()

####################################################################################################

getQuoteAndSign()
hideFooter()



# st.markdown(
#     """<style>
#         .element-container:nth-of-type(n) button {
#             display: flex;
#             flex-direction: column;
#             justify-content: center;
#             align-items: center;
#             height: 30px;
#             width: 120px;
#             background-color: #f0f5f4;
#             border: none;
#             border-radius: 8px;
#             border-width: 1px;
#             border-style: solid;
#             border-color: #597a75;
#             font-size: 20px;
#             font-weight: bold;
#             color: #333333;
#             transition: all 0.2s ease-in-out;
#         }
#         .element-container:nth-of-type(n) button:hover {
#             background-color: #333333;
#             color: #f2f2f2;
#             cursor: pointer;
#         }
#         </style>""",
#     unsafe_allow_html=True,
#     )

#     st.markdown(
#     """<style>
#         .animate-charcter
#     {
#       background-image: linear-gradient(
#         -225deg,
#         #231557 0%,
#         #44107a 29%,
#         #ff1361 67%,
#         #fff800 100%
#       );
#       background-size: auto auto;
#       background-clip: border-box;
#       background-size: 200% auto;
#       color: #fff;
#       background-clip: text;
#       text-fill-color: transparent;
#       -webkit-background-clip: text;
#       -webkit-text-fill-color: transparent;
#       animation: textclip 2s linear infinite;
#       display: inline-block;
#       margin-left: 200px;
#           font-size: 50px;
#     }

#     @keyframes textclip {
#       to {
#         background-position: 200% center;
#       }
#     }
#         </style>""",
#     unsafe_allow_html=True,
#     )