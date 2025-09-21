with open("sample.txt","r") as f:
    lines= f.readlines()
    lastline=lines[-1].strip()
    b=lastline.split()
    a=int(b[0])
with open("sample.txt", "a") as f:
    for i in range(a+1,a+6):
        f.write(f"{i} Ashwin\n")
print("Done writing.")


