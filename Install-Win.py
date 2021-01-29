import os, time, shutil

src = "./nova3/"
dstwin = "\\Users\\" + os.getlogin() + "\\AppData\\Local\\qBittorrent\\nova3\\engines\\"

if not os.path.exists(dstwin):
    os.makedirs(dstwin)
    print("Folder created")
    time.sleep(2)

else:
    print("Folder exists")
    time.sleep(2)

print("Copying files..")

shutil.copytree(src, dstwin, dirs_exist_ok=True), time.sleep(4)

print("Copy complete")
print()
print("Restart qBittorrent and update the plugins!"), time.sleep(1)
print()
