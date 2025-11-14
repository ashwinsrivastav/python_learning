def bulb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=[1]*n;count=2
        while count<=n:
            for repeater in range(-1,len(a),count):
                try:
                    a[count+repeater]=int((not a[count+repeater]))
                except IndexError:
                    break
            count+=1
        return a.count(1)
n=int(input("enter the number"))
print(bulb(n))