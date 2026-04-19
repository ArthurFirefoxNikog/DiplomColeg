const languages = ["ru", "en", "kk"];
let translations = {};
let currentLang = localStorage.getItem("lang") || "ru";

async function loadTranslations() {
    for (let lang of languages) {
        const res = await fetch(`/static/lang/${lang}.json`);
        translations[lang] = await res.json();
    }
}

function getValue(obj, path) {
    return path.split(".").reduce((acc, part) => acc?.[part], obj);
}

function applyLanguage(lang) {
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.dataset.i18n;
        const value = getValue(translations[lang], key);

        if (value) {
            el.textContent = value;
        }
    });

    localStorage.setItem("lang", lang);
}

function nextLang(lang) {
    if (lang === "ru") return "en";
    if (lang === "en") return "kk";
    return "ru";
}

document.addEventListener("DOMContentLoaded", async () => {
    await loadTranslations();
    applyLanguage(currentLang);

    document.getElementById("lang-toggle").addEventListener("click", () => {
        currentLang = nextLang(currentLang);
        applyLanguage(currentLang);
    });
});