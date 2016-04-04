var Temperatures = new Mongo.Collection("temperatures");

if (Meteor.isClient) {
  Template.tempHistorySection.helpers({
    'temperatures': function () {
      return Temperatures.find({},{sort: {ts:-1},limit:20})
    }
  });
  
  Template.tempSection.helpers({
    'count': function(){
      return Temperatures.find({}).count();
    },
    'minTemp': function () {
      var temp = Temperatures.findOne({},{sort: {tmp:1}, limit: 1});
      if(!temp) return 0;
      return temp.tmp;
    },
    'currentTemp':function(){
      var temp =  Temperatures.findOne({},{sort: {ts:-1},limit: 1});
      if(!temp) return 0;
      return temp.tmp;
    },
    'maxTemp':function () {
      var temp = Temperatures.findOne({},{sort: {tmp:-1},limit: 1});
      if(!temp) return 0;
      return temp.tmp;
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
