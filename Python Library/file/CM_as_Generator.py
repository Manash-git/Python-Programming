from contextlib import contextmanager

@contextmanager
def manage_file(name):
    try:
        f=open(name,'a')
        yield f
    finally:
        f.close()

with manage_file("hello.txt") as cm_f:
    cm_f.write("Hello World\n")
    cm_f.write("Blah Blah ...\n")