document.addEventListener("DOMContentLoaded", function() {

    const registerBtn = document.getElementById("button-link-for-register");
    if (registerBtn) {
        registerBtn.addEventListener("click", function(event) {
            event.preventDefault();
            document.getElementById("link-for-register").click();
        });
    }

    const loginBtn = document.getElementById("button-link-for-login");
    if (loginBtn) {
        loginBtn.addEventListener("click", function(event) {
            event.preventDefault();
            document.getElementById("link-for-login").click();
        });
    }

});