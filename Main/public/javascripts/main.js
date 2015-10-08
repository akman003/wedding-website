
$(function () {

    // RSVP system
    var base = 'http://127.0.0.1:8000/rsvps';
    // 0. handle errors:
    var handleError = function(){
        $('#guestsearch, #guestsearchresults, #attendance, #confirmation, #confirmationdecline').fadeOut(function(){
            $('#rsvperror').fadeIn();
        });
    };

    $(document).ajaxError(handleError);

    // 1. user searches their name:
    $('#rsvp-search').submit( function () {

        // validate
        var searchtext = $('#rsvp-name').val();

        if(searchtext.length == 0) {
            return false;
        }

        $.get(base + '/search/' + encodeURIComponent(searchtext)).done(function(searchResults){
            console.log(searchResults);

            var template = $('#guest-search-results-template').html();
            var rendered = Mustache.render(template, {
                people: searchResults
            });

            $('#rsvp-modal').find('.modal-body').html(rendered);
            $('#rsvp-modal').modal('show');
        });

        // animate out
        $('#guestsearch').fadeOut( function () {
            // data
            $.get(base + '/search/' + encodeURIComponent(searchtext)).done(function(searchResults){
                var template = $('#guestsearchresultstemplate').html();
                var rendered = $.mustache(template, {
                    people: searchResults
                });
                $('#guestsearchresults').html(rendered);
                // animate in
                $('#guestsearchresults').fadeIn();
            });
        });
        return false;
    });

    $('.mfb-component__button--child').click( function () {
        $('.mfb-component--br').attr('data-mfb-state', 'closed');
    });
});
