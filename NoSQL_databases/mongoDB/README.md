Commands


### Creating Databases and Collections
- show databases;
- use `database_name`;
- db.createCollection("`collection`")
- db.`collection`.drop()
- db.dropDatabase()

### Insering documents into collection

- db.`collection`.insertOne({`obj`})
- db.`collection`.insertMany([{`obj_1`}, {`obj_2`}])

### Querying documents from collections

- db.`collection`.find(`filter`, `projection`)

- db.`collection`.find(
    {`field_1`: `value_1`, `field_2`: { $gt: `value_2` } },
)

- db.`collection`.find(
    {},
    {`field_1`: 1, `field_2`: 1, `field_3`: 0}
)

- db.`collection`.find().sort("`field_1`: 1, `field_2`: -1)

### Updating documents:

#### Templates

- **ReplaceOne**: db.`collection`.replaceOne(`filter`, `replacement`)
- **updateOne**: db.`collection`.updateOne(`filter`, `update`)
- **updateMany**: db.`collection`.updateMany(`filter`, `update`)
- **deleteOne**: db.`collection`.deleteOne({`cond_delete`})
- **deleteMany** db.`collection`.deleteMany({`cond_delete`})


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





