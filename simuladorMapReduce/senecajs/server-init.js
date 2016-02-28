var seneca = require( 'seneca' )()
  .use( require('./msGenerator.js') )
  .listen(8080)


var app = require( 'express' )()
    .use( require( 'body-parser' ).json() )
    .use( function(req, res, next) {
        res.header( "Access-Control-Allow-Origin", "*" );
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
    })
    .use(seneca.export('web'))
    .listen(9000,'0.0.0.0');
