''' Mini Projeto na qual fui solicitado em uma entrevista basicamente era para criar uma API que solicitava certos dados de um site relacionados a pokemons,
    tratar esses dados e retornar em um gráfico em forma de pizza.
    Mini Project in which I was asked in an interview was basically to create an API that requests data from a web site related to pokemons,
    treat this data and return it in a pie chart.
'''  


import matplotlib.pyplot as plt
import requests
import pandas as pd
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20")
data = response.json()
#display(data['results'])


for i, pokemon in enumerate(data['results']):
    print(i, pokemon['name'])

choice = int(input("Escolha um a pokemon de acordo com o index: "))
response = requests.get(data['results'][choice]['url'])
pokemonSelected = response.json()



pokemonSelected['stats'][0]['stat']['name'], pokemonSelected['stats'][0]['base_stat'],
pokemonSelected['stats'][1]['stat']['name'], pokemonSelected['stats'][1]['base_stat'],
pokemonSelected['stats'][2]['stat']['name'], pokemonSelected['stats'][2]['base_stat'],
pokemonSelected['stats'][3]['stat']['name'], pokemonSelected['stats'][3]['base_stat'],
pokemonSelected['stats'][4]['stat']['name'], pokemonSelected['stats'][4]['base_stat'],
pokemonSelected['stats'][5]['stat']['name'], pokemonSelected['stats'][5]['base_stat']
#display(pokemonSelected)

df = pd.DataFrame(columns=['HP', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed'])
df['HP'] = pd.DataFrame([pokemonSelected['stats'][0]['base_stat']])
df['Attack'] = pd.DataFrame([pokemonSelected['stats'][1]['base_stat']])
df['Defense'] = pd.DataFrame([pokemonSelected['stats'][2]['base_stat']])
df['Sp. Attack'] = pd.DataFrame([pokemonSelected['stats'][3]['base_stat']])
df['Sp. Defense'] = pd.DataFrame([pokemonSelected['stats'][4]['base_stat']])
df['Speed'] = pd.DataFrame([pokemonSelected['stats'][5]['base_stat']])
#display(df)

final_df = df.T
#display(final_df)

plt.pie(final_df[0], labels=final_df.index, autopct='%1.1f%%', explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1], shadow=True)
plt.title('{} type {}'.format(pokemonSelected['name'], pokemonSelected['types'][0]['type']['name']))
plt.show()