# class Demo:
#
#     def session(self):
#         print("demo class")
# class Sample:
#     def __init__(self):
#         self.demo_obj=Demo()
# s=Sample()
# s.session()


# class Demo:
#     def spam(self):
#         print("in spam")
#
# class Sample:
#     def __init__(self):
#         self.demo_obj = Demo()      # composition
#     def display(self):
#         print("in display")
#
#
# s=Sample()
# s.display()
# s.demo_obj.spam()

# class Consolelogger:
#     def  log(self,message):
#         self.message=message
#
#
# class TextFileLogger:
#     def __init__(self,file_obj):
#         self.file_obj=file_obj
#
#     def log(self,message):
#         file_obj.write(message + "\n")
#
#
# class Filtteredlogger:
#     def __init__(self,pattern,obj):
#         self.pattern=pattern
#         self.obj=obj
#     def log(self,message):
#         if self.pattern in message:
#             self.obj.log(message)
#             print(f"it is a {self.pattern} message")
#         else:
#             print("it does nt have pattern in msg")
#
# cl=Consolelogger()
# fl=Filtteredlogger("info",cl)
# fl.log("this is info message")



# class Stack:
#     def __init__(self):
#         self.items=[]
#     def insert_item(self,item):
#         self.items.append(item)
#     def remove_item(self,item):
#         self.items.remove(item)
#
#     def len_stack(self):
#         print(len(self.items))
#
# class NumberStack:
#     def __init__(self):
#         self.stack=Stack()
#
#     def insert_item(self,item):
#         if not isinstance(item, (int, float)):
#             raise Exception("it is not a number")
#         self.stack.insert_item(item)
#     def remove_item(self,item):
#         self.stack.remove_item(item)
#
#
# n=NumberStack()
# n.insert_item(12345)
# print(n.stack.items)

# class Stack:
#     def __init__(self):
#         self.items=[]
#     def insert_item(self,item):
#         self.items.append(item)
#     def remove_item(self,item):
#         self.items.remove(item)
#
#     def len_stack(self):
#          print(len(self.items))
#
# class NumberStack:
#     def __init__(self,obj):
#         self.obj=obj
#
#     def insert_item(self,item):
#         if not isinstance(item, (int, float)):
#             raise Exception("it is not a number")
#         self.obj.insert_item(item)
#     def remove_item(self,item):
#         self.obj.remove_item(item)
#
# s=Stack()
# n=NumberStack(s)
# n.obj.insert_item(3)
# print(n.obj.items)















