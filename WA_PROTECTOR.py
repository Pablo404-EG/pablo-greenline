import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Style

R = Fore.RED
G = Fore.GREEN
W = Fore.WHITE

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

suspicious_keywords = ["XPHANTOM", "9999999999", "8888888888"]

def get_known_contacts():
    driver.get("https://web.whatsapp.com")
    print(f"{G}[+]{W} Please scan the QR code to login to WhatsApp Web...")
    time.sleep(30)  

    print(f"{G}[+]{W} Fetching known contacts...")
    known_contacts = set()

    contacts = driver.find_elements(By.XPATH, '//span[@class="_3ko75 _5h6Y_ _3Whw5"]')
    for contact in contacts:
        known_contacts.add(contact.text)
    
    print(f"{G}[+]{W} Known contacts fetched: {len(known_contacts)}")
    return known_contacts

def block_unknown_contacts():
    known_contacts = get_known_contacts()

    while True:
        try:
            unknown_contacts = driver.find_elements(By.XPATH, '//div[@class="_3OvU8"]')
            
            for contact in unknown_contacts:
                contact_name = contact.text
                if contact_name not in known_contacts:
                    print(f"{R}[!]{W} Unknown contact detected: {contact_name}")
                    contact.click()
                    time.sleep(2)
                    
                    driver.find_element(By.XPATH, '//div[@data-testid="menu"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//div[text()="Block"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//div[text()="BLOCK"]').click()
                    print(f"{G}[✓]{W} Contact {contact_name} has been blocked.")
                else:
                    print(f"{G}[✓]{W} Known contact: {contact_name}")
            
            time.sleep(10)  
        except Exception as e:
            print(f"{R}[×] Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    block_unknown_contacts()
