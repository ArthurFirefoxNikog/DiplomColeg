document.addEventListener("DOMContentLoaded", function() {

    const indexBtn = document.getElementById("button-link-for-index");
    if (indexBtn) {
        indexBtn.addEventListener("click", function(event) {
            event.preventDefault();
            document.getElementById("link-for-index").click();
        });
    }

});