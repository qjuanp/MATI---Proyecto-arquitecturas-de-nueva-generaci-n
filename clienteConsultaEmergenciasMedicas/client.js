var reportarEstadoDeLaPrueba = function (latency, result) {
    console.log('Numero de requests generados ->', latency.totalRequests) 
}

var resultadoDeLaPrueba = function (error, result) {
    if(error)
        return console.error(error)
        
    console.table({
        'Escenario': 'Latencia',
        'Peticiones Totales': result.totalRequests,
        'Tiempo promedio de Respuesta (Entre 200 y 500 milisegundos)': result.meanLatencyMs,
        'Peticiones por segundo': result.rps        
    })
}

var run = require('loadtest')
require('console.table')

var pruebaDeLatencia = {
    url : 'http://172.28.128.35:8000/emergenciasMedicas?longitudDesde=-74.261789&longitudHasta=-73.936241&latitudDesde=4.498841&latitudHasta=4.969203',
    concurrency: 1,
    maxRequests: 100,
    statusCallback: reportarEstadoDeLaPrueba
}

var pruebaDeEscalabilidad = {
    url : 'http://172.28.128.35:8000/emergenciasMedicas?longitudDesde=-74.261789&longitudHasta=-73.936241&latitudDesde=4.498841&latitudHasta=4.969203',
    concurrency: 50,
    maxRequests: 200,
    statusCallback: reportarEstadoDeLaPrueba
}

run.loadTest(pruebaDeLatencia, resultadoDeLaPrueba)
run.loadTest(pruebaDeEscalabilidad, resultadoDeLaPrueba)