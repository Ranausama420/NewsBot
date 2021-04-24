import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome('C://Users//Rana Usama//Downloads//chromedriver_win32 (7)//chromedriver.exe')
start_time=time.time()

def getGrouptitle():
    driver.get('https://web.whatsapp.com/')
    wait = WebDriverWait(driver, 600)

    target = '"Group Title"'
    # x_arg = '//span[contains(@title,' + target + ')]'
    # group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    # group_title.click()
    time.sleep(25)
    name = 'Gears'
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()


#//*[@id="main"]/footer/div[1]/div[2]/div/div[2]
def sendMessage(head,p1,p2,p3,l):
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    message.send_keys(head)
    message.send_keys(Keys.SHIFT, '\n \n')
    message.send_keys(p1)
    message.send_keys(Keys.SHIFT, '\n \n')
    message.send_keys(p2)
    # message.send_keys(Keys.SHIFT, '\n \n')
    # message.send_keys(p3)
    message.send_keys(Keys.SHIFT, '\n \n')
    message.send_keys(l)
    # //*[@id="main"]/footer/div[1]/div[3]/button
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()


getGrouptitle()

#type test.txt | shuffle.bat > tst_temp.txt
f=open("tst_temp.txt","r")
links=f.readlines()
for link in links:
    l=link.rstrip('\n')
    parsed_uri = urlparse(l)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    if result == "https://www.reuters.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        heading = soup.find('h1')
        paras = soup.find_all('p')
        head="*"+heading.text+"*"
        p1=paras[3].text
        p2=paras[4].text
        p3=paras[3].text
        sendMessage(head,p1,p2,p3,l)
    elif result == "https://www.dawn.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('a', attrs={'class':'story__link'})
        paras = soup.find_all('p')
        head = "*" + h.text.rstrip("\n") + "*"
        if paras[0].text == " ":
            p1 = paras[1].text
            p2 = paras[2].text
            p3 = paras[3].text
        else:
            p1 = paras[0].text
            p2 = paras[1].text
            p3 = paras[2].text

        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.thenews.com.pk/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        head = "*" + h.text.rstrip() + "*"
        p1 = paras[3].text
        p2 = paras[4].text
        p3 = paras[4].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.aljazeera.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        head = "*" + h.text.rstrip() + "*"
        p1 = paras[1].text
        p2 = paras[2].text
        p3 = paras[3].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.defenceaviationpost.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        head = "*" + h.text.rstrip("\n") + "*"
        p1 = paras[0].text
        p2 = paras[1].text
        p3 = paras[2].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.geo.tv/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        head = "*" + h.text.rstrip("\n") + "*"
        p1 = paras[1].text
        p2 = paras[2].text
        p3 = paras[3].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://timesofislamabad.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        head = "*" + h.text.rstrip() + "*"
        p1 = paras[0].text
        p2 = paras[1].text
        p3 = paras[2].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.indiatoday.in/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        head = "*" + h.text.rstrip() + "*"
        p1 = paras[2].text
        p2 = paras[3].text
        p3 = paras[4].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://dailytimes.com.pk/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # print(paras)
        head = "*" + h.text.rstrip() + "*"
        p1 = paras[6].text
        p2 = paras[8].text
        p3 = paras[9].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://sputniknews.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # print(paras)
        head = "*" + h.text.rstrip() + "*"
        p1 = paras[3].text.strip("\n")
        p2 = paras[4].text
        p3 = paras[3].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://tribune.com.pk/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # print(paras)
        head = "*" + h.text.rstrip() + "*"
        p1 = paras[1].text
        p2 = paras[2].text
        p3 = paras[3].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.ndtv.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # print(paras)
        head = "*" + h.text.strip() + "*"
        p1 = paras[1].text
        p2 = paras[2].text
        p3 = paras[3].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.indiablooms.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # print(paras)
        head = "*" + h.text.strip() + "*"
        p1 = paras[2].text.strip()
        p2 = paras[3].text.strip()
        p3 = paras[4].text.strip()
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.bbc.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.strip() + "*"
        p1 = paras[12].text.strip()
        p2 = paras[13].text.strip()
        p3 = paras[14].text.strip()
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://idrw.org/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.strip() + "*"
        p1 = paras[3].text.strip()
        p2 = paras[4].text.strip()
        p3 = paras[5].text.strip()
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.foxnews.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.strip() + "*"
        p1 = paras[3].text.strip()
        p2 = paras[4].text.strip()
        p3 = paras[4].text.strip()
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.aboutpakistan.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        # head = "*" + h.text.rstrip() + "*"

        p1 = paras[0].text
        p2 = paras[1].text
        p3 = paras[2].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.news18.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.rstrip() + "*"

        p1 = paras[0].text
        p2 = paras[1].text
        p3 = paras[1].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.urdupoint.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.rstrip() + "*"
        # print(head)
        p1 = paras[1].text
        p2 = paras[2].text
        p3 = paras[2].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.paktribune.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup.prettify())
        h = soup.find('h3')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.rstrip() + "*"

        p1 = paras[0].text
        p2 = paras[1].text
        p3 = paras[2].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://onlineindus.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup.prettify())
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.rstrip() + "*"

        p1 = paras[13].text
        p2 = paras[14].text
        p3 = paras[14].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://www.bolnews.com/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup.prettify())
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.rstrip() + "*"

        p1 = paras[3].text
        p2 = paras[4].text
        p3 = paras[4].text
        sendMessage(head, p1, p2, p3, l)
    elif result == "https://nation.com.pk/":
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup.prettify())
        h = soup.find('h1')
        paras = soup.find_all('p')
        # for i in range(len(paras)):
        #     print(i)
        #     print(paras[i].text)
        head = "*" + h.text.rstrip() + "*"

        p1 = paras[2].text
        p2 = paras[3].text
        p3 = paras[3].text
        sendMessage(head, p1, p2, p3, l)


seconds=time.time() - start_time
print("Execution Time:")
print("--- %s seconds ---" % (int(seconds)))
minutes = seconds / 60
print("--- %.2f minutes ---" % (float(minutes)))
