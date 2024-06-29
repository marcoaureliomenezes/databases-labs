




## Como optimizadores decidem usar o index


- Tabelas com muitos indexes.

QUERY: `SELECT * FROM table_name WHERE f1 = 1 AND f2 = 4;`


#### Caso 1

Optimizer decide não usar nenhum index.
Exemplo: Busca irá retornar tantas linhas que é mais rapido fazer um `Full table Scan`.

#### Caso 2

- Optimizer decide usar somente 1 index.
- Exemplos: 
    - Busca é com AND e uma das colunas é Priamry Key (Valores únicos).
    - Busca pelo primeiro campo no index, busca linhas no HEAP e filtra por segundo campo.


#### Caso 3

- Optimizer decide usar os 2 indexes.
- Exemplos: 
    - Busca paralela é feita nos 2 indexes e rows são mergeadas (intersceção para AND e união para OR).
    - Dataset é de tamanho médio.



### Criação de Indexes em PROD


- Bloqueia INSERTs
- Solução: CREATE CONCURRENTLY index_name ON table_name(name);
- Como lado negativo demora mais e consome mais recursos.


### Bloom Filters


Username existe?

Cache


## B-Trees Indexes


Full table Scan: 

