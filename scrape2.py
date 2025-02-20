from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://connect.mayoclinic.org/search/?search=vonoprazan"

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
driver.get(url)

divs = driver.find_elements(By.CLASS_NAME, "ch-search-result")
for div in divs:
    print(div.text)

driver.quit()
