

stack=[]
#PUSH==========================================================
#No length Boundation in list so No isFull() operation
print("stack befor push operation")
print(stack)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append('h')
stack.append('d')
print("stack after push operation")
print(stack)
#POP=============================================================================
def isemty(stack):
            if stack==[]:
                        return 'true'
            else:
                        return 'false'
def pop(stack):
            if(isemty(stack)=='true'):
                        print("stack is emty")
            else:
                         print(stack.pop())
                         print("After one pop operation")
                         print(stack)

pop(stack)
#################################IMPLEMENTATION OF  STACK USING "'deque"" #########################################################
"""
Python stack can be implemented using deque class from collections module. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
Same methods on deque as seen in list are used, append() and pop().
"""
###########::::::::::---------------------------------------------

from collections import deque
stack=deque()
####################       rest coding are same ###############################
print("stack befor push operation")
print(stack)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append('h')
stack.append('d')
print("stack after push operation")
print(stack)
#POP=============================================================================
def isemty(stack):
            if stack==[]:
                        return 'true'
            else:
                        return 'false'
def pop(stack):
            if(isemty(stack)=='true'):
                        print("stack is emty")
            else:
                         print(stack.pop())
                         print("After one pop operation")
                         print(stack)

pop(stack)



