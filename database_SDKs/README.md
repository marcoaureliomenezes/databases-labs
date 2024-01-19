



# SQL Alchemy ORM

## Criação de engine para diferentes bancos de dados

from sqlalchemy import create_engine


### 1 MySQL

O dialeto MySQL usa **mysqlclient** como database API padrão. Outros disponíveis são 

- string_connection = "mysql://user:tiger@localhost/foo"
The MySQL dialect uses mysqlclient as the default DBAPI. There are other MySQL DBAPIs available, including PyMySQL:

- string_connection = "mysql://`user`:`password`@`host`/`database_name`"
- string_connection = "mysql+mysqldb://`user`:`password`@`host`/`database_name`"
- string_connection = "mysql+pymysql://`user`:`password`@`host`/`database_name`"


### 2 - PostgreSQL

O dialeto PostgreSQL usa **psycopg2** como database API padrão. Outros disponíveis são pg8000 e asyncpg.

- string_connection = "postgresql://`user`:`password`@`host`/`database_name`"
- string_connection = "postgresql+psycopg2://`user`:`password`@`host`/`database_name`"
- string_connection = "postgresql+pg8000://`user`:`password`@`host`/`database_name`"


### 3 - Oracle SQL

O dialeto Oracle usa **cx_oracle** como database API padrão.

- string_connection = "oracle://`user`:`password`@`host`/`database_name`"
- string_connection = "oracle+cx_oracle://`user`:`password`@`host`/`database_name`"

### 4 - Microsoft SQL Server

O dialeto SQL Server usa **pyodbc** como database API padrão. Outra API padrão disponível é pymssql.

- string_connection = "mssql+pyodbc://`user`:`password`@`host`/`database_name`"
- string_connection = "mssql+pymssql://`user`:`password`@`host`/`database_name`"



### 5 - SQLite

SQLite
SQLite conecta a um database baseado em arquivos. Usa python o módulo builtin sqlite3 como padrão.
Como o SQLite conecta a arquivos locais, o formato da URL é ligeiramente diferente.
A porção file da URL é o nome do database. Para caminhos relativos use 3 barras (///).

- string_connection ="sqlite:///foo.db"

# sqlite://<nohostname>/<path>
# where <path> is relative:
