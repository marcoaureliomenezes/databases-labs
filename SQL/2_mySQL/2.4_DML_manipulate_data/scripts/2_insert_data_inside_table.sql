USE vendas_sucos;

INSERT INTO produtos (CODIGO, DESCRITOR, SABOR, TAMANHO, EMBALAGEM, PRECO_LISTA)
VALUES ('1040107', 'Light - 350 ml - Melância', 'Melância', '350 ml', 'Lata', 5.78);

INSERT INTO produtos (CODIGO, DESCRITOR, SABOR, TAMANHO, PRECO_LISTA)
VALUES ('1040108', 'Light - 350 ml - Laranja', 'Laranja', '350 ml', 5.78);

INSERT INTO produtos (CODIGO, DESCRITOR, SABOR, TAMANHO, EMBALAGEM, PRECO_LISTA)
VALUES
	('1040109', 'Normal - 350 ml - Melância', 'Melância', '350 ml', 'Lata', 5.16),
	('1040110', 'Normal - 350 ml - Laranja', 'Laranja', '350 ml', 'Lata', 5.16);


INSERT INTO clientes (CPF, NOME, ENDERECO, BAIRRO, CIDADE, ESTADO, CEP, DATA_NASCIMENTO, IDADE, SEXO, LIMITE_CREDITO, VOLUME_COMPRA, PRIMEIRA_COMPRA)
VALUES
	('1471156710', 'Érica Carvalho', 'R. Iriquitia', 'Jardins', 'São Paulo', 'SP', '80012212', '1990-09-01', 27, 'F', 17000, 24500, 0),
    ('19290992743', 'Fernando Cavalcante', 'R. Dois de Fevereiro', 'Água Santa', 'Rio de Janeiro', 'RJ', '80012212', '2000-02-12', 18, 'M', 100000, 20000, 1),
    ('2600586709', 'César Teixeira', 'Rua Conde de Bonfim', 'Tijuca', 'Rio de Janeiro', 'RJ', '22020001', '2000-03-12', 18, 'M', 120000, 22000, 0);


INSERT INTO produtos
SELECT CODIGO_DO_PRODUTO AS CODIGO, NOME_DO_PRODUTO AS DESCRITOR, SABOR, TAMANHO, EMBALAGEM, PRECO_DE_LISTA AS PRECO_LISTA
FROM sucos_vendas.tabela_de_produtos
WHERE CODIGO_DO_PRODUTO NOT IN (SELECT CODIGO FROM produtos);


SELECT * FROM produtos;

