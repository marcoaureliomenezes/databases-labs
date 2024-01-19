# Mongo DB Command Line Interface



## Comandos sobre Databases and Collections

- Mostrar databases disponíveis: `show databases` e `show dbs`;
- Usar um database específico: `use database_name`;
- Mostrar coleções dentro de um database: `show collections`;
- Criar uma coleção dentro de um database: `db.createCollection(collection_name)`;
- Deletando uma collection: `db.collection_name.drop()`;
- Deletando uma collection: `db.dropDatabase()`;

## CRUD no MongoDB (Create, Read, Update and Delete)

### CREATE: Inserindo documentos em uma coleção

- Inserindo um documento em uma coleção: `db.collection_name.insert_one({document})`;
- Inserindo muitos documentos em uma coleção:  `db.collection_name.insert_many([{document_1}, {document_2}, {document_3}])`;

### READ: Lendo documentos de uma coleção

- Lendo todos os documentos: `db.collection_name.find()`;
- Lendo todos os documentos com filtro: `db.collection_name.find({filter_condition})`;
- Lendo todos os documentos com projeção: `db.collection_name.find({}, {projection_definition})`;
- Lendo todos os documentos com filtro e projeção: `db.collection_name.find({filter_condition}, {projection_definition})`;

### UPDATE: Atualizando documentos de uma coleção:

- Atualizando um documento: `db.collection_name.replaceOne({filter}, {replacement})`
- Atualizando um documento: `db.collection_name.updateOne({filter}, {replacement})`
- Atualizando muitos documentos: `db.collection_name.updateMany({filter}, {replacement})`

### DELETE: Deletando documentos de uma coleção

- Deletando um documento: `db.collection_name.deleteOne({cond_delete})`;
- Deletando muitos documentos: `db.collection.deleteMany({cond_delete})`;


#### Examples:

- db.`collection`.updateOne({`cond_update`}, { $set: {"`field_1`": `new_value_1`, "`field_2`": `new_value_2`}})

- db.`collection`.updateMany({`cond_update`}, { $set: {"`field_1`": `new_value_1`, "`field_2`": `new_value_2`}})

- db.`collection`.deleteOne({`cond_delete`})

- db.`collection`.deleteMany({`cond_delete`})


**Documentos BSON**: Repressentação binária de JSON.

Tamanho máximo documento BSON: 16 MB


Importação de JSON e CSV

Consultas

- **FILTER**: Filtra documentos baseados em um condução.

- **PROJECT**: Indica campos a serem retornados na consulta. Ex: {`field_1`: 1, `field_2`: 0, `field_3`: 1}

- **SORT**: Ordena documentos baseados em uma coluna e uma ordem. Ex: {`field_1`: 1, `field_2`: -1}

- **COLLATION**: Ex: {locale: 'simple'}

- **MAX TIME MS**: Tempo de timeout que um query pode durar.


Operadores:

- **$eq**: equals.
- **$gt**: greater than.
- **$gte**: greater than or equals.
- **$lt**: less than.
- **$lte**: less than equals.
- **$ne**: not equals

- **$and**
- **$not**
- **$nor**
- **$or**
- **$in**
- **$all**
Example with Filter

- Filter: {$or: [{"`field_1`": `value_1`}, {"`field_2`": `value_2`}]}
- Filter: {"`field_1`": {$in [`value_1`, `value_2`]}}
- Filter: {"`field_1`": {$gt: `value_1`}}





