import requests

import smtplib 

from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/TCL-138-71-inches-55P65US-2019-Built/dp/B07SBB3K61/ref=sr_1_1_sspa?crid=OHILRWTGU8TE&keywords=55+inch+smart+tv&qid=1574259900&sprefix=55+in%2Caps%2C276&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRVRMOFAzRVFPMEFPJmVuY3J5cHRlZElkPUEwMTA1OTI2MTlBVFM1QldUWTRJRiZlbmNyeXB0ZWRBZElkPUEwOTk4MzEyMzhXVE9EMk5RNFA3UiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def get_product():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productName = soup.find(id ="productTitle").get_text()

    productPrice = soup.find(id = "priceblock_ourprice").get_text()

    floatPrice = productPrice[0:8]

    if(floatPrice == 33,999 ):
        send_email()

    print("PRODUCT NAME:" +  productName.strip())
    print("PRODUCT PRICE:" + floatPrice.strip())


def send_email():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vignesh6901@gmail.com', 'bzdxbrpiysrdvskh')

    subject = 'The prices are down and you can buy it now!!!!'
    body = 'Check the amazon link below \n https://www.amazon.in/TCL-138-71-inches-55P65US-2019-Built/dp/B07SBB3K61/ref=sr_1_1_sspa?crid=OHILRWTGU8TE&keywords=55+inch+smart+tv&qid=1574259900&sprefix=55+in%2Caps%2C276&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRVRMOFAzRVFPMEFPJmVuY3J5cHRlZElkPUEwMTA1OTI2MTlBVFM1QldUWTRJRiZlbmNyeXB0ZWRBZElkPUEwOTk4MzEyMzhXVE9EMk5RNFA3UiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    
    message = f"subject: {subject}\n\n{body}"

    server.sendmail('vignesh6901@gmail.com', 'vignesh6901@gmail.com' , message)
    print('the mail has been sent')

    server.quit() 

get_product()
