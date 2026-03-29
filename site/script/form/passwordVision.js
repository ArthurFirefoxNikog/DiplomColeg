function changingIcon(button, password){
    if (button){
        button.addEventListener("click", () => {
            if (password.type === "password") {
                password.type = "text";
                button.classList.remove("button-not-vision-password");
                button.classList.add("attention");
                button.classList.add("button-vision-password");
            } else {
                password.type = "password";
                button.classList.remove("button-vision-password");
                button.classList.remove("attention");
                button.classList.add("button-not-vision-password");
            }
        })
    }
};

document.addEventListener("DOMContentLoaded", function() {

    const btnFromRegisterVision1 = document.getElementById("btnVis1");
    const btnFromRegisterVision2 = document.getElementById("btnVis2");

    const pasFromRegisterVision1 = document.getElementById("pasCr");
    const pasFromRegisterVision2 = document.getElementById("pasCon");


    const btnFromLoginVision = document.getElementById("btnVis");

    const pasFromLoginVision = document.getElementById("pasLogin");


    changingIcon(btnFromRegisterVision1, pasFromRegisterVision1)
    changingIcon(btnFromRegisterVision2, pasFromRegisterVision2)

    changingIcon(btnFromLoginVision, pasFromLoginVision)
});