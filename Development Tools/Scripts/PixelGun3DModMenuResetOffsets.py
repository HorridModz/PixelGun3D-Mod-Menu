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


def get32bit():
    with open(_Offsets32bitPath, "r") as f:
        return f.read()


with open(_OutputPath, "w") as backup:
    backup.write(f"//32bit:\n\n{get32bit()}\n//64bit:\n\n{get64bit()}")
content = get64bit()
with open(_Offsets64bitPath, "w") as f:
    new = content
    for charcount in range(8):
        pattern = "0x" + "." * charcount + ";"
        new = re.sub(pattern, "0x69420;", new)
    f.write(new)
content = get32bit()
with open(_Offsets32bitPath, "w") as f:
    new = content
    for charcount in range(8):
        pattern = "0x" + "." * charcount + ";"
        new = re.sub(pattern, "0x69420;", new)
    f.write(new)
