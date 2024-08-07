paises = [
    ("Rússia", "Moscou", 146.2 milhões, 17.098.242 km², ["Armênia", "Azerbaijão", "Bielorrússia", "China", "Finlândia", "Geórgia", "Japão", "Cazaquistão", "Coreia do Norte", "Mongólia", "Noruega", "Polônia", "Ucrânia", "Uzbequistão"], "Europa"),
    ("Canadá", "Ottawa", 38.0 milhões, 9.984.670 km², ["Estados Unidos", "Groenlândia"], "América do Norte"),
    ("Estados Unidos", "Washington, D.C.", 332.4 milhões, 9.833.517 km², ["Canadá", "México"], "América do Norte"),
    ("China", "Pequim", 1.444 bilhões, 9.596.961 km², ["Afeganistão", "Butão", "Cazaquistão", "Coreia do Norte", "Espanha", "Filipinas", "Índia", "Japão", "Laos", "Mianmar", "Nepal", "Paquistão", "Rússia", "Tailândia", "Vietnã"], "Ásia"),
    ("Brasil", "Brasília", 213.2 milhões, 8.515.767 km², ["Argentina", "Bolívia", "Colômbia", "Guiana", "Paraguai", "Peru", "Suriname", "Venezuela"], "América do Sul"),
    ("Austrália", "Camberra", 25.7 milhões, 7.682.300 km², ["Indonésia", "Papua-Nova Guiné", "Timor-Leste"], "Oceania"),
    ("Índia", "Nova Deli", 1.404 bilhões, 3.287.263 km², ["Bangladesh", "Butão", "China", "Myanmar", "Nepal", "Paquistão", "Sri Lanka"], "Ásia"),
    ("Argentina", "Buenos Aires", 45.3 milhões, 2.780.400 km², ["Bolívia", "Brasil", "Chile", "Paraguai", "Uruguai"], "América do Sul"),
    ("Cazaquistão", "Nur-Sultão", 18.9 milhões, 2.724.900 km², ["China", "Coreia do Norte", "Rússia", "Uzbequistão", "Turquemenistão", "Quirguistão"], "Ásia"),
    ("Argélia", "Argel", 44.8 milhões, 2.381.741 km², ["Marrocos", "Níger", "Líbia", "Mali", "Tunisia", "Mauritânia"], "África"),
    ("República Democrática do Congo", "Kinshasa", 89.5 milhões, 2.345.410 km², ["Angola", "Burundi", "Camarões", "República Centro-Africana", "Chade", "Ruanda", "Sudan", "Tanzania"], "África"),
    ("Arábia Saudita", "Riade", 35.4 milhões, 2.149.690 km², ["Emirados Árabes Unidos", "Iêmen", "Kuwait", "Oman", "Jordânia", "Iraque", "Palestina"], "Ásia")
    ("México", "Cidade do México", 128.9 milhões, 1.972.550 km², ["Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Estados Unidos"], "América do Norte"),
    ("Indonésia", "Jacarta", 273.5 milhões, 1.904.569 km², ["Austrália", "Brunei", "Camboja", "China", "Filipinas", "Malásia", "Timor-Leste"], "Ásia"),
    ("Sudão", "Cartum", 45.4 milhões, 2.505.813 km², ["Chade", "Egito", "Eritreia", "Etiópia", "Quénia", "Sudão do Sul"], "África"),
    ("Líbia", "Trípoli", 6.9 milhões, 1.759.540 km², ["Argélia", "Chade", "Egito", "Níger", "Tunísia"], "África"),
    ("Irã", "Teerã", 84.3 milhões, 1.648.195 km², ["Armênia", "Azerbaijão", "Afeganistão", "Iraque", "Paquistão", "Turquia"], "Ásia"),
    ("Mongólia", "Ulaanbaatar", 3.2 milhões, 1.566.000 km², ["China", "Rússia"], "Ásia"),
    ("Peru", "Lima", 33.3 milhões, 1.285.216 km², ["Brasil", "Bolívia", "Chile", "Colômbia", "Equador"], "América do Sul"),
    ("Chade", "N'Djamena", 16.8 milhões, 1.284.000 km², ["Camerão", "Cazaquistão", "Líbia", "Níger", "Sudão"], "África"),
    ("Níger", "Niamey", 23.3 milhões, 1.267.000 km², ["Benim", "Burkina Faso", "Chade", "Mali", "Nigéria"], "África"),
    ("Angola", "Luanda", 33.1 milhões, 1.246.700 km², ["Benim", "Camarões", "República Democrática do Congo", "República do Congo", "Namibia", "Zâmbia"], "África"),
    ("Mali", 21.2 milhões, 1.240.192 km², ["Argélia", "Burkina Faso", "Camarões", "Níger", "Senegal", "Guiné", "Costa do Marfim"], "África"),
    ("África do Sul", "Pretória", 60.4 milhões, 1.219.912 km², ["Botsuana", "Lesoto", "Namíbia", "Swazilândia", "Zâmbia", "Zimbabwe"], "África"),
    ("Colômbia", "Bogotá", 51.0 milhões, 1.141.748 km², ["Brasil", "Equador", "Panama", "Peru", "Venezuela"], "América do Sul"),
    ("Etiópia", "Addis Abeba", 115.4 milhões, 1.104.300 km², ["Djibouti", "Eritreia", "Quênia", "Somália", "Sudão"], "África"),
    ("Bolívia", "La Paz", 11.8 milhões, 1.098.581 km², ["Brasil", "Chile", "Colômbia", "Paraguai", "Peru"], "América do Sul"),
    ("Mauritânia", "Nouakchott", 4.8 milhões, 1.030.700 km², ["Argélia", "Mali", "Marrocos", "Senegal"], "África"),
    ("Egito", "Cairo", 102.3 milhões, 1.001.450 km², ["Líbia", "Sudão", "Israel"], "África"),
    ("Tanzânia", "Dodoma", 61.2 milhões, 947.303 km², ["Burundi", "Comores", "Congo", "Malawi", "Moçambique", "Ruanda", "Zâmbia", "Quênia"], "África"),
    ("Nigéria", "Abuja", 216.1 milhões, 923.768 km², ["Benin", "Chade", "Camerão", "Níger", "Chade", "Gana", "Guiné-Bissau"], "África"),
    ("Venezuela", "Caracas", 28.4 milhões, 912.050 km², ["Colômbia", "Brasil", "Guiana", "Guiana Francesa"], "América do Sul"),
    ("Namíbia", "Windhoek", 2.5 milhões, 825.418 km², ["Angola", "Botsuana", "África do Sul", "Zâmbia"], "África"),
    ("Paquistão", "Islamabad", 220.8 milhões, 881.913 km², ["Afeganistão", "China", "Índia", "Irã", "Turquemenistão"], "Ásia"),
    ("Moçambique", "Maputo", 31.2 milhões, 801.590 km², ["África do Sul", "Malawi", "Zâmbia", "Tanzânia", "Zimbabwe"], "África"),
    ("Turquia", "Ancara", 84.3 milhões, 783.562 km², ["Armênia", "Azerbaijão", "Bulgária", "Grécia", "Iraque", "Irã", "Síria"], "Ásia"),
    ("Chile", "Santiago", 19.1 milhões, 756.102 km², ["Argentina", "Bolivia", "Peru"], "América do Sul"),
    ("Zâmbia", "Lusaka", 18.4 milhões, 752.618 km², ["Angola", "Malawi", "Moçambique", "Namíbia", "Tanzânia"], "África"),
    ("Mianmar", "Naypyidaw", 54.4 milhões, 676.578 km², ["China", "Índia", "Laos", "Tailândia"], "Ásia"),
    ("Afeganistão", "Cabul", 40.2 milhões, 652.230 km², ["Paquistão", "Irã", "Tajiquistão", "Uzbequistão"], "Ásia"),
    ("França", "Paris", 67.2 milhões, 551.500 km², ["Alemanha", "Bélgica", "Luxemburgo", "Itália", "Suíça", "Andorra", "Monaco", "Reino Unido", "Países Baixos", "Marrocos"], "Europa"),
    ("Somália", "Mogadíscio", 15.6 milhões, 637.657 km², ["Etiópia", "Quênia", "Djibouti", "Iêmen"], "África"),
    ("República Centro-Africana", "Bangui", 4.7 milhões, 622.984 km², ["Chade", "Sudão", "Congo", "República Democrática do Congo"], "África"),
    ("Sudão do Sul", 12.3 milhões, 644.329 km², ["Sudão", "Uganda", "Quênia", "República Democrática do Congo"], "África"),
    ("Ucrânia", "Kiev", 43.1 milhões, 603.628 km², ["Rússia", "Belarus", "Polônia", "Romênia", "Hungria", "Moldávia"], "Europa"),
    ("Botswana", "Gaborone", 2.4 milhões, 582.040 km², ["Namibia", "Zâmbia", "África do Sul"], "África"),
    ("Madagascar", "Antananarivo", 27.4 milhões, 587.041 km², ["Seicheles", "Comores", "Mianmar", "Tanzânia"], "África"),
    ("Quênia", 53.0 milhões, 580.367 km², ["Somália", "Sudão do Sul", "Uganda", "Tanzânia", "África do Sul"], "África"),
    ("Iêmen", 29.3 milhões, 527.970 km², ["Arábia Saudita", "Omã", "Eritreia", "Somália"], "Ásia"),
    ("Tailândia", "Banguecoque", 69.2 milhões, 513.120 km², ["Laos", "Mianmar", "Camboja", "Malásia"], "Ásia"),
    ("Espanha", "Madrid", 47.3 milhões, 505.990 km², ["França", "Portugal", "Marrocos", "Grécia", "Andorra", "Gibraltar"], "Europa"),
    ("Turcomenistão", "Asgabate", 6.1 milhões, 491.210 km², ["Afeganistão", "Irã", "Uzbequistão", "Cazaquistão"], "Ásia"),
    ("Camarões", 26.5 milhões, 475.442 km², ["Nigéria", "Chade", "República Centro-Africana", "Gana", "Guiné Equatorial", "República Democrática do Congo", "Gabão"] , "África")

]
Poderia me gerar um comando de insert no postgres para inserir 10 carros da montadora tesla na seguinte tabela?

CREATE TABLE IF NOT EXISTS carros (
    id SERIAL PRIMARY KEY,
    montadora_id INTEGER REFERENCES montadoras(id) ON DELETE CASCADE,
    modelo VARCHAR(50),
    ano_inicio_fabricacao VARCHAR(50),
    ano_final_fabricacao VARCHAR(50),
    valor_medio em REAL
);