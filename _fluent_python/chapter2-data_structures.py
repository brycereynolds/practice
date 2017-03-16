from pprint import pprint

print("")
print("")
print("###### TUPLES ######")

metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)), 
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
pprint(metro_areas)

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


# Named tuples
# The collections.namedtuple function is a factory that produces subclasses of typle
# enhanced with field names and a class name --- very helpful for debugging.
print("")
print("")
print("###### NAMED TUPLES ######")

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
print(LatLong._fields)

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# delhi = City._make(delhi_data)
delhi = City(*delhi_data)
print(delhi)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print('{0}:{1}'.format(key, value))


print("")
print("")
print("###### SLICES ######")
l = list(range(10))
print(l)

l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

l[3::2] = [11,22]
print(l)

# l[2:5] = 100

l[2:5] = [100]
print(l)

print("")
print("")
print("###### USING + * WITH SEQUENCES ######")
l = [1, 2, 3]
print(l)

print(l * 5)


print("")
print("")
print("###### BULDING LISTS OF LISTS ######")

print("correct_board")
board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

print("wrong_board")
wrong_board = [['_'] * 3] * 3
print(wrong_board)
wrong_board[1][2] = 'X'
print(wrong_board)


print("")
print("")
print("###### IN PLACE WITH *= += ######")

l = [1,2,3]
print(id(l))

l *= 2
print(id(l))

l = (1,2,3)
print(id(l))

l *= 2
print(id(l))

print('Repeated concatenation of immutable sequences is inefficient, because instead of just appending new items, the interpreter has to copy the whole target sequence to create a new one with the new items concatenated5"0')

print("")
print("")
print("###### list.sort and sorted ######")
print('list.sort is an in-place sort')
print("")
print('Functions or methods that change an object in-place should return None to make it clear to the caller that the object itself was changed, and no new object was created.')

print("")
print("")
print("###### managing ordered sequences w/ bisect ######")
print('The bisect module offers two main functions - bisect and insort - that use the binary search algorithm to quickly find and insert items in any sorted sequence.')
print('')
print('See this recipe for an easy recipe over using native bisect functions:')
print('http://code.activestate.com/recipes/577197-sortedcollection/')

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


bisect_fn = bisect.bisect

print('DEMO:', bisect_fn.__name__)
print('haystack -> ', ' '.join(['{0:2d}'.format(n) for n in HAYSTACK]))
demo(bisect_fn)
print('')
print('')

print('Given a test score, grade returns the corresponding letter grade.')
def grade(score, breakpoints = [60,70,80,90], grades='FDCBA'):
    position = bisect.bisect(breakpoints, score)
    return grades[position]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
print('')
print('Use functions from bisect as a faster replacement for the index method when searching through long ordered sequences of numbers.')


print('')
print('')
print('###### inserting with bisect.insort ######')

import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('{0:2d} -> {1}'.format(new_item, my_list))





print('')
print('')
print('###### Arrays: When list is not the answer ######')

print('')
print('Creating, saving and loading a large array of 10 million random floats.')
print('')
print('//commented out')

import array

# floats = array.array('d', (random.random() for i in range(10**7)))
# print(floats[-1])

# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()

# floats2 = array.array('d')
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10**7)
# fp.close()

# print(floats2[-1])
# print(floats2 == floats)
print('')
print('File size is exactly 80,000,000 bytes (8 bytes per double, zero overhead)')
print('')
print('Another fast and more flexible way of saving numeric data is the pickle module for object serialization. Saving an array of floats with pickle.dump is almost as fast as with array.tofile, but pickle handles almost all built-in types, including complex numbers, nested collections and even instances of user defined classes automatically - if they are not too tricky in their implementation.')

print('')
print('')
print('###### Arrays: Using memorview for large datasets ######')
print('')
print('A memoryview is essentially a generalized NumPy array structure in Python itself (without the math). It allows you to share memory between data-structures (things like PIL images, SQLlite databases, NumPy arrays, etc.) without first copying. This is very important for large data sets.')

print('')
print('Example 2-21. Changing a single byte of an array of 16-bit integers')

numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)

memv = memoryview(numbers)

print(len(memv))
print(memv[0])

# Create memv_oct by casting the elements of memv to typecode 'B' (unsigned char).
memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers)

print('')
print('')
print('###### NumPy and SciPy ######')
print('')
print('IF you are doing advanced numeric processing in arrays, then you should be using the NumPy and SciPy libraries.')

import numpy

a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)

a.shape = 3, 4
print(a)
print(a[2])
print(a[2][2])
print(a[2, 2])

# Get column at index 1
print(a[:,1])

print(a.transpose())



print('')
print('')
print('###### Dequeues and other queues ######')
print('')
print('The class collections.dequeue is a thread-safe, double-ended queue designed for fast inserting and removing from both ends.')


from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

