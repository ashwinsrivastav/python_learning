ransomNote = "aa" ; magazine = "aab"
magazine=magazine.split()
for i in ransomNote:
    if i in magazine:
        magazine.remove(i)
    else:
        print("false")
print("true")