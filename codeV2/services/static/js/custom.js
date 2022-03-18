$(document).ready(function(){
    // Create a scroll container
    var controller = new ScrollMagic.Controller();

    // Create a scene for first trigger and set properties via an object
    var sceneOne = new ScrollMagic.Scene({
        duration: 500
    }).setPin('#TitleBox');


    // Create a Scene for second trigger and set properties via an object
    var sceneTwo = new ScrollMagic.Scene({
        triggerElement: '#PersistenceValueCircle',
        duration: 500
    }).setPin('#PersistenceValueCircle');

    // Add scenes to controller
    controller.addScene([
    ]);


});