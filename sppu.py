import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# SeatNumber = input("Enter Seat Number")
# MotherName = input("Enter Mother's Name")

driver = webdriver.Chrome()

driver.get("https://onlineresults.unipune.ac.in/result/dashboard/default")

#Search Box
search_box = driver.find_element(By.CSS_SELECTOR,".dataTables_filter input")
search_box.clear()
search_box.send_keys("S.E.(2019 CREDIT PAT.)") # Search Accroding to your Prefrence 

# Click Check on Result Button
element = driver.find_element(
    By.CSS_SELECTOR,
    ".btn.btn-outline-info.btn-sm.mt-2.dashboardbtnwidth"
)
element.click()

# Credentials

# Seat Number
seatno_input = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.ID, "SeatNo"))
)
seatno_input.clear()
seatno_input.send_keys("") # Enter Your Seat No.

# Mother's Name
mother_name = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.ID, "MotherName"))
)
mother_name.clear()
mother_name.send_keys("") # Enter Your Mother's Name.

# Get Result
get_Result = WebDriverWait(driver,15).until(
    EC.element_to_be_clickable((By.ID, "btn"))
)
get_Result.click()

time.sleep(2)

# Download Result
# download = driver.find_element(By.ID,"downlaod")
# download.click()

time.sleep(600)
driver.quit()