

s = "(]"

def isValid(list):
        
        stack = []

        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for char in s:
            if char not in close_to_open:
                stack.append(char)
            elif not stack or stack[-1] != close_to_open[char]:
                return False
            else:
                stack.pop()

        return len(stack) == 0


isValid(s)


# print("hello")



listtest = ["hello", "my", "name", "is", "john"]
emptylist = []

# emptylist.append(listtest.pop())


# print(listtest)
# print(emptylist)



for words in listtest:
     if words not in emptylist:
          emptylist.append(words)
          print(emptylist)