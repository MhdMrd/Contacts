$(document).ready(function(){
    $('.collapsible').collapsible({
        accordion: true
    });
    $('.parallax').parallax();
    $(".button-collapse").sideNav();
    $('.carousel').carousel();
    $('.modal-trigger').leanModal({
        dismissible: true, // Modal can be dismissed by clicking outside of the modal
        opacity: .5, // Opacity of modal background
        in_duration: 300, // Transition in duration
        out_duration: 200, // Transition out duration
        starting_top: '4%', // Starting top style attribute
        ending_top: '10%', // Ending top style attribute
    }
  );
});

$(document).ready(function(){
    var tab = ["images/Wallpapers/free-hd-wallpaper-download.jpg","images/Wallpapers/Itachi-Uchiha-HD-Background.png", "images/Wallpapers/wallpaper17_UCtPqot.jpg"];
    for (var i = 0; i <tab.length; i++) {
            $("#body").css({
                'background-image': 'url('+tab[i]+')',
            });
            
        };

});

new WOW().init();
