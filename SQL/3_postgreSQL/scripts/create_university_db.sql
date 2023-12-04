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


CREATE TABLE curso (
	id SERIAL,
	nome VARCHAR(255),
	id_disciplinas: INTEGER,
	id_departamento: INTEGER,
	id_aluno INTEGER,
	carga_horaria: INTEGER,
	duracao_normal: INTEGER,
	duracao_maxima INTEGER,
);

CREATE TABLE disciplina (
	id SERIAL,
	nome VARCHAR(50),
	descricao TEXT,
	id_tematica INTEGER,
	id_curso INTEGER,
	id_aluno INTEGER
	nota_minima NUMERIC(4,2),
	nota_maxima NUMERIC(4,2),
	media_aprovacao NUMERIC(4,2),
	esta_ativa BOOLEAN
);

CREATE TABLE professor (
	id SERIAL,
	nome VARCHAR(255),
	grau_formacao VARCHAR(30),
	data_admissao DATE,
	cpf VARCHAR(11),
	id_disciplinas INTEGER,
	id_departamento INTEGER,
	salario:  NUMERIC(10, 2),
	carga_horaria: INTEGER,
	horario_inicio TIME,
	horario_fim TIME,

	ativo BOOLEAN,
);

CREATE TABLE aula (
	id_aula SERIAL,
	nome VARCHAR(255),
	semestre: INTEGER
	carga_horaria: INTEGER,
	horario_inicio TIME,
	horario_fim TIME,
	id_aulas_curso_id
	id_professor INTEGER,
	id_aula_aluno INTEGER,
	ativo BOOLEAN,
);