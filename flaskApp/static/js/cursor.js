const cursorTag = document.querySelector("div.cursors");
const balls = cursorTag.querySelectorAll("div");

let aimX = 0;
let aimY = 0;

balls.forEach((ball, index) => {
    let currentX = 0;
    let currentY = 0;
    let speed = 0.2 - index * 0.01;
    const animate = function () {
        currentX += (aimX - currentX) * speed;
        currentY += (aimY - currentY) * speed;

        ball.style.left = currentX + "px";
        ball.style.top = currentY + "px";

        requestAnimationFrame(animate);
    };
    animate();
});

const projectItems = document.querySelectorAll("div.ProjectItem");
projectItems.forEach((item) => {
    $(item).hover(
        function () {
            $(balls[0]).append($(this).find("h3")[0].cloneNode(true));
            $(balls[0]).append($(this).find("p")[0].cloneNode(true));
            $(balls[0]).find("p").append(" <br> click for more info!");
        },
        function () {
            $(balls[0]).empty();
        }
    );
});

document.addEventListener("mousemove", function (event) {
    aimX = event.pageX - 5;
    aimY = event.pageY - 90;
});

