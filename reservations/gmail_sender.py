import os.path
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class GmailSender:
    def __init__(self, credentials_path='config/gmail_credentials.json'):
        self.scopes = ['https://www.googleapis.com/auth/gmail.send']
        self.creds = None
        
        if os.path.exists('config/gmail_token.json'):
            self.creds = Credentials.from_authorized_user_file('config/gmail_token.json', self.scopes)
        
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, self.scopes)
                self.creds = flow.run_local_server(port=0)
            
            with open('config/gmail_token.json', 'w') as token:
                token.write(self.creds.to_json())

        self.service = build('gmail', 'v1', credentials=self.creds)

    def send_mail(self, subject, content, to_email):
        try:
            message = EmailMessage()
            message.set_content(content)
            message['To'] = to_email
            message['From'] = "Samet Özalp <tecnhartstest@gmail.com>"
            message['Subject'] = subject

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            send_message = self.service.users().messages().send(
                userId="me", 
                body={'raw': encoded_message}
            ).execute()
            
            print(f"Sent mail! ID: {send_message['id']}")
        except Exception as e:
            print(f"Error: {e}")