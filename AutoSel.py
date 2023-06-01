import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_auto_update import check_driver
import selenium.webdriver.support.expected_conditions as EC
import os
import traceback
from bs4 import BeautifulSoup as bs

ProductsEachPage = 55
df = pd.DataFrame(columns=["Product Description", "Price","Sold","Rate","Shipping","Link"])


def webdriver_install():
    # Check the version of Chrom Driver and download the last one
    try:
        check_driver(os.getcwd())
    except Exception:
        print(traceback.print_exc())

def aliexpress_driver():
    url = 'https://www.aliexpress.com/'
    browser = webdriver.Chrome()
    browser.get(url)
    return browser

def automate_scroll(driver):
    # To automate the scroll up and scroll down the website
    # Define an initial value
    temp_height = 0
    while True:
        # Looping down the scroll bar
        driver.execute_script("window.scrollBy(0,1000)")
        # sleep and let the scroll bar react
        time.sleep(5)
        # Get the distance of the current scroll bar from the top
        check_height = driver.execute_script(
            "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
        # If the two are equal to the end
        if check_height == temp_height:
            break
        temp_height = check_height

    time.sleep(10)

def search_for(product,Qty, FilePath,Price=False, ProductName=False, ProductLink=False, Shipping=False, Rate=False, SoldAmount=False):
    browser = aliexpress_driver()
    wait = WebDriverWait(browser, 3)

    search = wait.until(EC.visibility_of_element_located((By.ID, 'search-key')))
    search.send_keys(product)
    search.send_keys(Keys.ENTER)

    # wait for the element to get located to click
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.law18--btn--29ue4Ne.law18--left--2XI39FE'))).click()
        time.sleep(1)
    except:
        pass

    collect_data(browser.current_url, Qty ,FilePath,browser,Price, ProductName, ProductLink, Shipping, Rate, SoldAmount)



def collect_data(product_link, Qty,FilePath,browser,Price=False, ProductName=False, ProductLink=False, Shipping=False, Rate=False, SoldAmount=False):

    df_list = []
    dict = {}

    wait = WebDriverWait(browser, 10)

    global df

    numberOfPages = int(Qty/55) #2
    ReminderOfResult = (Qty%55)
    global ProductsEachPage

    automate_scroll(browser)

    while (numberOfPages>=0):

        #print("This is ====================",numberOfPages)
        if (numberOfPages == 0):
            ProductsEachPage = ReminderOfResult

        for i in range(1,ProductsEachPage+1):

            item = browser.find_element(By.XPATH, '//*[@id="card-list"]/a['+str(i)+']')

            if ProductLink:
                #time.sleep(1)
                #print(item.get_attribute("href"))#link
                Link = item.get_attribute("href")
            else:
                Link = ''

            if Price:
                #time.sleep(1)
                #print(item.find_element(By.XPATH,'.//div[2]/div[1]/div[1]').text)#price
                price = item.find_element(By.CLASS_NAME,'manhattan--price-sale--1CCSZfK').text
            else:
                price= ''

            #print(Link)
            #print(Price)
            if SoldAmount:
                try:
                    time.sleep(1)
                    #print(item.find_element(By.CLASS_NAME,"manhattan--trade--2PeJIEB").text)#sold
                    Sold = item.find_element(By.CLASS_NAME,"manhattan--trade--2PeJIEB").text
                except:
                    #print("No Sold Data")
                    Sold = ""
            else:
                Sold = ""


            if ProductName:
                try:
                    time.sleep(2)
                    #print(item.find_element(By.CLASS_NAME, "manhattan--titleText--WccSjUS").text) #Name
                    Name = item.find_element(By.CLASS_NAME, "manhattan--titleText--WccSjUS").text

                except:
                    #print("No Name Data")
                    Name = ""
            else:
                Name = ""

            if Rate:
                try:
                    time.sleep(2)
                    #print(item.find_element(By.CLASS_NAME, "manhattan--evaluation--3cSMntr").text)  # Rate
                    rate = item.find_element(By.CLASS_NAME, "manhattan--evaluation--3cSMntr").text
                except:
                    #print("No Rate Data")
                    rate = ""
            else:
                rate = ""


            if Shipping:
                try:
                    time.sleep(2)
                    #print(item.find_element(By.CLASS_NAME, "tag--text--2VtIxqd tag--textStyle--vcAi3Rh").text)  # Shipping
                    shipping = item.find_element(By.CLASS_NAME, "tag--text--2VtIxqd tag--textStyle--vcAi3Rh").text
                except:
                    #print("No Shipping Data")
                    shipping = ""
            else:
                shipping = ""


            dict = {
                "Product Description": Name, "Price": price ,"Sold": Sold ,"Rate": rate,"Shipping": shipping,"Link": Link}


            df = pd.concat([df, pd.DataFrame([dict])], ignore_index=True)

            #print('-------------------------------',i,'--------------')

        numberOfPages -= 1

        if (numberOfPages != 0):
            nextPage=browser.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div[2]/div[4]/div[1]/ul/li[9]')
            browser.execute_script('arguments[0].click()', nextPage)
            time.sleep(3)


    Full_FilePath = FilePath + "\\\\" + "Aliexpress.csv"

    print('The file will be save to:',Full_FilePath)
    df.to_csv(Full_FilePath, encoding='utf-8-sig')

    print("Done!")

if __name__ == "__main__":
    webdriver_install()
    #product_link, broswer = search_for("test")
    #collect_data(product_link, broswer)
    #search_for("pen",200, False, False, True, False, False, False)

