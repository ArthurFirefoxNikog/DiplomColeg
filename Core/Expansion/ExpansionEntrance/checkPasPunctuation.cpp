#include <cctype>
#include <cstring>

extern "C" __declspec(dllexport) bool checkPasPunctuation(const char* password) {
    const char* punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
    for (size_t i = 0; i < strlen(password); ++i) {
        if (strchr(punctuation, password[i])) {
            return true;
        }
    }
    return false;
}