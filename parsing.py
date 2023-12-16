import undetected_chromedriver
# import time


from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import openpyxl


# book = openpyxl.open('products.xlsx', read_only=False)
# sheet = book.active


driver = undetected_chromedriver.Chrome()
wait = WebDriverWait(driver, 10, 0.5)



def get_price_mvideo(prod_name, driver):
    wait = WebDriverWait(driver, 10, 0.5)
    prodict = {}
    driver.get(f'https://www.mvideo.ru/product-list-page?q={prod_name}')
    element = wait.until(EC.visibility_of_element_located((
    By.CLASS_NAME,
    'product-cards-row')))
    final_name =  element.find_elements(By.CLASS_NAME, 'product-title__text')[0].text
    final_price = element.find_elements(By.CLASS_NAME, 'price__main-value')[0].text
    final_link = element.find_elements(By.CLASS_NAME, 'product-title__text')[1].get_attribute('href')


    prodict['user_promt'] = prod_name
    prodict['mvideo_name'] = final_name
    prodict['mvideo_link'] = final_link
    prodict['mvideo_price'] = int(final_price[:-2].replace(' ',''))


    return prodict