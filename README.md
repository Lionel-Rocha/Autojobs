<div align="center">

![image](https://github.com/Lionel-Rocha/Autojobs/assets/111009073/4439b0aa-a1e8-4b64-995d-ea06705a3133)


<img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/work_in-progress-C86B21?style=for-the-badge" alt="Work in progress"/>
</div>

Um pequeno script que automatiza a busca por vagas de emprego na área de Tecnologia da Informação, focado em vagas de estágio e júnior. A partir do uso das bibliotecas BeautifulSoup 4 e python-jobspy, foi possível obter vagas do arv.dev, NerdIn, Indeed, LinkedIn e Glassdoor. É possível mudar a cidade para vagas presenciais a partir da variável "cidade" no vagas.py, conforme ilustrado na imagem abaixo:

![image](https://github.com/Lionel-Rocha/Autojobs/assets/111009073/3604b110-992a-46a4-b285-f69785c371f4)

Ao iniciar com ```python main.py``` no terminal, o script irá abrir uma página web no endereço *http://127.0.0.1:5000/*. Caso o arquivo vagas_totais.csv não exista, ele irá criar um fazendo o scrapping das plataformas citadas acima (e caso você queira atualizar as vagas, remova esse arquivo). Esse processo irá demorar um pouco.
