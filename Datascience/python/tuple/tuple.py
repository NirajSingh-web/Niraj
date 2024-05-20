def Tuple_method():
    Tuple=("n","s","9",10)
    numof10item=Tuple.count(10)
    indexofn=Tuple.index("n")
#    modified tupe 
    convertedlist=list(Tuple)
    convertedlist.append("10")
    newtuple= tuple(convertedlist)
    print(newtuple)

Tuple_method()