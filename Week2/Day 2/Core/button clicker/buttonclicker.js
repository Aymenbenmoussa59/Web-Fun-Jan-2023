var likesAlert = () => {
    window.alert('Ninja was liked')
}

var logInOut = (element) => {
    let inner = element.innerText;
    switch(inner){
        case 'Login': 
        element.innerText = 'Logout'
            break;
        case 'Logout': 
        element.innerText = 'Login'
            break;
    }
}

var addDef = (element) => {
    element.style.visibility  = 'hidden'}