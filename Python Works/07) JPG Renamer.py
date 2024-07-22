import os
os.chdir("test AVIFs")
print(os.getcwd())
i = 1
for filename in os.listdir():
    ext = os.path.splitext(filename)
    os.rename(filename, str(i) + ext[1])
    i += 1
print(os.listdir())
