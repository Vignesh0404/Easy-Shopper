from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:/Users/k9Iyappan/Downloads/chromedriver_win32/chromedriver.exe")

brands=[]
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
url="https://www.flipkart.com/mens-clothing/tshirts/pr?sid=2oq%2Cs9b%2Cj9y&otracker=nmenu_sub_Men_0_T-Shirts&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DADIDAS&page="
#url="https://www.flipkart.com/men/tshirts/pr?sid=2oq%2Cs9b%2Cj9y&page="
for i in range(1,30):
    driver.get(url+str(i))
    content = driver.page_source
    soup = BeautifulSoup(content,'html.parser')

    pagenum = soup.find_all('div',attrs={'class':'_2zg3yZ'})
    print(pagenum)

#print(pagenum.string)

    for a in soup.find_all('div', attrs={'class': '_2LFGJH'}):
        brand = a.find('div', attrs={'class':'_2B_pmu'})
        name = a.find('a', attrs={'class':'_2mylT6'})   #name works
        price = a.find('div', attrs={'class':'_1vC4OE'})
        print(brand.string)
        brands.append(brand.string)
        products.append(name.string)
        prices.append(price.string)

df = pd.DataFrame({'Brand Name':brands,'Product Name':products,'Price':prices})
df.to_csv(r'D:\Swaran\products.csv', index=False, encoding='utf-8')