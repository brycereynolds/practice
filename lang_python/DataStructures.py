def p(val):
    print(val)

sets = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
p("sets ==> {0}".format(sets))

a = set('abracadabra')
b = set('alacazam')
p("a ==> {0}".format(a))
p("b ==> {0}".format(b))
p("Letters in a but not in b")
p("a - b ==> {0}".format(a - b))

p("Letters in either a or b")
p("a | b ==> {0}".format(a | b))

p("Letters in both a and b")
p("a & b ==> {0}".format(a & b))

p("Letters in a or b but not both")
p("a ^ b ==> {0}".format(a ^ b))



p("")
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
p("fruits ==> {0}".format(fruits))

p("fruits.count('apple') ==> {0}".format(fruits.count('apple')))

p("fruits.index('banana') ==> {0}".format(fruits.index('banana')))

p("fruits.index('banana', 4) ==> {0}".format(fruits.index('banana', 4)))

p("fruits.reverse() ==> {0}".format(fruits.reverse()))
p("fruits ==> {0}".format(fruits))

p("fruits.append('grape') ==> {0}".format(fruits.append('grape')))
p("fruits ==> {0}".format(fruits))

p("fruits.sort() ==> {0}".format(fruits.sort()))
p("fruits ==> {0}".format(fruits))

p("fruits.pop() ==> {0}".format(fruits.pop()))
p("fruits ==> {0}".format(fruits))

p("")
stack = [3, 4, 5]
p("stack ==> {0}".format(stack))

p("stack.append(6) ==> {0}".format(stack.append(6)))
p("stack.append(7) ==> {0}".format(stack.append(7)))

p("stack ==> {0}".format(stack))

p("stack.pop() ==> {0}".format(stack.pop()))
p("stack ==> {0}".format(stack))


p("")
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
p("queue ==> {0}".format(queue))

p("queue.append('Terry') ==> {0}".format(queue.append('Terry')))
p("queue.append('Graham') ==> {0}".format(queue.append('Graham')))

p("queue ==> {0}".format(queue))

p("queue.popleft() ==> {0}".format(queue.popleft()))

p("")
squares = []
for x in range(10):
    squares.append(x**2)
p("squares ==> {0}".format(squares))

squares = [x**2 for x in range(10)]
p("squares ==> {0}".format(squares))

squares = list(map(lambda x: x**2, range(10)))
p("squares ==> {0}".format(squares))

p([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
p([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x is y])

p("")
vec = [-4, -2, 0, 2, 4]
p("vec ==> {0}".format(vec))

p("[x*2 for x in vec] ==> {0}".format([x*2 for x in vec]))

p("[x*2 for x in vec if x >= 0] ==> {0}".format([x*2 for x in vec if x >= 0]))

p("[abs(x) for x in vec] ==> {0}".format([abs(x) for x in vec]))

p("[(x, x**2) for x in range(6)] ==> {0}".format([(x, x**2) for x in range(6)]))

p("[(x, y) for x in range(3) for y in range(2)] ==> {0}".format([(x, y) for x in range(3) for y in range(2)]))

# p("len([(a, b, c, d) for a in range(10) for b in range(10) for c in range(10) for d in range(10)]) ==> {0}".format(len([(a, b, c, d) for a in range(10) for b in range(10) for c in range(10) for d in range(10)])))

p("")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
p("matrix ==> {0}".format(matrix))

p("[i for i in range(4)] ==> {0}".format([i for i in range(4)]))
p("[row for row in matrix] ==> {0}".format([row for row in matrix]))

p("[[row[i] for row in matrix] for i in range(4)] ==> {0}".format([[row[i] for row in matrix] for i in range(4)]))
p("")
p("Another usage of the *l idiom is to unpack argument lists when calling a function.")
p("matrix ==> {0}".format(matrix))
p("list(zip(matrix)) ==> {0}".format(list(zip(matrix))))
p("list(zip(*matrix)) ==> {0}".format(list(zip(*matrix))))
p("list(zip([1,2,3,4],[5,6,7,8])) ==> {0}".format(list(zip([1,2,3,4],[5,6,7,8]))))
p("list(zip(*[[1,2,3,4],[5,6,7,8]])) ==> {0}".format(list(zip(*[[1,2,3,4],[5,6,7,8]]))))

first, *rest = [1,2,3,4]
p("first, *rest = [1,2,3,4]")
p("first ==> {0}".format(first))
p("rest ==> {0}".format(rest))

p("")
def foo(x,y,z):
    p("x={0}".format(x))
    p("y={0}".format(y))
    p("z={0}".format(z))

mylist = [1,2,3]
p("mylist ==> {0}".format(mylist))
p("foo(*mylist)")
foo(*mylist)

mydict = {'x':1, 'y':2, 'z':3}
p("mydict ==> {0}".format(mydict))
p("foo(*mydict)")
foo(*mydict)

mydict = {'x':1, 'y':2, 'z':3}
p("mydict ==> {0}".format(mydict))
p("foo(**mydict)")
foo(**mydict)


mytuple = (1,2,3)
p("mytuple ==> {0}".format(mytuple))
p("foo(*mytuple)")
foo(*mytuple)

p("")

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

p("questions ==> {0}".format(questions))
p("answers ==> {0}".format(answers))
p("for q, a in zip(questions, answers):")
for q, a in zip(questions, answers):
    p("What is your {0}?  It is {1}.".format(q, a))





