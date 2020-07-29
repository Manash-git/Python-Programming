# stack : LIFO
lst_stack= [5,2,9,4,3,5,515]
# Apend() -> for last in
# pop() -> for last out

print(lst_stack.pop())
print(lst_stack)
lst_stack.append(20)
print(lst_stack)

# Queue : LILO
# Here append() -> is same for last in
# pop(0) -> here is for first element out

lst_queue = [5,2,9,4,3,5,515]
# lst_queue.sort()
lst_queue.reverse()
print(lst_queue)
# print(lst_queue[::-1])

print(lst_queue.pop(0))
print(lst_queue)
lst_queue.append(121)
print(lst_queue)