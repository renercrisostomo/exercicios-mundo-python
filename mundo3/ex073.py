# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados. B) Os últimos 4 colocados da tabela. C) Uma lista com os times em ordem alfabética. D) Em que posição na tabela está o time da Chapecoense.

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O time da Chapecoense está na {times.index("Chapecoense") + 1}ª posição')

