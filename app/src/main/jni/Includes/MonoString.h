// Thanks to https://platinmods.com/threads/how-to-modify-unitys-il2cpp-string-methods.123414/ for this header


typedef struct _monostring {
    void *klass;
    void *monitor;
    int length;
    char chars[1];

    int getLength() {
        return length;
    }

    char *getChars() {
        return chars;
    }
} monostring;