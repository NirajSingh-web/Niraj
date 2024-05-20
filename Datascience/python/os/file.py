# write method
f=open("./os/Text.txt","w")
f.write("hello world")
# append method
f=open("./os/Text.txt","a")
f.write(" djfjjdsjd")
# read method
f=open("./os/Text.txt","r")
content= f.read().split(" ")
def getdata(x):
    print(x)
    return x
content=list(map(getdata,content))
content=list(map(lambda x:x,content))
print(content)
filtereddata=list(filter(lambda x:x=="hello",content))
print(filtereddata)
f.close()
