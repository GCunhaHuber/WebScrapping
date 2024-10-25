from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from unidecode import unidecode
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

with open("log.txt", "w") as log_file:

    def extrair_titulos_de_jogos(url):
        start_time = time.time()
        driver.get(url)
        wait = WebDriverWait(driver, 20)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@rel='bookmark']")))
            game_links = driver.find_elements(By.XPATH, "//a[@rel='bookmark']")
            game_titles = [unidecode(link.text).replace('Ç', 'C') for link in game_links]
            
            end_time = time.time()
            processing_time = end_time - start_time

            log_file.write(f"Processou {url} em {processing_time:.2f} segundos.\n")
            return game_titles

        except TimeoutException:
            log_file.write(f"Erro ao carregar a pagina {url} ou os elementos nao foram encontrados.\n")
            return []

    def navegar_entre_paginas(numero_de_paginas):
        base_url = "https://fitgirl-repacks.site/page/"
        todos_os_jogos = []

        for pagina in range(1, numero_de_paginas + 1):
            url = f"{base_url}{pagina}/"
            todos_os_jogos.extend(extrair_titulos_de_jogos(url))
        
        return todos_os_jogos

    numero_de_paginas = 10

    lista_de_jogos = navegar_entre_paginas(numero_de_paginas)

    driver.quit()

    # Registra a lista de jogos encontrados no log
    log_file.write("\nLista de jogos encontrados:\n")
    for jogo in lista_de_jogos:
        log_file.write(f"{jogo}\n")

    for jogo in lista_de_jogos:
        print(jogo)
 
 
 