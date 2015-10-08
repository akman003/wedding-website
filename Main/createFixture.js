// CSV-to-JSON data goes here
var data = [{"Titles":"Mr. and Mrs.","Name(s)":"David and Kathy Killinger","No.":2},{"Titles":"Ms.","Name(s)":"Cindy Killinger","No.":1},{"Titles":"Mr. and Ms.","Name(s)":"Faith Grandchamp and Bob","No.":2},{"Titles":"Mr.","Name(s)":"Tom Killinger","No.":1},{"Titles":"Mr. and Mrs.","Name(s)":"Parke and Lois Killinger","No.":2},{"Titles":"Mr. and Mrs.","Name(s)":"Ronny and Inez Killinger","No.":2},{"Titles":"Mr. and Mrs.","Name(s)":"Chris and Franny Arryo","No.":2},{"Titles":"Ms.","Name(s)":"Joni Fluke","No.":1},{"Titles":"Ms.","Name(s)":"Mary Fluke","No.":1}];

var counter = 0;
var fixture = $.map(data, function(person) {
    return {
        "model": "rsvps.Invitee",
        "pk": ++counter,
        "fields": {
            "name":person.Titles + ' ' + person["Name(s)"],
            "num_allowed":person["No."],
            "was_submitted":false,
            "num_rsvpd":0
        }
    }
});
console.log(JSON.stringify(fixture));