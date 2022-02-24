import os
import time
import math
import random
import sys
from modules.util import *
import readkeys

files = [f for f in os.listdir("people") if os.path.isfile(os.path.join("people", f))]

mainText = [x.split(".")[0].capitalize() for x in files if x != "__init__.py"]
mainText.sort()
extraText = ["Main Test File || 0.3.1", "Made by Archit", "Files are shown below", ""]

mainText.append("Exit")

while True:
  selection = createMenu(mainText, 0, 63, extraText, 63)

  if selection == "Exit":
    clear()
    print("Test File Exited")
    break
  else:
    clear()
    f = open("people/" + selection.lower() + ".py")
    exec(f.read())
    f.close()
    print("\n\nPROGRAM COMPLETE")
    print("Press any key to continue")
    readkeys.getkey()