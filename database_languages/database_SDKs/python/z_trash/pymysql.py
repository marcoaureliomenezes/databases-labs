import pymysql

# Conectar ao banco de dados

class PyMySQL:

    def __init__(self, host, user, password, database):
        connection_data = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

    def connect(self, add_configs={}):
        self.connection = pymysql.connect(**self.connection_data, **add_configs)

    def disconnect(self):
        self.connection.close()

    def execute(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
            return cursor.fetchall()
        

    def insert(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
            return cursor.lastrowid
        

    def update(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
            return cursor.rowcount
        
    def delete(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
            return cursor.rowcount
        

if __name__ == '__main__':
    add_configs = {'cursorclass': pymysql.cursors.DictCursor}
    db = PyMySQL('seu_host', 'seu_usuario', 'sua_senha', 'seu_banco_de_dados').connect(add_configs)
    resultados = db.execute("SELECT * FROM sua_tabela")
    for linha in resultados:
        print(linha)
    db.disconnect()





