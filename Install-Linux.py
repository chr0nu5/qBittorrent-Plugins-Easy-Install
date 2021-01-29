import os, time, shutil

src = "./nova3/"
dstlinux = "~/.local/share/data/qBittorrent/nova/"

if not os.path.exists(dstlinux):
    os.makedirs(dstlinux)
    print("Folder created")
    time.sleep(2)

else:
    print("Folder exists")
    time.sleep(2)

print("Copying files..")

shutil.copytree(src, dstlinux, dirs_exist_ok=True), time.sleep(4)

print("Copy complete")
print()
print("Restart qBittorrent and update the plugins!"), time.sleep(1)
print()
