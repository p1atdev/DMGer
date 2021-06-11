import os
import sys

for f in sys.argv[1:]:
    f = f.replace(" ", "\ ") + "/Contents/MacOS/*"
    print(f)
    os.system("chmod 777 " + f)

print("chmod process finished :)")