# Controle de concorrencia

- Objetivo de garantir consistência


### Exclusive Locks

- Operações: Leitura e escrita.
- Impede modificação e leitura do dado.
- Garante 1 transação por vez


### Shared Locks or Read Locks

- Operações: Leitura
- Impede modificação do dado.
- Torna leituras consistentes.
- Pode ser cumulativo.


### Dead Locks

Transações fazem lock


- O ultimo a entrar em Dead Lock falha.
BEGIN 2 transactions

Quando ocorre o Dead Lock

- Em Tx-1 insere-se linha (1, 'Marco') sendo 1 valor PK.
- Em Tx-2 insere-se

INSERT INTO test VALUES (20);


t2

INSERT INTO test VALUES (21);
INSERT INTO test VALUES (20);

### Two Fase Locks


Marcar poltronas duplicadas de onibus ao mesmo tempo.


Leitura para ver se Poltrona está ocupada.

    SELECT * FROM seats WHERE id = 14 for update;

Atualização de poltrona para estado de ocupado









