let form = document.form1;

let message = {
    loading: "Загрузка",
    success: "Спасибо! Скоро мы с вами свяжемся",
    failure: "Что-то пошло не так..."
}

form.addEventListener("submit", event => {
    event.preventDefault()

    let msg = document.createElement("div")
    msg.textContent = message.loading
    form.append(msg)

    let request = new XMLHttpRequest();
    request.open("POST", "server.php")
    let formData = new FormData(form)
    request.send(formData)

    request.addEventListener("load", function(){
        if(request.status == 200){
      
            msg.remove();
            
     
            let new_div = document.createElement('div')
            new_div.innerHTML = message.success
            new_div.classList.add('new_div') 
            
 
            
            form.append(new_div) 
            
        } else {
            msg.textContent = message.failure
            msg.style.backgroundColor = "#f8d7da";
            msg.style.color = "#721c24";
        }
        
        form.reset()
        setTimeout(() => {
        
            let messages = form.querySelectorAll('div');
            messages.forEach(message => message.remove());
        }, 3000)
    })
})