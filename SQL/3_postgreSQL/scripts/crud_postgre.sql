CREATE TABLE aluno (
	id SERIAL,
	nome VARCHAR(255),
	cpf CHAR(11),
	id_curso INTEGER,
	observacao TEXT,
	valor_mensalidade NUMERIC(10, 2),
	media_notas REAL,
	ativo BOOLEAN
);

INSERT INTO aluno (nome, cpf, id_curso, observacao, valor_mensalidade, media_notas, ativo)
VALUES
	('Marco Menezes', '12345678901', 5, 'Muito pensativo', 0, 4.7, TRUE),
	('Felipe Etrusco', '12345678900', 1, 'Muito criativo', 0, 3.7, FALSE),
	('Rosemberg Farias', '10987654321', 4, 'Muito crânio', 0, 7.2, TRUE);


UPDATE aluno SET media_notas = 8 WHERE id = 1;
DELETE FROM aluno WHERE id = 2;
SELECT * FROM aluno;

DELETE FROM aluno WHERE TRUE;
DROP TABLE aluno;
