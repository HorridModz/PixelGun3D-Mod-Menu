import sys
import re

_Offsets64bitPath = r"C:\Users\zachy\AndroidStudioProjects\PixelGun3D-Mod-Menu\app\src\main\jni\Hacks\Offsets64bit.h"
_Offsets32bitPath = r"C:\Users\zachy\AndroidStudioProjects\PixelGun3D-Mod-Menu\app\src\main\jni\Hacks\Offsets32bit.h"
_OutputPath = r"C:\Users\zachy\OneDrive\Documents\Work\Temp\Python Temps\modmenuoffsets.cpp"

log = []


def logmessage(message):
    log.append(message)

def get64bit():
    with open(_Offsets64bitPath, "r") as f:
        return f.read()

def replace64bit(replaced, resetoffsets=True):
    new = replaced
    if resetoffsets:
        for charcount in range(8):
            pattern = "0x" + "." * charcount + ";"
            new = re.sub(pattern, "0x69420;", new)
    with open(_Offsets64bitPath, "w") as f:
        f.write(new)

def get32bit():
    with open(_Offsets32bitPath, "r") as f:
        return f.read()

def replace32bit(replaced, resetoffsets=True):
    new = replaced
    if resetoffsets:
        for charcount in range(8):
            pattern = "0x" + "." * charcount + ";"
            new = re.sub(pattern, "0x69420;", new)
    with open(_Offsets32bitPath, "w") as f:
        f.write(new)

with open(_OutputPath, "w") as backup:
    backup.write(get64bit())
replace64bit(get32bit(), True)