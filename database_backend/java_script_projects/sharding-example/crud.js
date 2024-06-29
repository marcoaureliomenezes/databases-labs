const app = require('express')();
const {Client} = require('pg');
const ConsistentHash = require('consistent-hash');
const crypto = require('crypto');
const hr = new ConsistentHash();

hr.add("15432");
hr.add("15433");
hr.add("15434");


const clients = {
    "15432": new Client({
        "host": "localhost",
        "port": 15432,
        "user": "postgres",
        "password": "postgres",
        "database": "postgres"
    }),
    "15433": new Client({
        "host": "localhost",
        "port": 15433,
        "user": "postgres",
        "password": "postgres",
        "database": "postgres"
    }),
    "15434": new Client({
        "host": "localhost",
        "port": 15434,
        "user": "postgres",
        "password": "postgres",
        "database": "postgres"
    })   
}

async function connect() {
    await clients["15432"].connect();
    await clients["15433"].connect();
    await clients["15434"].connect();
}

connect();



app.get('/', (req, res) => {

});


app.post('/', (req, res) => {
    const url = req.body.url;
    const hash = crypto.createHash('sha256').update(url).digest('base64');
    res.send({
        "hash": hash,
        "url": url,
        "shard": hr.getNode(hash)
    });
});

app.listen(8081, () => {
    console.log("Server is listening on port 8081");
})