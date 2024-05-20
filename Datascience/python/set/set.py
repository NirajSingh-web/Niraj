def Set():
    # set is the well defined object and it remove the dublicate data from the collection 
    set_item={"niraj","helo","niraj"}
    print(set_item)
    # crating the new set 
    newset=set()
    newset.add(1)
    print(newset)
    newset.remove(1)
    print(newset)
    newset2={"heelo","heelo",'tokyo','niraj'}
    newset3={'heelo',"neeraj","grnr"}
    combinedset=newset2.union(newset3)
    newset3.update(newset2)
    print(combinedset,newset2)
    intersection=newset2.intersection(newset3)
    difference=newset2.difference(newset3)
    print(intersection,difference)
    print(newset2.isdisjoint(newset3))
    print(newset2.issubset(newset3))
    print(newset2.issuperset(newset3))
    print(newset3.issuperset(newset2))
Set()