let password = document.getElementById("password");
let strength = document.getElementById("strength");

password.addEventListener("input", function(){

    let pass = password.value;

    if(pass.length < 6){
        strength.innerHTML = "Weak";
        strength.style.color = "red";
    }
    else if(pass.length < 10){
        strength.innerHTML = "Medium";
        strength.style.color = "orange";
    }
    else{
        strength.innerHTML = "Strong";
        strength.style.color = "green";
    }

});
