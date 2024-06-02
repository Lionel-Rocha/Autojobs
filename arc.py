from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


def pega_vagas():
    try:
        firefox_options = Options()
        firefox_options.add_argument("--headless")

        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)

        url = "https://arc.dev/remote-jr-jobs"
        driver.get(url)

        driver.implicitly_wait(10)

        section = driver.find_element(By.CSS_SELECTOR, 'section.sc-54d12837-0.kaFWQn')

        link_elements = section.find_elements(By.TAG_NAME, 'a')

        # Filtra os links que correspondem ao padrão desejado
        links_vagas = []
        for link in link_elements:
            href = link.get_attribute('href')
            if href and href.startswith('https://arc.dev/remote-jobs/j/') and not (href in links_vagas):
                links_vagas.append(href)

        # Extrai títulos das páginas dos links
        titulo_vagas = []
        for link in links_vagas:
            driver.get(link)
            driver.implicitly_wait(10)
            # Encontra o elemento cujo atributo 'class' contém a palavra 'title'
            try:
                title_element = driver.find_element(By.XPATH, "//*[contains(@class, 'title')]")
                title = title_element.text
                titulo_vagas.append({'title': title,'link': link})
            except Exception as e:
                print(f"Could not get title for {link}: {e}")

        driver.quit()

        lista_vagas = []

        for i in range(len(links_vagas)):
            lista_vagas.append(titulo_vagas[i])

        return lista_vagas

    except Exception as e:
        print(f"An error occurred: {e}")
