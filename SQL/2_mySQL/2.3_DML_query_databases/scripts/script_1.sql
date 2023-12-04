USE sucos_vendas;

DESCRIBE itens_notas_fiscais;

SELECT * FROM itens_notas_fiscais;
SELECT NUMERO, CODIGO_DO_PRODUTO, QUANTIDADE, PRECO FROM itens_notas_fiscais;
SELECT NUMERO, CODIGO_DO_PRODUTO AS CODIGO, QUANTIDADE AS QTD, PRECO FROM itens_notas_fiscais;


SELECT * FROM tabela_de_produtos;
SELECT * FROM tabela_de_produtos WHERE CODIGO_DO_PRODUTO = '1000889';
SELECT * FROM tabela_de_produtos WHERE SABOR = 'Laranja';

SELECT * FROM tabela_de_produtos WHERE PRECO_DE_LISTA BETWEEN 19.49 AND 19.51;




