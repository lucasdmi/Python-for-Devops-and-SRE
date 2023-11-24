import os

print(os.listdir())

os.rename("so.py", "os.py")
print("Successfully renamed. ")


print(os.listdir(os.getcwd()))



#result
#['Test.py', 'so.py', 'Exercise1.py', 'ola.py', 'Exercise2.py', 'rename.py']
#Successfully renamed. 
#['Test.py', 'Exercise1.py', 'ola.py', 'os.py', 'Exercise2.py', 'rename.py']