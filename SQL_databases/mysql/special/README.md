### COMMIT and ROLLBACK

**START TRANSACTION**:  Cria um ponto de estado do banco de dados.

**COMMIT**: Confirma todas as operações entre START TRANSACTION e o comando COMMIT. Persiste todos os INSERTs, UPDATEs e DELETEs.

**ROLLBACK**: Tudo que foi feito entre o START TRANSACTION e o comando ROLLBACK será desprezado e os dados voltarão ao status de quando o START TRANSACTION foi executado.



## 9 - Triggers

Um trigger (gatilho) é um tipo especial de stored procedure executado automaticamente quando ocorre um evento no servidor do banco de dados.

**Exemplo**: Ao incluir dados em uma tabela atualize um log com data e hora.


CREATE
    [DEFINER = user]
    TRIGGER `trigger_name`
    `trigger_time` `trigger_event`
    ON `tbl_name` FOR EACH ROW
    [`trigger_order`]
    `trigger_body`

**trigger_time**: { BEFORE | AFTER }
**trigger_event**: { INSERT | UPDATE | DELETE }
**trigger_order**: { FOLLOWS | PRECEDES } other `trigger_name`



## Stored Procedures











