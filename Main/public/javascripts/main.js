
$(function () {

    $('.mfb-component__button--child').click( function () {
        $('.mfb-component--br').attr('data-mfb-state', 'closed');
    });

    $('#wedding-video').click( function () {
        var $videoModal = $('#video-modal');
        $videoModal.modal('show');
        // $videoModal.find('video')[0].play();
        return false;
    });

    $('#video-modal').on('hidden.bs.modal', function() {
        $(this).find('video')[0].pause();
    });

    $('a.gallery').featherlightGallery({
        openSpeed: 300
    });
});
