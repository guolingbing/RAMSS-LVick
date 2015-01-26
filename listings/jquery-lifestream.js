var user = "jdoe";
$("#results").lifestream({
    list:[
        { 
          service: "github", 
          user: user
        },
        { 
          service: "twitter", 
          user: user
        },
        { 
          service: "reddit", 
          user: user
        }
    ]
});

 