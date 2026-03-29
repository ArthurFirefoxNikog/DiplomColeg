let translations = {};

function getValue(obj, path) {
    return path.split('.').reduce((o, key) => {
        if (Array.isArray(o)) return o[Number(key)];
        return o?.[key];
    }, obj);
}

async function loadLang(lang) {
    const res = await fetch(`../../lang/${lang}.json`);
    translations = await res.json();

    applyTranslations(lang);
    setActiveButton(lang);
}

function setActiveButton(lang) {
    document.querySelectorAll(".buttons-language button").forEach(btn => {
        btn.classList.remove("select-button-translate");

        if (btn.value === lang) {
            btn.classList.add("select-button-translate");
        }
    });
}

function applyTranslations(lang) {

    document.documentElement.lang = lang;

    // текст
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.dataset.i18n;
        el.textContent = getValue(translations, key);
    });

    // placeholder
    document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
        const key = el.dataset.i18nPlaceholder;
        el.placeholder = getValue(translations, key);
    });
}

const savedLang = localStorage.getItem("lang") || "ru";
loadLang(savedLang);

document.querySelectorAll(".buttons-language button").forEach(btn => {
    btn.addEventListener("click", () => {
        loadLang(btn.value);
        localStorage.setItem("lang", btn.value);

        document.querySelectorAll(".buttons-language button").forEach(b => {
            b.classList.remove("select-button-translate");
        });

        btn.classList.add("select-button-translate");

    });
});