const dotenv = require("dotenv")
dotenv.config()

db.createUser({
    user : process.env.DB_USERNAME,
    pwd : process.env.DB_PASSWORD,
    roles : [{role: "userAdminAnyDatabase" , db:"admin"}]
})

db.auth(process.env.DB_USERNAME,process.env.DB_PASSWORD)

db.createCollection("cnab")
