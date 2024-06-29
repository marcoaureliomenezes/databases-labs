# Cassandra

## Introdução

- Criado pelo facebook e Open Source;
- Distribuido e descentralizado;
- Elastically scalable;
- Sempre disponivel e com consistência configurável;
- Tolerante a falhas;
- Alta throughput para escrita;
- Rápido e escalável linearmente;
- Support em data center multiplos.
- Linguagem de queries amigável ao SQL.

- `MongoDB`:
    - Seach sue cases, ecommerce websites.
    - Read with indexes.
    - Consistency
    - Primary-Secondary architecture


- `Apache Cassandra`:
    - "Always available" type of services (Netflix, Spotify)
    - Fast Writes - capture all data
    - Availability and scalability


- Não é um substituto imediato para bancos de dados relacinais.

    - Não suporta JOINs
    - Suporte limitado a agregações
    - Suporte limitado a transações
    - Para JOINs e aggregações utilizar `Cassandra + Spark`.

### Cenários de uso

- Quando número de escritas é maior do que de leituras.
    - Exemplo: Guardar todos os clicks de um site.
    - Guardar todos os logs de tentativas de acesso a um serviço.

- Quando dados são frequentemente inseridos mas raramente atualizados ou deletados.
- Quando é possível pre-definir e acesso aos dadospor uma chave primária conhecida.
    - Dados podem ser particionados via uma chave que permite ao database espalhar esses dados por todo cluster

- Seguir atividade de usuário em uma aplicação.
- Series temporais
    - Monitoramento logs de acesso em servidores.
    - Dados de dispositivos IoT.
- eCommerce websites:
    - Interaçoes por click para prever comportamento do cliente.
    - Status de pedidos e transações de usuários.


## Arquitetura do Cassandra


- Projetada para prover escalabilidade, disponibilidade, confiabilidade e armazenar quantidades massivas de dados.

- Arquitetura de sistemas distribuidos.
- Cada instancia do apache Cassandra é denominada um nó
- Arquitetura em anel.
- Todos os nós do cluster são iguais.
- Projetado para topologia de rede Peer-to-Peer.
- Qualquer nó pode performar operações no database e servir requisições de clientes
- Não há a necessidade de um nó primário.

- Gossip é um protocolo usado pelo Cassandra para comunicação P2P.

- Multi Data Center Deployment

Componentes de um no cassandra

- **Memtable**: 
    - Estruturas em memória onde o cassandra faz buffers de escrita. 
    - Em geral existe 1 Memtable ativa por tabela.

- **CommitLog**: 
    - Append-only logs de todas as mutações locais de um nó Cassandra. 
    - Provê durabilidade em casos de cashes no servidor. 
    - Após o servidor reiniciar qualquer mutação será escrita na Memtable.

- **SSTables**:
    - Arquivos imutáveis que o Cassandra usa pra persistir dados no disco.
    - SSTables são escritas no disco a partir de Memtables ou de strems vindo de outros nós.
    - Cassandra faz compactação para combinar multiplas SSTables e sumente uma.
    - Uma vez que uma nova SSTable foi escrita, velhas SSTables são deletadas.
    - Cada SSTable é comprimida de multiplos componentes guardados em diferentes arquivos, tais como
        - `Data.db`: The actual data.
        - `Index.db`: An index partition keys to positions in the Data.db file
        - `Summary.db`: Uma amostra de (por padrão) toda 128º entrada no arquivo Index.db.
        - `Filter.db`: Um Bloom filter das chaves de partição na tabela
        - `CompressionInfo.db`: Metadados sobre os offsets e tamanhos de compression chuncks no arquivo Data.db.


## Processo de escrita a nível de Nó


## Processo de leitura a nível de Nó


## Cassandra Data Model

### Tabelas

- Entidade lógica que organiza dados a nível de nó ou de cluster.
- Dados são organizados em tabelas contendo linhas de colunas
- Tabelas podem ser criadas, dropadas, alteradas em tempo de execução sem bloquear updates e queries.
- Para criar uma tabela é preciso definir uma chave primária e outros dados das colunas.



### Keyspaces

- Entidade lógica que contém 1 ou mais tabelas
- Replicação e distribuição entre data centers é feita nível de Keyspace.
- Recomendado 1 keyspace por aplicação

### Primary KEy

- Sub grupo de colunas declaradas
- Mandatório (não é possível alterar uma vez que declarado).
- 2 papeis principais:
    - Optimizar performance de leitura para queries na tabela. Query Driven table system.
    - Provê unicidade às entradas.
- 2 componentes principais:
    - Chave de Partição ou Partition Key (Obrigatório).
    - Clustering Key (Optional).

### Partition Key

Partition Key => Hash (token) => Node.
Partition Key determina os dados localmente no cluster.
- Dados com uma chave de partição específica estão sempre no mesmo nó.
- Podem haver réplicas dos dados da chave partição em outros nós.


### Clustering Key

- Guarda dados ordenados de forma ascendente ou descendente com a partição para queries rápidas de valores similares.
- Uma ou multiplas colunas podem ser clustering keys.
- Completa a chave primária de uma tabela dinâmica.

### Data Modeling

- Criar chaves primárias que otimizam queries.
- Escolher uma chave de partição que começa a resolver a query e espalha uniformemente pelo cluster.
- Minimizar o numero de partições lidas para responder a uma query.




### Tipos de tabelas


- **Static Tables**:  PRIMARY KEY (username). Não contém Clustering Keys.
- **Dynamic Tables**: PRIMARY KEY ((groupid), username)

## CQL - Cassandra Query Language


- **Create Namespace**: `CREATE KEYSPACE keyspace_name WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'replication_factor': 3 };`
- **Modify Namespace**: `ALTER KEYSPACE keyspace_name WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'replication_factor': 3 };`
- **Create Table**: `CREATE TABLE tablename ();`
- **Insert Data**: `INSERT INTO table_name (col_1, col_2, ...) VALUES (val_1, val_2, val_n)...`
- **Update Data**: `UPDATE table_name SET col_target = new_value WHERE col_cond = value_cond`
- **Delete Data**: `DELETE FROM tablename WHERE col_cond = value_cond`
- **Drop table**: `DROP TABLE table_name;`

#### Observações

- Não case-sensitive
- Não suporta JOINs
- 

####Como executar queries no cassandra:

- Usando Cassandra Client Drivers. Default = open source Datastax Java Driver.
- Usando CQLSH client: Python-based CLI em shell para interagir com Cassandra usando CQL.
- Outros CQL editores disponíveis tais como 


--help
--version

-p -password
-k -keyspace
-u -user

CAPTURE
CONSISTENCY
COPY TO: Export table to a CSV
COPY FROM: Import table
DESCRIBE
EXIT
PAGING
TRACING

Tunnable consistent: Set consistency.

Comando laboratorio cassandra

- show host
- describe keyspaces
- cls
- 

### DDL


#### Built-in Datatypes

- ASCII
- Boolean
- Int:  Usado para inteiros de 64 bits.
- Bigint: Usado para inteiros de 64 bits.
- Decimal
- Double
- Float
- Varchar: Usado para representar strings. Representa strings encoded com UTF-8
- Blob: Bytes arbitrários. Indicado para guardar pequenas imagens ou strings curtas (1MB)
- Text: 
- Uuid
- Timestamp
- Timeuuid

#### Collection Data types

Adequado para uma lista limitada.

- Lists: Coleção de um ou mais elementos. `list<txt>`

`UPDATE table_name SET col_list = ['new_item'] + col_list WHERE col_name = 'col_value';`
`UPDATE table_name SET col_list = col_list + ['new_item'] WHERE col_name = 'col_value';`
`UPDATE table_name SET col_list[0] = 'new_item' WHERE col_name = 'col_value';`

- Maps: Coleção chave valor.
- Sets: Coleção de elementos unicos.


#### User-defined datatype


#### Keyspaces 

- Uma keyspace precisa ser criada antes de criar tabelas.
- Keyspaces contem qualquer número de tabelas.
- Uma tabela pertence somente a um keyspace.
- Replicação é definida a nivel de keyspace.
- É preciso especificar um fator de replicação no momento de criação do keyspace.


- Replication Factor: Número de réplicas colocadas em diferentes nós.
- Replication Strategy: Quais nós irão hospedar réplicas.

Observações:

- Todas as réplicas tem a mesma importância
- Fator de replicação não deve exceder numero de nós no cluster.



### DML





