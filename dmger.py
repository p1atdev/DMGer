import sys
import os
import glob

for f in sys.argv[1:]:
    f = f.replace(" ", "\ ")
    base = os.path.basename(f)
    print(f)
    print(base)
    os.system("mkdir /tmp/" + base)
    os.system("7z x " + f + " -o/tmp/" + base)

    files = glob.glob("/tmp/" + base + "/*")
    apppath = ""
    for file in files:
        fls = glob.glob(file + "/*")
        for fl in fls:
            # print(fl)
            if fl.endswith(".app"):
                apppath = os.path.abspath(fl)
    apppath = apppath.replace(" ", "\ ")
    # contents = apppath + "/Contents/MacOS/*"
    print(apppath)
    os.system("chmod -R 777 " + apppath)
    print("mv "+ apppath + " " + os.path.dirname(f) + "/" +  os.path.basename(apppath))
    os.system("mv "+ apppath + " " + os.path.dirname(f) + "/")
    os.system("rm -r /tmp/" + base)
    
print("DMG extraction finished :)")
