import requests
from bs4 import BeautifulSoup
import smtplib
import ssl


URL = 'https://av-info.faa.gov/OperatorsName.asp'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

target = 'Global Cross'

# Email config
port = 465  # For SSL
password = 'supersecuretest'
sender_email = "jcstestemails@gmail.com"
receiver_email = "jcrobertson26@gmail.com"
message = """
    Stock has been found!!!
"""

if target in soup:
    print('Target Sighted')
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
else:
    print('not found')
