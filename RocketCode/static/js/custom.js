// $(document).ready(function(){
//     // Create a scroll container
//     var controller = new ScrollMagic.Controller();

//     var sceneOne = new ScrollMagic.Scene({
//         duration: 500
//     }).setPin('#TitleBoxSection');

//     var sceneTwo = new ScrollMagic.Scene({
//         triggerElement: '#PersistenceSection',
//         duration: 500
//     }).setPin('#PersistenceSection');

//     controller.addScene([
//         sceneOne,
//         sceneTwo
//     ]);
// });


document.querySelector(".ContactMeForm").addEventListener("submit", function(e){
    alert("SENT");
    submitButton = document.querySelector(".submitbutton");
    submitButton.color = "red";
    e.preventDefault();
})








// var element = document.querySelector(".wrapper")
// if (element)
// {
//     element.addEventListener('click', (e) => {
//         e.currentTarget.classList.toggle('is-active');
//     });
// }
