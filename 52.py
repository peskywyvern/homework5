names = ['James', 'Bruce', 'Jervis', 'Edward']
name = input('Name: ')
if name not in names:
    print('Not found')
else:
    if names.index(name) % 2 == 0:
        print("It's all good")
    else:
        names.remove(name)
        print(names)
