import time
import resource


# resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

# time_start = time.clock()
# #run your code
# time_elapsed = (time.clock() - time_start)
# print(time_elapsed)

usage = resource.getrusage(resource.RUSAGE_SELF)

for name, desc in [
    ('ru_utime', 'User time'),
    ('ru_stime', 'System time'),
    ('ru_maxrss', 'Max. Resident Set Size'),
    ('ru_ixrss', 'Shared Memory Size'),
    ('ru_idrss', 'Unshared Memory Size'),
    ('ru_isrss', 'Stack Size'),
    ('ru_inblock', 'Block inputs'),
    ('ru_oublock', 'Block outputs'),
    ]:
    print ('%-25s (%-10s) = %s' % (desc, name, getattr(usage, name)))