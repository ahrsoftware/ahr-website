$(document).ready(function() {

    // Scroll to the section specified in parameter
    function scrollToSection(sectionid){
        $('html,body').animate({ scrollTop: $('section#' + sectionid).offset().top - 40 }, 800); 
    }

    // Scroll down to main welcome section when clicking on the proceed button in the welcome banner
    $('#jumbotron-proceed').on('click', function(){
        scrollToSection('welcome');
    });

    // Navigate to the linked particular section
    $('[sectionlink]').on('click', function(){
        scrollToSection($(this).attr('sectionlink'));
    });

    // Set the background of the navbar based on scroll position
    $(document).on('scroll', function (){
        let navHasSolidBg = $('nav').hasClass('solidbg');
        let currentPosition = $(window).scrollTop();
        let pastBanner = $('#jumbotron').offset().top + $('#jumbotron').height() + 100;
        // If past banner, add solid background. If not, remove it.
        if (currentPosition >= pastBanner && !navHasSolidBg) $('nav').addClass('solidbg');
        else if (currentPosition < pastBanner && navHasSolidBg) $('nav').removeClass('solidbg'); 
    });

    // Set the current year for copyright
    $('.currentyear').html(new Date().getFullYear());

});