# x=(50,100)
# for y in x:
#     if y%2!=0:
#         print(y)
    
# x=range(50,100)
# for y in x:
#     if y%2==0:
#         print(y)
def word(a):
    new=""
    i=0
    for x in a:
        if (i<len(a)//2):
            new+=a[i].upper()
            i+=1
        else:
            new+=a[i]
            i+=1
    print(new)
word("pascaline")