# Databases Labs

This repo contains material collected and developed by me since I've started mu Database Studies. An important discovery that I've made during my studies about databases was that understanding some fundamental concepts, plus undersdanding the similarities between than, and how each one implement the fundamental concepts is a key. So, makes sense to create a central repository to store all the material. Then, while I'm organizing and improving this material, I'm also organizing this knowledge in my mind and providing a better way to access it. At some point it can be userful for others and also useful for me to produce some content, such as articles, videos, and more.

It's important to establish that It's a material in constant evolution, so I'm always updating and improving it with new concepts, languages and database flavors that I'm studying. Basically it contains:

- Markdown files where I firstly take notes while studying, in a raw manner. Then I keep improving these notes with time, studies, reflexions and improvements in the text.
- Dockerfiles and Docker Compose files to spin up some databases locally and in a simple way, in order to practice.
- Scripts in languages such as SQL to interact directly with databases. And also scripts in other languages, such as Python, Java, and more, to interact with databases using SDKs.

## 1. Repo structure

Here is the structure of the repository:

- **Data modeling**: This folder contains some data modeling theory texts and practical material and exercises.
- **Database Backend**: This folder contains low level information about databases, such as storage engines, indexing, query optimization and more.
- **database Flavors**: This folder contains specific information about some databases that I'm studying, such as Postgres, Mysql, ScyllaDB, Cassandra, Mongodb, and more.
- **Database Frontend**: This folder contains information about how to connect and interact with databases using SQL, SDKs in other languages, such as Python, Java, and more.
- **Database Seeders**: This folder contains some scripts to seed databases with some data, in order to practice some concepts and languages.
- **Docker**: Dockerfiles to build images on top of databases images with custom configurations and tools used to interact with databases.
- **Mount**: This folder is where I'm mounting the volumes to store the data of the databases that I'm spinning up.
- **Services**: Docker Compose files to spin up some databases and tools that I'm studying. The idea is to have a simple way to start a database and try some concepts and languages.

## 2. How to Spin Up the Environment

We use here Docker and Docker Compose to spin up the databases, associated with a Makefile to simplify the commands. Here are the steps to spin up the environment:

```bash

