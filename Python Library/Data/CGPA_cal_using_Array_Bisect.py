import bisect

breakpoints= [60,70,80,90]

print(bisect.bisect(breakpoints,90))

grades='FDCBA'

print(grades[4])

scores= [83,90,55,99,79]


def cgpa(n):
    cutoff= bisect.bisect(breakpoints,n)
    return grades[cutoff]

result = [cgpa(i) for i in scores]

print(result)


# def cgpa(n):
#     cutoff= bisect.bisect_right(breakpoints,n)
#     return grades[cutoff]

# result = [cgpa(i) for i in scores]

# print(result)


# def cgpa(n):
#     cutoff= bisect.bisect_left(breakpoints,n)
#     return grades[cutoff]

# result = [cgpa(i) for i in scores]

# print(result)