from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set path ke driver Chrome
chrome_driver_path = "/usr/bin/chromedriver"

# Inisialisasi browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Mode tanpa GUI
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Buka halaman airdrop
driver.get("https://blockmesh.io/airdrop")

time.sleep(3)  # Tunggu halaman terbuka

# Contoh input email
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("emailanda@example.com")
email_input.send_keys(Keys.RETURN)

time.sleep(2)  # Tunggu submit selesai

# Screenshot sebagai bukti
driver.save_screenshot("airdrop_success.png")

# Tutup browser
driver.quit()
