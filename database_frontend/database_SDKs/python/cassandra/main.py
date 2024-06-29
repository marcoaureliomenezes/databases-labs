from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)

session = cluster.connect("employee")

# Criar tabela de funcionarios

session.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id int PRIMARY KEY,
    name text,
    salary varint
)""")

# Inserir 5 linhas na tabela

session.execute("INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)", (1, "John", 10000))
session.execute("INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)", (2, "Mike", 20000))
session.execute("INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)", (3, "David", 30000))
session.execute("INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)", (4, "Peter", 40000))
session.execute("INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)", (5, "Julia", 50000))


print("START of simple query\n")
# Consultar dados na tabela

rows = session.execute("SELECT * FROM employee WHERE id IN (1,2)")
for row in rows:
    print(row)


print("\nEND of simple query\n")



# ESCRITA ASSINCRONA DE 5 LINHAS

future = session.execute_async("INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)", (7, "Julia", 50000))


# Prepared statement
    
prepared_statement = session.prepare("SELECT * FROM employee WHERE id=?")
employees_to_lookup = [1,2]

print("START of prepared query\n")
for employee_id in employees_to_lookup:
    employee = session.execute(prepared_statement, [employee_id]).one()
    print(employee)

print("\nEND of prepared query\n")