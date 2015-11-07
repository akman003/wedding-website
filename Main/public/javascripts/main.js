
$(function () {

    // RSVP system
    var base = 'http://127.0.0.1:8000/rsvps';
    // 0. handle errors:
    var handleError = function() {
        var $modal = $('#rsvp-modal');
        $modal.find('#guest-search-results').html('').hide();
        $modal.find('#attendance').html('').hide();
        $modal.find('#confirmation').html('').hide();
        $modal.find('#confirmation-decline').html('').hide();
        $('#rsvp-modal').find('#error').html(Mustache.render($('#error-template').html())).fadeIn();
    };

    $(document).ajaxError(handleError);

    // 1. user searches their name:
    $('#rsvp-search').submit( function () {

        // trim and validate
        var searchtext = $('#rsvp-name').val();
        searchtext = searchtext.replace(/\s/g, '');

        if(searchtext.length == 0) {
            return false;
        }

        $.get(base + '/search/' + encodeURIComponent(searchtext)).done( function (searchResults) {

            var template = $('#guest-search-results-template').html();
            var rendered = Mustache.render(template, {
                people: searchResults
            });

            $('#rsvp-modal').find('#guest-search-results').html(rendered).fadeIn();
            $('#rsvp-modal').modal('show');
        });

        return false;
    });

    // 2. user selects their name:
    $('#guest-search-results').on('click', 'li a', function () {

        // validate / find what they chose
        var guestid = $(this).attr('href');

        $('#rsvp-modal').find('#guest-search-results').fadeOut( function () {

            // data
            $.ajax({
                url:base + '/' + guestid,
                success: function(data) {
                    data.num_allowed_array = function() {
                        var ret = [];
                        for (var i = 1; i <= data.num_allowed; i++) {
                            ret.push({'num':i, 'checked':(i==data.num_allowed)});
                        };
                        return ret;
                    };

                    var template = $('#attendance-template').html();
                    var rendered = Mustache.render(template, data);

                    $('#rsvp-modal').find('#attendance').html(rendered).fadeIn();
                },
                error: function(error) {
                    handleError();
                }
            });
        });
        return false;
    });

    $('#attendance').on('submit', 'form#attending-form', function() {
        // validate / gather data
        var isAttending = ($('[name="attendance-radio"]:checked', this).val() == 'attending');
        var num_rsvpd = 0;
        if (isAttending) {
            num_rsvpd = $('select[name="num_attending"]').val();
        }
        var guestid = $(this).data('guestid');
        var guestname = $(this).data('guestname');

        // animate out
        $('#attendance').fadeOut(function() {
            // data
            $.ajax({
                url:base + '/' + guestid,
                type:'POST',
                dataType:'json',
                data: {'num_rsvpd':num_rsvpd},
                success: function(data) {
                    if(data.detail) {
                        alert(data.detail);
                        handleError();
                    } else {
                        if(isAttending) {
                            var template = $('#confirmation-template').html();
                            var rendered = Mustache.render(template, { name:guestname });
                            $('#confirmation').html(rendered).fadeIn();
                            $('#rsvp-modal').find('#confirmation').html(rendered).fadeIn();
                        } else {
                            var template = $('#confirmation-decline-template').html();
                            var rendered = Mustache.render(template, { name:guestname });
                            $('#rsvp-modal').find('#confirmation-decline').html(rendered).fadeIn();
                        }
                    }
                }
            });
        });
        return false;
    });

    $('.mfb-component__button--child').click( function () {
        $('.mfb-component--br').attr('data-mfb-state', 'closed');
    });

    $('#rsvp-modal').on('hidden.bs.modal', function() {
        var $this = $(this);
        $this.find('#guest-search-results').html('').hide();
        $this.find('#attendance').html('').hide();
        $this.find('#confirmation').html('').hide();
        $this.find('#confirmation-decline').html('').hide();
        $this.find('#error').html('').hide();
    });
});
