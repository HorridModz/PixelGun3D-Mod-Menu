#if defined(__aarch64__)
bool is64bit = true;
#else
bool is64bit = false;
#endif
#define targetLibName OBFUSCATE("libil2cpp.so")
#include <chrono>
#include <thread>
#include <list>
#include <vector>
#include <string.h>
#include <cstring>
#include <pthread.h>
#include <thread>
#include <cstring>
#include <jni.h>
#include <unistd.h>
#include <fstream>
#include <iostream>
#include <dlfcn.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include "Includes/Logger.h"
#include "Includes/obfuscate.h"
#include "Includes/Offset2String.hpp"
#include "Includes/Vector3.h"
#include "Includes/MonoString.h"
#include "Includes/monoarray.h"
#include "Includes/Utils.h"
#include "KittyMemory/MemoryPatch.h"
#include "Includes/Macros.h"
std::string VERSION = "1.0.0";
bool menuauthorized = false;
int hackthreaddone = 0;
bool updatehooksready = true;
//#include "ByNameModding/BNM.cpp"
////#include "ByNameModding/BNM.hpp"
//#include "Hacks/oldoffsets.h"
#if defined(__aarch64__)
//#include "Hacks/Offsets64bit.h"
#include "Hacks/Offsets32bit.h"
#else
#include "Hacks/Offsets32bit.h"
#endif
#include "Hacks/Features.hpp"
#include "Hacks/FeatureDefaults.hpp"
// For some reason, I get an error if I try to call setfeaturedefaults() by itself.
// However, if I make a middle-man function that calls setfeaturedefaults() and returns a value,
// then store and immediately dispose of this value, it works.
int setfeaturedefaultsworkaround_ = setfeaturedefaultsworkaround();
#include "Menu/Hooks.h"
#include "Menu/HackThread.h"
// For some reason, I get an error if I try to call starthackthread() by itself.
// However, if I make a middle-man function that calls starthackthread() and returns a value,
// then store and immediately dispose of this value, it works.
int starthackthreadworkaround_ = starthackthreadworkaround();
#include "Menu/Setup.h"


// Do not change or translate the first text unless you know what you are doing
// Assigning feature numbers is optional. Without it, it will automatically count for you, starting from 0
// Assigned feature numbers can be like any numbers 1,3,200,10... instead in order 0,1,2,3,4,5...
// ButtonLink, Category, RichTextView and RichWebView is not counted. They can't have feature number assigned
// Toggle, ButtonOnOff and CheckBox can be switched on by default, if you add True_. Example: CheckBox_True_The Check Box
// To learn HTML, go to this page: https://www.w3schools.com/

jobjectArray GetFeatureList(JNIEnv *env, jobject context) {
    jobjectArray ret;

    const char *features[] = {
            OBFUSCATE("RichTextView_Pixel Gun 3D Mod Menu By HorridModz<br /><font color='gray'><b>Discord: User123456789#6424</b></font>"),
            OBFUSCATE("0_Toggle_Lotto Sets 10k"), //Done
            OBFUSCATE("Category_About"),
            OBFUSCATE("ButtonLink_Mod Menu Github Page_https://github.com/HorridModz/Pixel-Gun-3D-Mod-Menu"),
            OBFUSCATE("Collapse_My Socials"),
            OBFUSCATE("CollapseAdd_RichTextView_Discord: User123456789#6424<br />Youtube: HorridModz 2.0<br />Github: HorridModz<br />Gameguardian: HorridModz<br />"),
            OBFUSCATE("CollapseAdd_ButtonLink_Youtube_https://www.youtube.com/channel/UCt17kVvITO-q-zUICdw7hUQ"),
            OBFUSCATE("CollapseAdd_ButtonLink_Github_https://github.com/HorridModz"),
            OBFUSCATE("CollapseAdd_ButtonLink_Gameguardian_https://gameguardian.net/forum/profile/1234241-horridmodz/"),
            OBFUSCATE("Collapse_Credits"),
            OBFUSCATE("CollapseAdd_RichTextView_Thanks to LGL for the mod menu template"),
    };

    //Now you dont have to manually update the number everytime;

    int Total_Feature = (sizeof features / sizeof features[0]);
    ret = (jobjectArray)
            env->NewObjectArray(Total_Feature, env->FindClass(OBFUSCATE("java/lang/String")),
                                env->NewStringUTF(""));

    for (int i = 0; i < Total_Feature; i++)
        env->SetObjectArrayElement(ret, i, env->NewStringUTF(features[i]));
    return (ret);
}

void Changes(JNIEnv *env, jclass clazz, jobject obj,
             jint featNum, jstring featName, jint value,
             jboolean boolean, jstring str) {

    LOGD(OBFUSCATE("Feature name: %d - %s | Value: = %d | Bool: = %d | Text: = %s"), featNum,
         env->GetStringUTFChars(featName, 0), value,
         boolean, str != NULL ? env->GetStringUTFChars(str, 0) : "");

    //BE CAREFUL NOT TO ACCIDENTLY REMOVE break;
    switch (featNum) {
		

		//Lotto Sets 10k
		case 0:
			Features::Toggle_LottoSets10k((boolean != JNI_FALSE));
            PATCH_LIB_SWITCH("libil2cpp.so", "0x2995F28", "100702E31EFF2FE1", Features::isLottoSets10k);
            break;

	}
    updatehooksready = true;
}

__attribute__((constructor))
void lib_main() {
	// Create a new thread so it does not block the main thread, means the game would not freeze
	//pthread_t ptid;
	//pthread_create(&ptid, NULL, hack_thread, NULL);
}

int RegisterMenu(JNIEnv *env) {
	JNINativeMethod methods[] = {
			{OBFUSCATE("Icon"), OBFUSCATE("()Ljava/lang/String;"), reinterpret_cast<void *>(Icon)},
			{OBFUSCATE("IconWebViewData"),  OBFUSCATE("()Ljava/lang/String;"), reinterpret_cast<void *>(IconWebViewData)},
			{OBFUSCATE("IsGameLibLoaded"),  OBFUSCATE("()Z"), reinterpret_cast<void *>(isGameLibLoaded)},
			{OBFUSCATE("Init"),  OBFUSCATE("(Landroid/content/Context;Landroid/widget/TextView;Landroid/widget/TextView;)V"), reinterpret_cast<void *>(Init)},
			{OBFUSCATE("SettingsList"),  OBFUSCATE("()[Ljava/lang/String;"), reinterpret_cast<void *>(SettingsList)},
			{OBFUSCATE("GetFeatureList"),  OBFUSCATE("()[Ljava/lang/String;"), reinterpret_cast<void *>(GetFeatureList)},
	};

	jclass clazz = env->FindClass(OBFUSCATE("com/android/support/Menu"));
	if (!clazz)
		return JNI_ERR;
	if (env->RegisterNatives(clazz, methods, sizeof(methods) / sizeof(methods[0])) != 0)
		return JNI_ERR;
	return JNI_OK;
}

int RegisterPreferences(JNIEnv *env) {
	JNINativeMethod methods[] = {
			{OBFUSCATE("Changes"), OBFUSCATE("(Landroid/content/Context;ILjava/lang/String;IZLjava/lang/String;)V"), reinterpret_cast<void *>(Changes)},
	};
	jclass clazz = env->FindClass(OBFUSCATE("com/android/support/Preferences"));
	if (!clazz)
		return JNI_ERR;
	if (env->RegisterNatives(clazz, methods, sizeof(methods) / sizeof(methods[0])) != 0)
		return JNI_ERR;
	return JNI_OK;
}

int RegisterMain(JNIEnv *env) {
	JNINativeMethod methods[] = {
			{OBFUSCATE("CheckOverlayPermission"), OBFUSCATE("(Landroid/content/Context;)V"), reinterpret_cast<void *>(CheckOverlayPermission)},
	};
	jclass clazz = env->FindClass(OBFUSCATE("com/android/support/Main"));
	if (!clazz)
		return JNI_ERR;
	if (env->RegisterNatives(clazz, methods, sizeof(methods) / sizeof(methods[0])) != 0)
		return JNI_ERR;

	return JNI_OK;
}

extern "C"
JNIEXPORT jint JNICALL
JNI_OnLoad(JavaVM *vm, void *reserved) {
	JNIEnv *env;
	vm->GetEnv((void **) &env, JNI_VERSION_1_6);
	if (RegisterMenu(env) != 0)
		return JNI_ERR;
	if (RegisterPreferences(env) != 0)
		return JNI_ERR;
	if (RegisterMain(env) != 0)
		return JNI_ERR;
	return JNI_VERSION_1_6;
}