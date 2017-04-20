$(document).ready(function() {
    $('[data-toggle="offcanvas"]').click(function() {
        $('#wrapper').toggleClass('menuDisplayed');
    });


        $BODY = $('body'),
        $MENU_TOGGLE = $('#menu_toggle'),
        $SIDEBAR_MENU = $('#sidebar-menu');

    var menu_toggle = false;

    $MENU_TOGGLE.on('click', function() {
        if (menu_toggle == false) {
            $('#sidebar-wrapper').find('#profile').show();
            $('#chevron-down').addClass('fa fa-chevron-down');
            $('.menu-section').find('h3').show();
            $('.menu-section').find('.fa').css({'font-size':'18px'});
            $('.menu-section').css({'text-align':'left'});
            $('.menu-footer').addClass('sidebar-footer');
            menu_toggle = true;
        } else {
            $('#sidebar-wrapper').find('#profile').hide();
            $('#sidebar-menu').find('.fa-chevron-down').removeClass();
            $('.menu-section').css({'text-align':'center'});
            $('.menu-section').find('.fa').css({'font-size':''});
            $('#sidebar-menu').find('h3').hide();
            $('.menu-footer').removeClass('sidebar-footer');
            menu_toggle = false;
        }
    })
});
