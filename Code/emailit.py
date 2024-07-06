import requests
import streamlit as st

class details:
    def __init__(self, message):
        self.sendmail(message)
    
    def sendmail(self, message):
        api_key = st.secrets["Email_API_KEY"]
        api_url = st.secrets["Email_API_URL"]

        data = {
            'sender': {
                'name': 'Reminisce',
                'email': st.secrets["Email_sender"]
            },
            'to': [
                {
                    'email': st.secrets["Email_reciever"]
                }
            ],
            'subject': st.secrets["Email_subject"],
            'htmlContent': f'{message}'
        }

        headers = {
            'Content-Type': 'application/json',
            'api-key': api_key
        }
        print(data)
        response = requests.post(api_url, headers=headers, json=data)

        # Checking if email was successfully sent
        if response.status_code == 201:
            print('OTP sent successfully')
        else:
            print(f'Failed to send email: {response.content}')

        