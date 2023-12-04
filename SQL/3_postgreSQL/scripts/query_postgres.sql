




CREATE TABLE IF NOT EXISTS aluno (
	id INTEGER PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	cpf CHAR(11) NOT NULL,
	id_aluno_curso INTEGER,
	observacao TEXT,
	media_notas REAL,
	cotista BOOLEAN,
	ativo BOOLEAN
);


CREATE TABLE IF NOT EXISTS aluno_curso (
	aluno_id INTEGER,
	curso_id INTEGER,
	data_matricula DATE,
	PRIMARY KEY(aluno_id, curso_id),
	FOREIGN KEY (aluno_id) REFERENCES aluno (id),
	FOREIGN KEY (curso_id) REFERENCES curso (id)
);


CREATE TABLE IF NOT EXISTS curso (
	id INTEGER PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	id_aluno INTEGER
);

INSERT INTO aluno (nome, cpf, semestro_inicio, id_curso, observacao, valor_mensalidade, media_notas, ativo)
VALUES
	('Marco Menezes', '12345678901', '09.2', 5, 'Muito pensativo', 0, 8.7, TRUE),
	('Erick Guedes', '12345678902', '12.1', 5, 'Muito quieto', 0, 8.2, TRUE),
	('Marcelo Hamanaka', '12345678903', '12.1', 5, 'Muito esperto', 0, 7.2, TRUE),
	('Rosemberg Farias', '12345678904', '12.2', 4, 'Muito pensativo', 0, 6.2, TRUE),
	('Jade Ferreira', '12345678905', '12.2', 4, 'Muito assidua', 0, 6.5, TRUE),
	('Felipe Etrusco', '12345678906', '13.1', 1, 'Muito crânio', 0, 7.2, FALSE),	
	('Korahi Ferreira', '12345678907', '14.2', 1, 'Muito pensativo', 0, 6.1, TRUE),
	('Alecio Schetino', '12345678908', '13.1', 1, 'Muito sagaz', 0, 8.2, FALSE),
	('Felipe Moreira', '12345678909', '12.1', 3, 'Muito manso', 0, 7.8, TRUE),
	('Rildo Magalhães', '12345678910', '10.2', 3, 'Muito inteligente', 0, 7.3, TRUE),
	('Tauan Miranda', '12345678911', '10.1', 3, 'Muito chilele', 0, 3.7, FALSE),
	('Tauan Miranda', '12345678912', '14.2', 1, 'Muito chilele', 0, 8.1, FALSE),
	('Andre Nogueira', '12345678913', '08.2', 4, 'Muito sabio', 0, 6.5, TRUE);


SELECT * FROM aluno;

SELECT * FROM aluno WHERE ativo IS TRUE;
SELECT * FROM aluno WHERE ativo IS NOT TRUE;

SELECT * FROM aluno WHERE nome = 'Marco Menezes';
SELECT * FROM aluno WHERE nome <> 'Marco Menezes';
SELECT * FROM aluno WHERE media_notas >= 6;
SELECT * FROM aluno WHERE media_notas < 6;
SELECT * FROM aluno WHERE nome LIKE 'Marco%';
SELECT * FROM aluno WHERE nome LIKE 'M_rco Menezes';
SELECT * FROM aluno WHERE media_notas BETWEEN 6 AND 10;
SELECT * FROM aluno WHERE id_curso IN (5, 4);



