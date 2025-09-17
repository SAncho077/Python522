document.querySelector("#button").addEventListener("click", loadUsers);

async function loadUsers() {
    let url = "https://jsonplaceholder.typicode.com/todos";
    let response = await fetch(url);
    let data = await response.json();
    
    // Фильтруем только выполненные задачи
    let completedTasks = data.filter(item => item.completed === true);
    
    let html = completedTasks.map(function (item) {
        return "<li>" + "Пользователь: " + item.userId + 
               " Выполнил задачу № " + item.id + 
               " - " + item.title + "</li>";
    });
    document.querySelector("#list").innerHTML = '';
    document.querySelector("#list").insertAdjacentHTML('afterbegin', html.join(" "));
};


