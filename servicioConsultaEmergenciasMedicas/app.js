var bodyParser = require('body-parser');
var dateParser = require('express-query-date')
var express = require('express')
var app = express()
var emergenciasMedicas = require('./lib/consultaEmerfenciasMedicas')

emergenciasMedicas(app)

app.use(bodyParser.json());
app.use(dateParser());

app.listen(8000, function () {
    console.log("Ready!")
})