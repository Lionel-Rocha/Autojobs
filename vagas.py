import nerdin
import csv
from jobspy import scrape_jobs

def obtem_vagas():
    cidade = "Rio de Janeiro"

    resposta_nerdin = nerdin.main()

    resposta_scrapping = resposta_nerdin

    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        search_term="estágio ti",
        location=cidade,
        distance=12,
        results_wanted=20,
        hours_old=168,
        country_indeed='Brazil',
    )

    jobs.to_csv("vagas_jobspy_estagio.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)

    resposta_jobspy_estagio = extrair_titulo_link('vagas_jobspy_estagio.csv')

    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        search_term="estágio software",
        location="Brazil",
        results_wanted=20,
        hours_old=168,
        country_indeed='Brazil',
        is_remote=True
    )

    jobs.to_csv("vagas_jobspy_estagio_remoto.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)

    resposta_jobspy_estagio_remoto = extrair_titulo_link('vagas_jobspy_estagio_remoto.csv')

    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        search_term="software junior",
        location=cidade,
        distance=12,
        results_wanted=20,
        hours_old=168,
        country_indeed='Brazil',
    )

    jobs.to_csv("vagas_jobspy_junior.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)

    resposta_jobspy_junior = extrair_titulo_link('vagas_jobspy_junior.csv')

    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        search_term="software junior",
        location="Brazil",
        results_wanted=20,
        hours_old=168,
        country_indeed='Brazil',
        is_remote=True
    )
    jobs.to_csv("vagas_jobspy_junior_remoto.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)

    resposta_jobspy_junior_remoto = extrair_titulo_link('vagas_jobspy_junior_remoto.csv')

    resposta_jobspy = resposta_jobspy_estagio + resposta_jobspy_junior + resposta_jobspy_estagio_remoto + resposta_jobspy_junior_remoto

    resposta_total = resposta_scrapping + resposta_jobspy

    escrever_csv_respostas(resposta_total, 'vagas_totais.csv')


def escrever_csv_respostas(dados, nome_arquivo):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['Título', 'Link'])

        for dado in dados:
            escritor_csv.writerow([dado['title'], dado['link']])




def extrair_titulo_link(nome_arquivo):
    dados_extrair = []
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            titulo = linha['title']
            link = linha['job_url']
            dados_extrair.append({'title': titulo, 'link': link})
    return dados_extrair

