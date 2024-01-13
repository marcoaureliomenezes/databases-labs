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


