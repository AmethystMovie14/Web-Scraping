import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

start_urls = ['https://www.accuweather.com/es/mx/mexico-city/242560/weather-forecast/242560',
                    'https://www.accuweather.com/es/mx/guadalajara/243735/weather-forecast/243735',
                    'https://www.accuweather.com/es/mx/monterrey/244681/weather-forecast/244681']


def extraer_clima():

    driver = webdriver.Edge()

    for url in start_urls:
        driver.get(url)

        time.sleep(2)

        ciudad = driver.find_element_by_xpath('//h1').text
        current = driver.find_element_by_xpath('//a[contains(@class, "cur-con-weather-card")]//div[@class="temp"]').text
        real_feal = driver.find_element_by_xpath('//a[contains(@class, "cur-con-weather-card")]//div[@class="real-feel"]').text
        
        real_feal = real_feal.replace('RealFeel®', '').replace('°','').replace('\n','').replace('\t','').replace('\r','').strip()
        current = current.replace('°','').replace('\n','').replace('\t','').replace('\r','').strip()

        f = open("datos-clima.csv", "a")
        f.write(f"{ciudad},{current},{real_feal}\n")
        f.close()

        print(ciudad)
        print(current)
        print(real_feal)
        print("\n")

    driver.close()

schedule.every(1).minute.do(extraer_clima)

extraer_clima()

while True:
    schedule.run_pending()
    time.sleep(1)