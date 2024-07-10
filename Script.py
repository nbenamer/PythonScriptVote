import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import pyautogui
from screeninfo import get_monitors



def vote_and_validate():
    profile_path = r"C:\Users\Gaming\AppData\Local\Google\Chrome\User Data"
    
   

    # Configure Chrome options
    options = Options()
    
   
    options.add_argument(f"user-data-dir={profile_path}")
    
    
    

    # Configure the ChromeDriver service
    service = Service('chrd/chromedriver.exe')  # Specify the path to your chromedriver executable

    # Initialize Chrome driver with the configured options and service
    driver = uc.Chrome(options=options, service=service, use_subprocess=True)


    try:
        #Your script logic here
        driver.get("https://arcadia-game.com/vote")
        time.sleep(4)
        btnallervoter = driver.find_element(By.CLASS_NAME , 'btn-blok')
        btnallervoter.click()
        time.sleep(5)
        x, y = 1500, 770
        pyautogui.click(x, y)
        time.sleep(6)
        #Changer d'onglet
        x, y = 143, 26
        pyautogui.click(x, y)
        time.sleep(3)
       
        
        #Page de validation QUI MARCHE
        x, y = 370, 679
        pyautogui.click(x, y)
        time.sleep(1)
        boutondone = driver.find_element(By.NAME , 'done')
        boutondone.click()
        time.sleep(1)
        x, y = 412, 761
        pyautogui.click(x, y)
        time.sleep(1)

    finally:
        # Ensure the browser is closed after tasks are completed
        driver.quit()

if __name__ == "__main__":
    while (1):
        vote_and_validate()
        time.sleep(5400) 