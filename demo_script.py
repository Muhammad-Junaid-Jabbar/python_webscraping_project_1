from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait
import os

# current directory files list
CurrentDirectoryFiles = os.listdir()
# current working directory path
CurrentPath = os.getcwd()

for i in CurrentDirectoryFiles:
    if i.endswith(".exe"):
        print(i)
        chromedriver_file = i
        break
chromedriver_file = CurrentPath + "\\" + chromedriver_file

opt=Options()
opt.add_argument("--disable-extensions")
opt.add_argument("--disable-infobars")
opt.add_argument("--disable-notifications")
opt.add_argument("--disable-popup-blocking")
opt.add_argument("--disable-prompt-on-repost")
opt.add_argument("--disable-sync")
opt.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36')
# opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver=webdriver.Chrome( executable_path=chromedriver_file,chrome_options=opt)
# url_ = str(input("Enter url: "))
driver.get("https://www.arbeitsagentur.de/jobsuche/suche?angebotsart=4&was=Fitness&wo=Hamberge,%20Holstein&umkreis=200")
# driver.get(url_)
input("Press Enter to continue...")

with open("email_list.txt", "w+") as f:
    for i in range(0,50):
        try:
            capcha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#jobdetails-kontaktdaten-container > div > jb-aas > form > div.loesung-container > div > label"))).text
            if capcha == 'Dargestellte Zeichen':
                print("please enter the capcha and then press enter")
                input("Press Enter to continue...")
        except:
            pass
        try:
            links3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#eintrag-{}-titel".format(str(i)))))
            print(links3.text)
            for j in range(0,2):
                try:
                    links3.click()
                    break
                except:
                    continue
            try:
                capcha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#jobdetails-kontaktdaten-container > div > jb-aas > form > div.loesung-container > div > label"))).text
            except:
                capcha = ''
                pass
            if capcha == 'Dargestellte Zeichen':
                print("please enter the capcha and then press enter")
                input("Press Enter to continue...")
            email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#jobdetail-angebotskontakt-email",)))
            print(email.text)
            f.write(email.text + "\n")
            f.flush()
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#close-modales-slide-in-detailansicht"))).click()
        except:
            try:
                button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#close-modales-slide-in-detailansicht"))).click()
                continue
            except:
                continue

driver.quit()
print("done")