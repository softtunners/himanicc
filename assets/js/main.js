// This code is written for Opening Full header (Nav-Header) - Main file can be found in Base.html & Link.html

$(document).on('ready', function () {
    var headerFullscreen = new HSHeaderFullscreen($('#headerFullscreen')).init();

    $(document).on('keydown', function (e) {
        if (e.keyCode && e.keyCode === 27) {
            $('[aria-pressed]').attr('aria-pressed', false).removeClass('active focus');
            $('#fullscreenNav .collapse').collapse('hide');
        }
    });
});


// This code is written for Slider (Main-slider) - Main file can be found in index.html & Link.html

$(document).on('ready', function () {
    $('.js-slick-carousel').each(function () {
        var slickCarousel = $.HSCore.components.HSSlickCarousel.init($(this));
    });
});


//scrapbook.html || the code is written for gallery

$(document).on('ready', function () {
    $('.cbp').each(function () {
        var cbp = $.HSCore.components.HSCubeportfolio.init($(this), {
            layoutMode: 'grid',
            filters: '#filterControls'
        });
    });
});