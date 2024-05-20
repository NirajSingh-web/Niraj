def dictionary():
    dic={
        "name":'niraj',
        "age":20,
        "city":'mumbai'
    }
    print(dic.keys())
    print(dic.values())
    print(dic.get("name"))
    dic2={
        'subject':"branch",
        "data":"kdkkdkfkfdk"
    }
    dic.update(dic2)
    dic.pop("name")
    print(dic)
dictionary()