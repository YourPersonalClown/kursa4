import undetected_chromedriver
# import time
from random import randint


from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep as pause
import openpyxl


# book = openpyxl.open('products.xlsx', read_only=False)
# sheet = book.active





def get_price_mvideo(prod_name, driver):
    wait = WebDriverWait(driver, 10, 0.5)
    prodict = []
    driver.get(f'https://www.mvideo.ru/product-list-page?q={prod_name}')
    element = wait.until(EC.visibility_of_element_located((
    By.CLASS_NAME,
    'product-cards-row')))
    final_name =  element.find_elements(By.CLASS_NAME, 'product-title__text')[0].text
    final_price = element.find_elements(By.CLASS_NAME, 'price__main-value')[0].text
    final_link = element.find_elements(By.CLASS_NAME, 'product-title__text')[1].get_attribute('href')


    prodict.append( prod_name)
    prodict.append( final_name)
    prodict.append( final_link)
    prodict.append( int(final_price[:-2].replace(' ','')))


    return prodict



def get_price_dns(prod_name, driver):
    # wait = WebDriverWait(driver, 5)
    prodict = []
    prodict.append( prod_name)
    prod_name = prod_name.replace(' ','+')


    try:
        driver.get(f'https://www.dns-shop.ru/search/?q={prod_name}')

    except:
        ...
        
#     element = wait.until(EC.visibility_of_element_located((
#     By.CLASS_NAME,
#     'container category-child'
#  )))

    pause(randint(7, 11))
    # driver.set_page_load_timeout(10)
    product_card = driver.find_elements(By.CLASS_NAME, 'catalog-product')
    product_card = product_card[0]
    final_name =  product_card.find_element(By.CLASS_NAME, 'catalog-product__name').text
    final_price = product_card.find_element(By.CLASS_NAME, 'product-buy__price').text
    final_link =  product_card.find_element(By.CLASS_NAME, 'catalog-product__name').get_attribute('href')

    # prodict = {}
    # prodict['user_promt'] = prod_name
    prodict.append(final_name)
    prodict.append(final_link)
    final_price = final_price.split(' ')[:2]
    prodict.append( int(float(''.join(final_price))) )



    return prodict