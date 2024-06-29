const app = require('express')();
const {Client} = require('pg');
const crypto = require('crypto');
const ConsistentHash = require('consistent-hash');

const hr = new ConsistentHash();
hr.add('5432');
hr.add('5433');
hr.add('5434');


const client = {
    "5432": new Client({
        "host": "localhost",
        "port": "5432",
        "user": "postgres",
        "password": "pass_123",
        "database": "postgres"
    }),
}

async function connect() {
    await client["5432"].connect();
    await client["5433"].connect();
    await client["5434"].connect();
    await app.listen(3000);
}

app.get('/', (req, res) => {

})


app.post('/', (req, res) => {
    const url = req.query.url;("sha256").update(url).digest("hex");
    const hash = crypto.createHash
    

})