# CRUD com Flask e PostgreSQL
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from sqlalchemy import create_engine


# Criando a conexão com o banco de dados

postgres_config = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",
    "database": "tasks",
}

mysql_conf = ("localhost", "3306", "root", "root", "tasks")
pg_conf = ("localhost", "5432", "postgres", "postgres", "tasks")


mysql_url = f"mysql://{mysql_conf[2]}:{mysql_conf[3]}@{mysql_conf[0]}:{mysql_conf[1]}/{mysql_conf[4]}"
pg_url = f"postgresql://{pg_conf[2]}:{pg_conf[3]}@{pg_conf[0]}:{pg_conf[1]}/{pg_conf[4]}"

# Criando a conexão com o banco de dados
mysql_engine = create_engine(mysql_url)
pg_engine = create_engine(pg_url)

# Criando a tabela no banco de dados


app = Flask(__name__)

# Exemplo de dados para simular um banco de dados real
tasks = [
    {"id": 1, "description": "Aprender Databases", "done": False},
    {"id": 2, "description": "Aprender Flask", "done": True},
]


# Rota da página inicial
@app.route("/")
def index():
    return {
        "status": "success",
        "message": "Bem-vindo à API de tarefas do DADAIA",
    }

# Rota para listar todas as tarefas
@app.route("/tasks")
def get_tasks():
    print("UI")
    return {"status": "success", "data": tasks}


# Rota para listar uma tarefa específica
@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    return {"status": "success", "data": task[0]}

# Rota para criar uma nova tarefa
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.form
    data = dict(data)
    return {"status": "success", "message": "Tarefa criada com sucesso", "data": data}

# Rota para atualizar uma tarefa
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.form
    data = dict(data)
    return {"status": "success", "message": "Tarefa atualizada com sucesso", "data": data}

# Rota para deletar uma tarefa
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = [task for task in tasks if task["id"] == task_id]
    return {"status": "success", "message": "Tarefa deletada com sucesso", "data": task[0]}


if __name__ == "__main__":
    app.run(debug=True)