var MongoClient = require('mongodb').MongoClient;

function decimalAdjust(type, value, exp) {
// If the exp is undefined or zero...
    if (typeof exp === 'undefined' || +exp === 0) {
        return Math[type](value);
    }
    value = +value;
    exp = +exp;
    // If the value is not a number or the exp is not an integer...
    if (isNaN(value) || !(typeof exp === 'number' && exp % 1 === 0)) {
        return NaN;
    }
    // Shift
    value = value.toString().split('e');
    value = Math[type](+(value[0] + 'e' + (value[1] ? (+value[1] - exp) : -exp)));
    // Shift back
    value = value.toString().split('e');
    return +(value[0] + 'e' + (value[1] ? (+value[1] + exp) : exp));
}

if (!Math.round10) {
    Math.round10 = function(value, exp) {
        return decimalAdjust('round', value, exp);
    };
}

function randomIntFromInterval(min,max)
{
    return Math.round10(Math.random()*(max-min+1)+min,1);
}

var yourRandomGenerator = function(rangeOfDays,startHour,hourRange){
    var today = new Date(Date.now());
    return new Date(today.getYear()+1900,today.getMonth(), today.getDate()+Math.random() *rangeOfDays, Math.random()*hourRange + startHour, Math.random()*60)
}


function r(){
 MongoClient.connect("mongodb://localhost:3001/meteor", function(err, db) {
  if(err) { return console.dir(err); }

  db.collection('temperatures', function(err, collection) {
      console.log("Creating");
      for(var i = 0; i<=100; i++){
        console.log("Creating ",i);
          
        var t = {
            id : Math.floor((Math.random() * 10) + 1),
            tmp: randomIntFromInterval(20,60),
            ts: yourRandomGenerator(2,8,2)
        }
        console.log("Insert",t);          
        collection.insert(t);
      }
  });
});
}

setInterval(r,2400)
console.log("bye")