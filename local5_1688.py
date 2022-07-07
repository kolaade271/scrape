from time import sleep
from selenium import webdriver
from googletrans import Translator
translator = Translator()
import os
from urllib.parse import urlparse
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from flask import Flask
from flask import request
import re



app = Flask(__name__)
@app.route('/url/', methods=['GET', 'POST', 'DELETE'])
def message():
    url = request.args.get('url')
    options = webdriver.ChromeOptions() 
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-sh-usage")
    options.add_argument("start-maximized")
    options.add_argument("--auto-open-devtools-for-tabs")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
    driver = webdriver.Chrome(DRIVER_BIN)
    #driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER PATH"), chrome_options=options)
    
    domain = urlparse(url).netloc
    if domain == "m.1688.com" or  domain == "detail.1688.com":

        driver.get("https://user.lovbuy.com/item.php?url="+str(url)+"")
        sleep(10)
        productname = driver.find_element_by_xpath("//html/body/div/div/div/div[2]/h5[1]")
        mainimg = driver.find_element_by_xpath("//html/body/div/div/div/div[1]/div/div[1]/img")
        price = driver.find_element_by_xpath("//html/body/div/div/div/div[2]/h4/strong")
        shipping = driver.find_element_by_xpath("//html/body/div/div/div/div[2]/h5[3]/strong")
        quantity = driver.find_element_by_xpath("//html/body/div/div/div/div[2]/form/div/input")
        firstimage = mainimg.get_attribute('src')
        minquantity = quantity.get_attribute('value')
        numobj  = driver.find_elements_by_xpath('//*[contains(@class, "panel-title")]')
        datas1  = driver.find_elements_by_xpath('//*[contains(@class, "0ATTR")]')
        datas2  = driver.find_elements_by_xpath('//*[contains(@class, "1ATTR") and @type="button"]')
        view1 = []
        view2 = []
        allobj = []
        for myobj in numobj:
            try:
                seeobj =myobj.text
                allobj.append(seeobj)
            except TimeoutException as ex:
                allobj=0
        countobj = len(allobj)

        for datax in datas1:
            try:
                mydata =datax.get_attribute("data-original-title")
                view1.append(mydata)
            except TimeoutException as ex:
                print("nodata")

        for dataxx in datas2:
            try:
                mydata2 =dataxx.text
                view2.append(mydata2)
            except TimeoutException as ex:
                print("nodata")

        allimg=[]

        
        imgs = driver.find_elements_by_xpath("//img")
        for img in imgs:
            try:
                allimgx =img.get_attribute("src")
                
                allimg.append(allimgx)
            except TimeoutException as ex:
                print ("nodata")


        if countobj == 2:

            obj2 = allobj[1]
        else:
            obj2 = 0
        allimg.remove('https://www.lovbuy.com/res/imgs/logo.svg')
        
        
        x = { "name":productname.text, "price":price.text, "shipping":shipping.text,"minquantity":minquantity,"info1":view1, "info2":view2,"info1name":allobj[0],"info2name":obj2,"firstimg":firstimage, "allimg":allimg}
        response = json.dumps(x)

        print(response)
        return response
    elif domain == "m.intl.taobao.com" or  domain == "detail.1688.com":
        driver.get("https://user.lovbuy.com/item.php?url="+str(url)+"")
        sleep(10)
        productname = driver.find_element_by_xpath("//html/body/div/div/div/div[5]/h5[1]/a")
        mainimg = driver.find_element_by_xpath("//html/body/div/div/div/div[4]/div/div[1]/img")
        price = driver.find_element_by_xpath("//html/body/div/div/div/div[5]/h4/strong")
        shipping = driver.find_element_by_xpath("//html/body/div/div/div/div[5]/h5[3]/strong")
        quantity = driver.find_element_by_xpath("//html/body/div/div/div/div[5]/form/div/input")
        firstimage = mainimg.get_attribute('src')
        minquantity = quantity.get_attribute('value')
        numobj  = driver.find_elements_by_xpath('//*[contains(@class, "panel-title")]')
        datas1  = driver.find_elements_by_xpath('//*[contains(@class, "1ATTR")]')
        datas2  = driver.find_elements_by_xpath('//*[contains(@class, "0ATTR") and @type="button"]')
        view1 = []
        view2 = []
        allobj = []
        for myobj in numobj:
            try:
                seeobj =myobj.text
                allobj.append(seeobj)
            except TimeoutException as ex:
                allobj=0
        countobj = len(allobj)

        for datax in datas1:
            try:
                mydata =datax.get_attribute("data-original-title")
                view1.append(mydata)
            except TimeoutException as ex:
                print("nodata")

        for dataxx in datas2:
            try:
                mydata2 =dataxx.text
                view2.append(mydata2)
            except TimeoutException as ex:
                print("nodata")

        allimg=[]

        
        imgs = driver.find_elements_by_xpath("//img")
        for img in imgs:
            try:
                allimgx =img.get_attribute("src")
                
                allimg.append(allimgx)
            except TimeoutException as ex:
                print ("nodata")


        if countobj == 2:

            obj2 = allobj[0]
        else:
            obj2 = 0
        allimg.remove('https://www.lovbuy.com/res/imgs/logo.svg')
        
        
        x = { "name":productname.text, "price":price.text, "shipping":shipping.text,"minquantity":minquantity,"info1":view1, "info2":view2,"info1name":allobj[1],"info2name":obj2,"firstimg":firstimage, "allimg":allimg}
        response = json.dumps(x)

        print(response)
        return response
    elif domain == "www.alibaba.com" or  domain == "m.alibaba.com":
        driver.get(str(url))
        numobj  = driver.find_elements_by_xpath('//*[contains(@class, "ma-quantity-range")]')
        
        try:
            productname = driver.find_element_by_xpath("//html/body/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/h1")
            quantity = driver.find_element_by_xpath("//html/body/div[3]/div/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div[1]/div[1]")
            range1 = driver.find_element_by_xpath("//html/body/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/ul/li[1]/span")
            range2 = driver.find_element_by_xpath("//html/body/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/ul/li[2]/span")
        
            range3 = driver.find_element_by_xpath("//html/body/div[3]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/ul/li[3]/span")
            range3x = range3.text
        except:
            range1 = "0"
            range2 = "0"
            range3x = "0"
            
        try:
            range4 = driver.find_element_by_xpath("//html/body/div[3]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/ul/li[4]/span")
            range4x = range4.text
        except:
            range4x = "0"


        price1 = driver.find_element_by_xpath("//html/body/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/ul/li[1]/div[1]/span")
        price2 = driver.find_element_by_xpath("//html/body/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/ul/li[2]/div[1]/span")
        try:
            price3 = driver.find_element_by_xpath("//html/body/div[3]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/ul/li[3]/div[1]/span")
            trueprice3 = price3.text
        except:
            trueprice3 = "0"

        try:
            price4 = driver.find_element_by_xpath("//html/body/div[3]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/ul/li[4]/div[1]/span")
            trueprice4= price4.text
        except:
            trueprice4 = "0"
        
        try:
            a =1
        except:
            a = "0"
        
        try:
            infoname2 = driver.find_element_by_xpath("//html/body/div[3]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[8]/div/div[4]/div[2]/dl[1]/dt")
            infoname2x= infoname2.text
        except:
            infoname2x = "0"
        infoname1  = driver.find_elements_by_xpath('//*[contains(@class, "name")]')
        infoname1x= infoname1


        
            
       
        x = { "name":productname.text}
        response = json.dumps(x)
       # return response
    elif domain == "detail.tmall.hk" or domain == "detail.tmall.com" or domain =="item.taobao.com":
        result=[]
        driver.get(str(url))
        #driver.find_element_by_xpath("//html/body/div[9]/div[2]/div").click()
        chinesename = driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1')
        price = driver.find_element_by_xpath('//*[@id="J_StrPriceModBox"]')
        try:
            size = driver.find_elements_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li')
            result = [{ "size": category.text} 
                for category in size]
        except:
            size = []
        
          
        try:
            color = driver.find_elements_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/ul/li')
            result2 = [{"image":category.get_attribute("src"), "color": category.text} 
                for category in color]
        except:
            color = []
        
        productname = chinesename.text

        try:
            image = driver.find_elements_by_xpath('//*[@id="J_UlThumb"]/li[1]/a/img')
            result3 = [{"image":category.get_attribute("src")} 
                for category in image]
        except:
            image = []
            
        try:
            
            sleep(10)
           
            
        except:
            tt = 0
        allimg =[]
        #imgs = driver.find_elements_by_xpath("//html/body/div[5]/div/div[2]/div/div[1]/div[2]/div[2]")
        # for img in imgs:
        #     try:
        #         allimgx =img.get_attribute("src")
                
        #         allimg.append(allimgx)
        #     except:
        #         print ("nodata")
        
        x = { "name":productname,"price":price.text,"size":result,"color":result2,"image":result3}
        response = json.dumps(x)
        return x


    
    
    #driver.close()

if __name__ == "__main__":
    app.run(debug=True)