from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Adarsh\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe") #path to chrome web driver
driver.get("https://web.whatsapp.com/")
import time
import xlrd
loc = ("C:\\Users\\Adarsh\\Documents\\selenium_TUT.xlsx")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
time.sleep(10)
for i in range(3):
    name=sheet.cell_value(i,1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input").send_keys(name)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input").send_keys("\n")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys("Hey ")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(name)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys("Bot this side\n")
