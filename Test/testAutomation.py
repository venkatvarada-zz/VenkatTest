from selenium import webdriver

driver = webdriver.Chrome("C:\Users\mindtree522\Downloads\chromedriver_win32\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("https://www.google.com")
driver.maximize_window()
driver.close()
driver.quit()
