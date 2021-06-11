import sys
import os
import glob

for f in sys.argv[1:]:
    f = f.replace(" ", "\ ")
    print(f)
    os.system("7zz x " + f + " -o/Users/$(whoami)/Downloads")
    
print("Finished")
