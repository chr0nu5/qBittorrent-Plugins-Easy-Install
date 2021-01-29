import os, time, shutil

src = "./nova3/"
dstmac = "/Users/" + os.getlogin() + "/Library/Application Support/qBittorrent/nova3/"
dstlinux = "~/.local/share/data/qBittorrent/nova/"
dstwin = "\\Users\\username\\AppData\\Local\\qBittorrent\\nova3\\engines\\"

if not os.path.exists(dstmac):
    os.makedirs(dstmac)
    print("Folder created")
    time.sleep(2)

else:
    print("Folder exists")
    time.sleep(2)

print("Copying files..")

shutil.copytree(src, dstmac, dirs_exist_ok=True), time.sleep(4)

print("Copy complete")
print()
print("Restart qBittorrent and update the plugins!"), time.sleep(1)
print()
