var MongoClient = require('mongodb').MongoClient

function filtrarEmergencias(rangoUbicaciones, rangoFechas, db, dbError,resultado) {
    var cursor = db
                    .collection('emergencias')
                    //.find()
                    .find({
                        "cP1La": { 
                            $gte: rangoUbicaciones.desde.latitud
                        },
                        "cP1Lo":{
                            $gte: rangoUbicaciones.desde.longitud
                        },
                        "cP2La": { 
                            $lte: rangoUbicaciones.hasta.latitud 
                        },
                        "cP2Lo":{
                            $lte: rangoUbicaciones.hasta.longitud
                        },
                        //"timeInicial":{
                        //    $gte: rangoFechas.desde.getTime()
                        //},
                        //"timeFinal":{
                        //    $lte: rangoFechas.hasta.getTime()
                        //}
                    })
    var emergencias = [];
    cursor.each(function (err, doc) {
        if(err)
            dbError(err)
        if(doc != null) emergencias.push(doc)
        else {
                resultado(emergencias)
            }
    })
}

function consulta(rangoUbicaciones, rangoFechas, error, resultados){
    MongoClient.connect('mongodb://192.168.99.100:27017/emergenciasMedicasTest', function (dbError,db) {
        if(dbError)
            error(dbError)
           
        filtrarEmergencias(
            rangoUbicaciones,
            rangoFechas,
            db,
            function(err){ error(err)},
            function (datos) {
                db.close()
                resultados(datos)
            })
    })
}

function resolverFecha(valor, valorPorDefecto) {
    if(valor === undefined) return valorPorDefecto;
    return new Date(valor);
}

function resolverFlotante(parametro, valorPorDefecto) { 
    if(parametro === undefined) return valorPorDefecto;
    return parseFloat(parametro.replace(",", "."));
}

module.exports = function name(app) {
    app.get('/emergenciasMedicas', function (req, res) {
        var rangoUbicaciones = {
            desde: {
                latitud : resolverFlotante(req.query.latitudDesde, -90.0),
                longitud : resolverFlotante(req.query.longitudDesde, -180.0),
            },
            hasta: {
                latitud : resolverFlotante(req.query.latitudHasta, 90.0),
                longitud : resolverFlotante(req.query.longitudHasta, 180.0),
            }
        }
        
        var rangoFechas = {
            desde: resolverFecha(req.query.fechaDesde,(function () {
                                                                var today = new Date();
                                                                today.setDate(today.getDate() - 1)
                                                                return today
                                                            })()),
            hasta : resolverFecha(req.query.fechaHasta, new Date())
        }
        
        //res.send()
        consulta(
            rangoUbicaciones, 
            rangoFechas,
            function (err) {
                res.status(500).send(err)
            },
            function (datos) {
                res.send(datos)
            })
    })
}