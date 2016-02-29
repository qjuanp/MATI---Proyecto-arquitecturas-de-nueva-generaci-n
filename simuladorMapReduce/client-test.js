var seneca = require('seneca')()

// Conexion a MongoDB:
seneca.use('mongo-store',{
	name: 'dbname',
	host: '172.28.128.15',
	port: 27017
})

var client = seneca.client({ host:'localhost', port:8080 })

function pause(segundos)
{
  setTimeout(continueExecution, segundos) // Espera n segundos
}
// --- pause()

function continueExecution()
{
   //finish doing things after the pause
   // Envia al topico de la generacion aleatoria y espera respuesta
	var iteraciones = 1; var index; var partes;
	for (var i = 0; i < iteraciones; i++) 
	{
		index = (i+1);
		client.act({ type: 'msGenerator', function: 'generar', vars:{"index":index}}, function (err, result)
		{
		  if (err)
		  {
		      console.error(err);
		  } 
		  else
		  {
		    var array = result.respond;
		    // Cada posicion del arreglo es un campo para el objeto JSON a meter en Mongo:
		    // 1. Inicializa la collecion:
		    var record = seneca.make$('emergenciasMedicasTest');
		    // 2. Asigna los diferentes atributos al objeto:
		    partes = array[0].split("|");
		    record.timeInicial = partes[0];
		    record.timeFinal = partes[1];
		    record.cP1La = partes[2];
		    record.cP1Lo = partes[3];
		    record.cP2La = partes[4];
		    record.cP2Lo = partes[5];
		    record.eventosC = partes[6]; // Eventos cardiacos
		    record.eventosR = partes[7]; // Eventos respiratorios
		    record.eventosT = partes[8];  // Eventos temperatura
		    // 3. Guarda el registro:
		    record.save$(function (err,record) 
		    {
			    console.log( "Registro creado exitosamente en MongoDB, con ID = "+record.id)
			})

		  }
		})
	};
}
// --- continueExecution()

// Ejecuta la funcion:
var numMilisegundos = 5000;
pause(numMilisegundos);







