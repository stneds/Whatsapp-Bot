from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def send_message(number, message, profile_path):
    
    options = Options()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--remote-debugging-port=9222")



    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        print(f"Abrindo conversa com {number}...")
        driver.get(f"https://web.whatsapp.com/send?phone={number}")

        print("Aguardando WhatsApp carregar...")
        time.sleep(50)

        input_box = driver.find_element(
            By.XPATH,
            '//footer//div[@contenteditable="true"]'
        )

        input_box.click()
        time.sleep(1)

        input_box.send_keys(message)
        time.sleep(1)
        input_box.send_keys(Keys.ENTER)

        print("✅ Mensagem REALMENTE enviada")
        driver.save_screenshot("mensagem_enviada.png")

        time.sleep(5) # Espera um pouco para garantir o envio antes de fechar

    except Exception as e:
        print(f"Erro ao tentar enviar: {e}")
        driver.save_screenshot("debug_erro_final.png")
    finally:
        driver.quit()
        # print("Limpando terminal em 3 ... 2 ... 1 ...")
        time.sleep(3)
        # os.system('cls' if os.name == 'nt' else 'clear')
