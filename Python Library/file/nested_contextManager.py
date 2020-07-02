import contextlib
# from contextlib import contextmanager

@contextlib.contextmanager
def sqr(n):
    yield n**2
    # print(n**2)
    print("Print")
    
with sqr(3) as x:
    print("Square of 3 is => ",x)

