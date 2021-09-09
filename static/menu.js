let menu = document.getElementById("collapsible-menu");
menu.classList = "collapse navbar-collapse";

let button = document.querySelector("nav .navbar-toggler");
button.toggleAttribute("hidden");
button.addEventListener("click", () => { menu.classList.toggle("show") });
