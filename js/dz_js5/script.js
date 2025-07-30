let show = document.getElementById("show");
let hide = document.getElementById("hide");
let img = document.getElementById("img");

show.addEventListener('click', function(){
    img.src = 'car.jpg';  // Убедитесь, что файл car.jpg существует
    img.alt = 'Car image'; // Добавляем alt текст
    img.style.display = 'block';
});

hide.addEventListener('click', function(){
    img.style.display = 'none';
});