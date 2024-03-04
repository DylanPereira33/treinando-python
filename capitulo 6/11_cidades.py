cities = {'Tokio':{'country':'Japão','population':13.9,'fact':'combina o estilo ultramoderno com o tradicional.'},
          'Rio de janeiro':{'country':'Brasil','population':6.7,'fact':'famosa pelas praias de Copacabana e Ipanema.'},
                'Berlim':{'country':'Alemanha','population':3.6,'fact':'existe desde o século XIII.'}}

for city,info in cities.items():
    print(f"{city} fica no {info['country']}, tem uma população média de {info['population']} milhões, além de, {info['fact']}")
    print("\n")