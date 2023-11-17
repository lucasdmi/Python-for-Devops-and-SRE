import os
print(os.environ['HOME'])
vars = os.environ
for v in vars:
    print(v, vars[v])
    if(v == 'USERNAME'):
        test = vars[v]
print('User encontrado: ', test)