# Modelagem de dados


## Modelo conceitual ou Modelo Domínio

- Entendimento dos requisitos do sistema;
- Representação visual;
- Fundamental para todos que trabalham com dados.

## Modelagem lógica

 É criada para realizar a descrição de como os dados serão armazenados no sistema. 
 Explora os conceitos de domínio. Nesse tipo de modelo são descritas:
 - entidades; 
 - atributos;
 - chaves primárias e estrangeiras e os seus relacionamentos.

## Modelagem Física

 - É criado para descrever as tabelas, suas colunas e os relacionamentos. 
 - Diferente do modelo lógico, podemos utilizar uma linguagem padrão para realizar essa representação.
 - A linguagem SQL, utilizada para trabalhar com banco de dados relacionais.


## SGBD - Sistema de Gerenciamento de Bando de dados 

Os SGBDs ou DBMS (Database Management System);
Interfaace para incluir, alterar ou ou consultar;

- MySQL;
- PostgreSQL;
- Oracle;
- MariaDB;
- Miscrosoft SQL Server;
- SQLite;



mini mundo

Clube do livro


Relacionamentos

- Relacionamento Binário
- Relacionamento Ternário
- Relacionamento n-ário

### Cardinalidade

1 -> 1

1 -> N

N -> N

## MER (Modelo Entidade Relacionamento)

- Modelo conceitual
- Usado para descrever entidades, suas caracteristicas e como se relacionam
- Forma abstrata.

## DER (Diagrama Entidade Relacionamento)

- Representação gráfica do MER.
- Software _brModelo;


Entidade associativa

# Modern Data Modeling



**Entidade clientes**

- Entidade Forte
- Atributos
    - tipo_pessoa
    - CPF
    - RG
    - CNPJ
    - IE
    - Endereco,
    - telefone
    - email

**Entidade livros**

- Entidade Fraca (Depende da editora)
- atributos:
    - titulo
    - categoria
    - ISBN
    - ano publicação
    - valor
    - editora
    - autor

**Entidade editora**

- Entidade Forte
- Atributos:
    - telefone_editora
    - nome_contato
    - email_contato

**Entidade Pedido**

- Entidade fraca (Depende de livro)
- Atributos:


**Entidade Estoque**
- Entidade fraca (Depende de livro)
- Atributos:

PS: 

- Cada livro deve estar relacionado a somente 1 editora
- Cliente pode comprar 1 ou mais livros em um pedido. 
## Entidades

- Entidade Forte
    - Existe independentemente de outras entidades.
    - 
- Entidade Fraca




## Modelo Banco de dados Universidade




Cardinalidade


## Data Base Modeling

### Relacionamentos

Os relacionamentos entre entidades (tabelas) pode ser feita de 4 maneiras distintas:
- 1:1
- 1:n
- n:1
- n:n

#### Relacionamento 1:1

Exemplos:

- Navio <-> Capitão
- Empresa <-> CEO
- Pais <-> Presidente
- Cidade <-> Prefeito
- Pessoa <-> Habilitação

#### Relacionamento n:n

Exemplos:

- Estudante <-> Aulas
- Sprints <-> Engenheiros
- Jogadores <-> Partidas de futebol
- Filmes <-> Atores
- Reuniões de trabalho <-> Funcionários

### Chaves primárias e estrangeiras

Chave privada: 

Chave estrangeira: 


### Consistencia de dados

**Situação:**

Dadas 2 tabelas, `livros` e `autores` com relacionamento 1:n:
- tabelas livros e autores possuem chaves primárias chamadas `id`.
- tabela livros possui a chave estrangeira chamada `autor_id`.

Casos que demonstram consistência:

**3 Cenários de consistência para inserção**

- Inserção de chave estrangeira que existe como chave primária na tabela 1: Funciona OK.
- Inserção de chave estrangeira como NULL: Funciona OK.
- Inserção de chave estrangeira que não existe como chave primária na tabela 1: Retorna ERRO! Foreign Key constraint.






