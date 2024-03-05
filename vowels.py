a=input("type text:")
value=["A","a","E","e","I","i","o","O","u","U"]
x=0
y=0
for i in a:
    if i in value:
        x=x+1
    else:
        y=y+1
print(x)
print(y)
    