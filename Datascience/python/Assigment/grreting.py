import datetime
def greeting():
    hours=datetime.datetime.now().hour
    print(hours)
    if 0<=hours<12:
        print("good Morning")
    elif 12 <= hours<17:
        print("good afternoon")
    elif 17 <= hours<21 :
        print("good Evening")
    else:
        print("Good night")

greeting()