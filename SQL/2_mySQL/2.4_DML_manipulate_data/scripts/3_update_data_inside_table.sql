USE vendas_sucos;

SELECT * FROM produtos;


UPDATE produtos SET PRECO_LISTA = 5 WHERE CODIGO = '1000889';

UPDATE produtos SET EMBALAGEM = 'PET', TAMANHO = '1 Litro', DESCRITOR = 'Sabor da Montanha - 1 Litro - Uva' WHERE CODIGO = '1000889';

UPDATE produtos SET PRECO_LISTA = PRECO_LISTA * 1.1 WHERE SABOR = 'Maracujá'; 


SELECT * FROM vendedores;

SELECT * FROM sucos_vendas.tabela_de_vendedores;

SELECT * FROM vendedores a
INNER JOIN sucos_vendas.tabela_de_vendedores b
ON a.MATRICULA = SUBSTRING(b.MATRICULA, 3, 3);


