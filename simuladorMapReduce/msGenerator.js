module.exports = function service(options) {

  // Agrega la funcion para la generacion de informacion aleatoria:
  this.add({ type: 'msGenerator', function: 'generar'}, generar)

  // Funcion de generacion de informacion aleatoria
  function generar(msg, respond)
  {
    var index = msg.vars.index;
    var records = [];
    var iteraciones = 1;
    // 1. Timestamps:
    var timestampInicial = 1455883200; // 19-Febrero-2016 07:00 am
    var avanceTS = 900; // 15 minutos
    // 2. Coordenadas:
    var minLatitud = 4.515255;
    var minLongitud = 73.981249;
    var maxLatitud = 4.781818;
    var maxLongitud = 74.096605;
    var latitud;
    var longitud;
    var avanceCoo = 0.01;
    // 3. Contadores eventos:
    var minCEvento = 0;
    var maxCEvento = 20;
    var separador = '|';

    var tSI = timestampInicial; var tSF; var cP1La; var cP1Lo; var cP2La; var cP2Lo; var numEventos; var tempLat; var tempLong;
    for (var i = 0; i < iteraciones; i++) 
    {
      // Inserta el log del registro:
      records.push('Generando el registro: ' + index);
      // Genera la informacion del registro:
      tSI = timestampInicial + (avanceTS*(index-1));
      tSF = tSI + avanceTS;
      // Genera el punto aleatorio: P1
      latitud = (Math.random() * (maxLatitud - minLatitud) + minLatitud).toFixed(6);
      longitud = (Math.random() * (maxLongitud - minLongitud) + minLongitud).toFixed(6);
      tempLong = (longitud*-1).toFixed(6);
      cP1La = latitud;
      cP1Lo = tempLong;
      // Calcula los demas:
      // P2:
      //tempLong = ((parseFloat(longitud)-avanceCoo)*-1).toFixed(6);
      //cP2 = latitud + ',' + tempLong;
      // P3:
      //tempLat = (parseFloat(latitud)-avanceCoo).toFixed(6);
      //cP3 =  tempLat + ',' + (longitud*-1);
      // P4:
      tempLat = (parseFloat(latitud)-avanceCoo).toFixed(6);
      tempLong = ((parseFloat(longitud)-avanceCoo)*-1).toFixed(6);
      cP2La = tempLat;
      cP2Lo = tempLong;
      // Calcula los eventos:
      numEventos = Math.floor((Math.random() * maxCEvento) + 1);

      // Formatea el string final:
      records.push(tSI+separador+tSF+separador+cP1La+separador+cP1Lo+separador+cP2La+separador+cP2Lo+separador+numEventos+separador+numEventos+separador+numEventos);
    };

    // Estructura de la base de datos columnar en HBASE:
    // ----- Familia de Columnas: Información Básica -----
    // Timestamps Inicial|Timestamps Final|Coordenada P1-NOcc|Coordenada P2-Nor|Coordenada P3-SOcc|Coordenada P4-SOr
    // ----- Familia de Columnas: Info. Eventos Consolidados
    // Num Eventos Cardiacos Inusuales|Num Eventos Respiratorios Inusuales|Num Eventos Temperatura Inusuales
    // Ejemplo de registro: ----- Familia de Columnas: Información Básica -----
    // 19.02.2016.07:00 am|19.02.2016.07:05 am|
    // Aumenta de a 900 (15 minutos)|P1: Normal|P2: Dec.Long de P1 en 0.01|P3: Dec. Lat de P1 en 0,01|P4 Dec. Long de P3 en 0,01
    // 1455883200|1455883500|4.781818, -74.096605|4.781818, -74.086605|4.771818, -74.096605|4.771818, -74.086605
    // Ejemplo de registro: ----- Familia de Columnas: Info. Eventos Consolidados -----
    // 3 (0-100) | 3 (0-100) | 5 (0-100)

    respond( null, { respond: records });
  }

}
