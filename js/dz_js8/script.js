let choose = document.querySelector("input[type='button']")

choose.addEventListener("click", chooseColor)

function chooseColor(){
    let f = document.form3.radio2
    console.log(f.lenght)
    for(let i=0; i<f.length; i++){
        if(f[i].checked){
            alert(`${f[i].value}`)
        }
    }
    
}