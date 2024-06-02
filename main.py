import os

from flask import Flask, render_template
import pandas as pd
import vagas
app = Flask(__name__)

def main():
    print("Iniciando tarefa. Isso irá demorar um pouco.")
    vagas_totais = vagas.obtem_vagas()
    df = pd.read_csv('vagas_totais.csv')
    dados_combinados = df[['Título', 'Link']].to_dict(orient='records')
    return dados_combinados

def retorna_dados(arquivo):
    df = pd.read_csv(arquivo)
    dados_combinados = df[['Título', 'Link']].to_dict(orient='records')
    return dados_combinados

@app.route('/')
def index():
    if os.path.exists('vagas_totais.csv'):
        dados_combinados = retorna_dados('vagas_totais.csv')
        return render_template('index.html', dados=dados_combinados)
    else:
        dados_combinados = main()
        return render_template('index.html', dados=dados_combinados)

if __name__ == '__main__':
    app.run(debug=True)
