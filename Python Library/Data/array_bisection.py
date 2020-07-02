
import bisect

values= [5,9,10,15,20]

# print(bisect.bisect(values,7))
# print(bisect.bisect(values,5))
# print(bisect.bisect_right(values,5))
# print(bisect.bisect_left(values,5))

# print(bisect.bisect(values,8))
# print(bisect.bisect_right(values,8))
# print(bisect.bisect_left(values,8))

# bisect.insort(values,4)
# bisect.insort_left(values,4)
bisect.insort_right(values,5)
print(values)




