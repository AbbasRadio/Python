import time
def search():
    book = "This is me abbas ali radio wala. I'm a web developer"
    while True:
        text = yield
        if text in book:
            print("Yes Found")
        else:
            print('Not Found')
check = search()
# check.__next__()
next(check)
check.send('abbas')
check.send('web')
check.send('deevloper')
check.send('developer')