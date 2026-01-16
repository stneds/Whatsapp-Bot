from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def send_message(number, message, profile_path):
    options = Options()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new") 
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        print(f"Abrindo conversa com {number}...")
        url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        driver.get(url)

        print("Aguardando carregamento da página (40s)...")
        time.sleep(50)  # Tempo seguro para carregar chats
        
        # Procura a caixa de texto e aperta ENTER
        input_box = driver.find_element(By.XPATH, '//*[@id="main"]//footer//*[@role="textbox"]')
        input_box.send_keys(Keys.ENTER)
        
        print("SUCESSO: Enter pressionado! Mensagem enviada.")
        
        time.sleep(5) # Espera um pouco para garantir o envio antes de fechar

    except Exception as e:
        print(f"Erro ao tentar enviar: {e}")
        driver.save_screenshot("debug_erro_final.png")
    finally:
        driver.quit()
        print("Limpando terminal em 3 ... 2 ... 1 ...")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')