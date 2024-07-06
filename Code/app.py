import streamlit as st
from functions import displayMessage, displayWriting, sidebar, message, getQuoteAndSign, connectMedia, hideFooter, comingSoonDisplay, displayPDF, reminisceTopics


st.set_page_config(page_title="Reminisce", page_icon="💎")
choose = sidebar()

###################################################################################################################

if choose == "Home":
    titleHome, titleEnd, messageHome, messageEnd = message()
    displayMessage(titleHome, messageHome)

###################################################################################################################

elif choose == "Reminisce": 
        topic = reminisceTopics()

        #Topic 1
        if topic=='Geopolitics':
            #Topic 1 Article 1

            
            displayPDF("RG1", './Cover Images/LT_IranUS_compressed.jpg', './Published/LT_IranUS_compressed.pdf', 'Joe Biden and the future of Iran', 'During his campaign, President Biden expressed a desire to return to the Joint Comprehensive Plan of Action (JCPOA), also known as the Iran nuclear deal, signed in 2015 under the Obama administration... ')



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
                    showPDF('./Published/LT_IranUS_compressed.pdf')
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
                    showPDF('./Published/LT_Armenia_compressed.pdf')
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
                    showPDF('./Published/LT_Taliban_compressed.pdf')
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
                    showPDF('./Published/LT_WarExtremisim_compressed.pdf')
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
                    showPDF('./Published/LT_TalibanVsISIS_compressed.pdf')
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
                    showPDF('./Unpublished/Boris Johnson survived the No confidence vote.pdf')
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
                    showPDF("./Unpublished/Imran Khan carried out Suicide Bombings throughout Pakistan.pdf")
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
                    showPDF("./Unpublished/UN must ensure Human Rights in Kashmir.pdf")
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
                    showPDF('./Published/LT_Covid_Havoc_compressed.pdf')
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
                    showPDF('./Unpublished/Dutch Minister slams Arab Nations over the controversial remarks on Prophet Mohammad.pdf')
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
                    showPDF('./Unpublished/India Qatar Relations.pdf')
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
                    showPDF('./Unpublished/Taliban-India.pdf')
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
                    showPDF('./Published/LT_Congress_compressed.pdf')
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
                    showPDF('./Published/LT_Naxal_compressed.pdf')
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
                    showPDF('./Unpublished/Israel-Arab.pdf')
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
                    showPDF('./Published/LT_BiharElection_compressed.pdf')
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
                    showPDF('./Published/LT_CalifornianWildfire_compressed.pdf')
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
                    showPDF('./Published/LT_SetuBharatam_compressed.pdf')
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

###################################################################################################################

elif choose == "Compendia":
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
                st.markdown('The first article of the series that explores the great epic **Rashmirathi** by Ramdhari Singh Dinkar, delving into its Philiterary themes, offering insights into duty, morality, and the complexities of the Mahabharata character, Karna.', unsafe_allow_html=True)
            if st.button("Get into it", key="mybutton"):
                showthecontent('./New/Books/Rashmirathi.html')
                st.button("Wrap it up!", help="Close it")
                

        for text in ["Did you like the article?"]:
                response = st_text_rater(text=text, key='4')
        st.write('---')

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

###################################################################################################################

elif choose == "Connect":
    titleHome, titleEnd, messageHome, messageEnd = message()
    displayMessage(titleEnd, messageEnd)
    connectMedia()

###################################################################################################################

getQuoteAndSign()
hideFooter()

