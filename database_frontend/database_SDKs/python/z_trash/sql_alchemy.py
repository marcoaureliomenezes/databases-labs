from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class SQLAlchemy:

    def __init__(self, user, password, host, port, database):
        self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
        self.metadata = MetaData(bind=self.engine)

# Substitua "mysql+mysqlconnector://seu_usuario:senha@seu_host/seu_banco_de_dados" pelos seus próprios detalhes de conexão.
engine = create_engine("mysql+mysqlconnector://seu_usuario:senha@seu_host/seu_banco_de_dados")

# Crie uma classe modelo para representar sua tabela
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    idade = Column(Integer)

# Crie a tabela no banco de dados (se ainda não existir)
Base.metadata.create_all(engine)


# Criar uma instância da sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserir dados
nova_pessoa = Pessoa(nome='João', idade=25)
session.add(nova_pessoa)
session.commit()

# Consultar dados
pessoas = session.query(Pessoa).all()
for pessoa in pessoas:
    print(f'ID: {pessoa.id}, Nome: {pessoa.nome}, Idade: {pessoa.idade}')

# Fechar a sessão
session.close()