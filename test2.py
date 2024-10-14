#Добавляем автоматизированный скриншотинг:
#Добавляем перезагрузку страницы
from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("dom.png")  #В кавычках указываем название, которое присвоится скриншоту
time.sleep(5)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(3)

browser.refresh()

browser.quit()
#Закрываем браузер