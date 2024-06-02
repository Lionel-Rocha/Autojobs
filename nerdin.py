import requests
from bs4 import BeautifulSoup


def extrair_vagas_e_links(url):
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        vagas_links = {}  # Dicionário para armazenar o título da vaga e seu link associado

        # Encontre todos os elementos <a> na página
        links = soup.find_all('a', href=True)

        for link in links:
            href = link.get('href')
            if href and href.startswith('vaga') and 'vagas' not in href:
                # Extrai o texto do link para identificar a vaga
                titulo_vaga = link.get_text(strip=True)
                # Adiciona o título da vaga e seu link associado ao dicionário
                vagas_links[titulo_vaga] = "https://www.nerdin.com.br/" + href

        return vagas_links
    else:
        print('Erro ao acessar a página:', response.status_code)
        return None


def main():
    url = 'https://nerdin.com.br/func/FVagaListar.php?CodigoNivel=4,3,7,6&CodigoCidade=3246'
    vagas_links = extrair_vagas_e_links(url)
    vagas_completas = []
    if vagas_links:
        for titulo_vaga, link_vaga in vagas_links.items():
            vaga = {'title':titulo_vaga,'link':link_vaga}
            vagas_completas.append(vaga)

    return vagas_completas
