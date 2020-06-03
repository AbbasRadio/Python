# To set recursion limit
import sys
sys.setrecursionlimit(200)

print(sys.getrecursionlimit())
i = 0
def fun():
    global i
    i += 1
    print('hello : ',i)
    fun()
fun()