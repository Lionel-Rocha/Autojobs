import os

from flask import Flask, render_template, jsonify
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
    else:
        dados_combinados = main()  # Você pode implementar essa função se necessário

    return jsonify(dados_combinados)

if __name__ == '__main__':
    app.run(debug=True)
