       var Crawler = require("crawler");
(function ($){
    "use strict";
       function fetchTital(id){

        var c = new Crawler({
            maxConnections : 1000,
            // This will be called for each crawled page
            callback : function (error, res, done) {
                if(error){
                    console.log(error);
                }else{
                    var $ = res.$;
                    // $ is Cheerio by default
                    //a lean implementation of core jQuery designed specifically for the server
                    console.log($("title").text());
                }
                done();
            }
        });

        // Queue just one URL, with default callback
        c.queue('http://www.amazon.com');
       }

      $('#trial').click(function(){
        console.log('alive !');
        var Id = $('#UserID').val();

        let url = 'https://www.instagram.com/'+Id;
        console.log(url);
        fetchTital(url);

//https://www.youtube.com/watch?v=DdUtE1VVUrI&ab_channel=CodingShiksha
//        "https://graph.facebook.com/" + userId + "/picture"


// NO core errro resolved in comment section
//https://www.youtube.com/watch?v=gDmmokYDPOw&ab_channel=CCSIT-KFU

      });
})(jQuery);

