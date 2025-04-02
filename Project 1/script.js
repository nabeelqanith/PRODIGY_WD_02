const navbar = document.getElementById('navbar');
const navLinks = document.querySelectorAll('.nav-link');
const colors = ['#333', '#555', '#777', '#999', '#bbb', '#ddd', '#ffcc00', '#ff6699'];
let currentColorIndex = 0;

window.addEventListener('scroll', () => {
    currentColorIndex = (currentColorIndex + 1) % colors.length;
    navbar.style.backgroundColor = colors[currentColorIndex];
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
    });
});