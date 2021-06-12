from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd

# to setting chrome options to downloading file into our choice location

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\ Users\s\Desktop\python_pro\projects"})

driver = webdriver.Chrome(executable_path="E:\project\chromedriver.exe",chrome_options=chromeOptions)

driver.maximize_window()

driver.get("https://ceva.invoize.com/login#")

#mail_id = input("Enter your email id :")
#password = input("Enter your password :")

#driver.find_element_by_name("userEmail")

# or

driver.find_element(By.NAME,"userEmail").send_keys("surendrakumar.aratikatla@searce.com")
driver.find_element_by_name("password").send_keys("Ceva@123")

driver.find_element_by_id("notloginLoader").click()

try:
    wait = WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.NAME, "forcedLoginChkBox")))
    driver.find_element_by_name("forcedLoginChkBox").click()
    driver.find_element_by_id("notloginLoader").click()

except:
    print('good to go')

driver.implicitly_wait(10)

try:
    wait3 = WebDriverWait(driver,10)
    wait3.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main-content']/div/div[3]/div/ul/li[3]/a")))
    driver.find_element_by_xpath("//*[@id='main-content']/div/div[3]/div/ul/li[3]/a").click()
finally:
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//*[@id='bprTable']/tbody[2]/tr[1]/td[11]/span").click()

    driver.implicitly_wait(5)


try:
    wait1 = WebDriverWait(driver,20)
    wait1.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='navbar-container']/div[2]/div/ul/li[1]/a/i")))
    driver.find_element_by_xpath("//*[@id='navbar-container']/div[2]/div/ul/li[1]/a/i").click()

finally:
    #driver.find_element_by_xpath("//*[@id='navbar-container']/div[2]/div/ul/li[1]/div/ul/li[2]/div/div[2]/div[3]/div/span").click()
    driver.implicitly_wait(5)

# now we are applying pandas techniques

df = pd.read_excel('Summary-Details_2019-03-10 23-40-09.xlsx',sheet_name='Undelivered')
df1 = df[['Booking Number','Invoice Number','Age','Shipment Status']]
print(df1.head())
