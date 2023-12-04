CREATE DATABASE IF NOT EXISTS vendas_sucos;
USE vendas_sucos;

CREATE TABLE IF NOT EXISTS produtos 
(
    CODIGO VARCHAR(10) NOT NULL,
    DESCRITOR VARCHAR(100) NULL,
    SABOR VARCHAR(50) NULL,
    TAMANHO VARCHAR(50) NULL,
    EMBALAGEM VARCHAR(50) NULL,
    PRECO_LISTA FLOAT NULL,
    PRIMARY KEY (CODIGO)
);

CREATE TABLE IF NOT EXISTS vendedores
(
    MATRICULA VARCHAR(5) NOT NULL,
    NOME VARCHAR(100) NULL,
    BAIRRO VARCHAR(50) NULL,
    COMISSAO FLOAT NULL,
    DATA_ADMISSAO DATE NULL,
    FERIAS BIT(1) NULL,
    PRIMARY KEY (MATRICULA)
);

CREATE TABLE IF NOT EXISTS notas
(
    NUMERO VARCHAR(5) NOT NULL,
    DATA_VENDA DATE NULL,
    CPF VARCHAR(11) NOT NULL,
    MATRICULA VARCHAR(5) NOT NULL,
    IMPOSTO FLOAT NULL,
    PRIMARY KEY (NUMERO)
);

CREATE TABLE IF NOT EXISTS clientes
(
    CPF VARCHAR(11) NOT NULL,
    NOME VARCHAR(100) NULL,
    ENDERECO VARCHAR(50) NULL,
    BAIRRO VARCHAR(50) NULL,
    CIDADE VARCHAR(50) NULL,
    ESTADO VARCHAR(50) NULL,
    CEP VARCHAR(8) NULL,
    DATA_NASCIMENTO DATE NULL,
    IDADE TINYINT NULL,
    SEXO VARCHAR(1) NULL,
    LIMITE_CREDITO FLOAT NULL,
    VOLUME_COMPRA FLOAT NULL,
    PRIMEIRA_COMPRA BIT(1) NULL,
    PRIMARY KEY (CPF)
);

CREATE TABLE IF NOT EXISTS itens_notas
(
    NUMERO VARCHAR(5) NOT NULL,
    CODIGO VARCHAR(10) NOT NULL,
    QUANTIDADE INT,
    PRECO FLOAT,
    PRIMARY KEY (NUMERO, CODIGO)
);


# ALTER TABLE notas ADD CONSTRAINT FK_CLIENTES FOREIGN KEY (CPF) REFERENCES CLIENTES (CPF);
# ALTER TABLE notas ADD CONSTRAINT FK_VENDEDORES FOREIGN KEY (MATRICULA) REFERENCES VENDEDORES (MATRICULA);
# ALTER TABLE itens_notas ADD CONSTRAINT FK_NOTAS FOREIGN KEY (NUMERO) REFERENCES NOTAS (NUMERO);
# ALTER TABLE itens_notas ADD CONSTRAINT FK_PRODUTOS FOREIGN KEY (CODIGO) REFERENCES PRODUTOS (CODIGO);


