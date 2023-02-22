monostring* CreateMonoString(char *str);

// Init Hooks

monostring *(*String_CreateString)(void *instance, char* str);

void Update() {
    // All stuff that should be done every game tick
    // but does not have a class with an update function
    // can go here.
}


int(*old_GameEventItemData_get_Count)(void *instance);
int GameEventItemData_get_Count(void *instance) {
    if (instance != NULL) {
        if (updatehooksready) {
            if (Features::isLottoSets10k) {
                return 10,000;
            }
        }
    }
    return old_GameEventItemData_get_Count(instance);
}

monostring* CreateMonoString(char *str) {
    return String_CreateString(nullptr, str);
}