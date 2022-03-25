$(document).ready(function(){
    // Create a scroll container
    var controller = new ScrollMagic.Controller();

    var sceneOne = new ScrollMagic.Scene({
        duration: 500
    }).setPin('#TitleBoxSection');

    var sceneTwo = new ScrollMagic.Scene({
        triggerElement: '#PersistenceSection',
        duration: 500
    }).setPin('#PersistenceSection');

    controller.addScene([
        sceneOne,
        sceneTwo
    ]);
});






// var element = document.querySelector(".wrapper")
// if (element)
// {
//     element.addEventListener('click', (e) => {
//         e.currentTarget.classList.toggle('is-active');
//     });
// }
