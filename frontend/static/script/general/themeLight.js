document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("theme-toggle");
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "light") {
        document.body.classList.add("light-theme");
    }

    if (button) {
        button.addEventListener("click", () => {
            document.body.classList.toggle("light-theme");

            if (document.body.classList.contains("light-theme")) {
                localStorage.setItem("theme", "light");
            } else {
                localStorage.setItem("theme", "dark");
            }
        });
    } else {
        console.error("Кнопка theme-toggle не найдена");
    }
});