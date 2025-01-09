import requests
import csv

# Função para obter a lista de tipos de Pokémon
def obter_tipos():
    url = "https://pokeapi.co/api/v2/type"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Extrai os dados em formato JSON
        tipos = response.json()['results']
        return [tipo['name'] for tipo in tipos]
    else:
        print("Erro ao acessar a API para obter tipos")
        return []

# Função para obter as informações detalhadas sobre um tipo de Pokémon
def obter_informacoes_tipo(tipo):
    url = f"https://pokeapi.co/api/v2/type/{tipo}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Extrai as fraquezas, resistências e imunidades
        dados = response.json()
        fraquezas = [v['name'] for v in dados['damage_relations']['double_damage_to']]
        resistencias = [v['name'] for v in dados['damage_relations']['half_damage_to']]
        imunidades = [v['name'] for v in dados['damage_relations']['no_damage_to']]
        
        return {
            'Tipo': tipo,
            'Fraquezas': ', '.join(fraquezas),
            'Resistências': ', '.join(resistencias),
            'Imunidades': ', '.join(imunidades)
        }
    else:
        print(f"Erro ao acessar a API para o tipo: {tipo}")
        return None

# Função para salvar os dados em um arquivo CSV
def salvar_csv(dados, nome_arquivo="tipos_pokemon.csv"):
    # Especifica o cabeçalho do CSV
    cabecalho = ['Tipo', 'Fraquezas', 'Resistências', 'Imunidades']
    
    # Abre o arquivo CSV em modo de escrita
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=cabecalho)
        
        # Escreve o cabeçalho
        writer.writeheader()
        
        # Escreve os dados
        for item in dados:
            writer.writerow(item)

# Função principal
def main():
    # Obter a lista de tipos de Pokémon
    tipos = obter_tipos()
    
    if tipos:
        dados = []
        # Para cada tipo, obter as suas fraquezas, resistências e imunidades
        for tipo in tipos:
            informacoes_tipo = obter_informacoes_tipo(tipo)
            if informacoes_tipo:
                dados.append(informacoes_tipo)
        
        # Salva os dados no arquivo CSV
        salvar_csv(dados)
        print("Arquivo CSV salvo com sucesso!")
    else:
        print("Não foi possível obter tipos de Pokémon.")

# Executa o programa
if __name__ == "__main__":
    main()
