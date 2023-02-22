//Hack thread

void *hack_thread(void *) {
    LOGI(OBFUSCATE("Hack thread pthread created"));

    //Check if target lib is loaded
    do {
        sleep(1);
    } while (!isLibraryLoaded("libil2cpp.so"));

    //Anti-lib rename
    //
    //do {
    //    sleep(1);
    //} while (!isLibraryLoaded("libil2cpp.so"));

    LOGI(OBFUSCATE("%s has been loaded"), (const char *) targetLibName);
    hackthreaddone = 1;

    //Initial Hooks and Patches

    LOGD(OBFUSCATE("Mod Menu: Hooking..."));

    //String.CreateString(char* value)
    //String_CreateString = (monostring *(*)(void *, char *))getAbsoluteAddress("libil2cpp.so", Offsets::Methods.String_CreateString);

    //LOGD(OBFUSCATE("Mod Menu: Hooked String.CreateString"));
    ////char* monostringtest = reinterpret_cast<char *>(CreateMonoString("Test"));
    ////LOGD(OBFUSCATE("Mod Menu: Tested String.CreateString %s"), monostringtest);

    //GameEventItemData.get_Count
    //HOOK_LIB("libil2cpp.so", Offset2String(Offsets::Methods.GameEventItemData_get_Count), GameEventItemData_get_Count, old_GameEventItemData_get_Count);
    //LOGD(OBFUSCATE("Mod Menu: Hooked GameEventItemData.get_Count"));

    hackthreaddone = 2;
	return NULL;
}

void starthackthread() {
// we will run our hacks in a new thread so our while loop doesn't block process main thread
pthread_t ptid;
pthread_create(&ptid, NULL, hack_thread, NULL);
}

int starthackthreadworkaround() {
    // For some reason, I get an error if I try to call starthackthread() by itself.
    // However, if I make a middle-man function that calls starthackthread() and returns a value,
    // then store and immediately dispose of this value, it works.
    starthackthread();
    LOGD("Started hack thread");
    return 0;
}