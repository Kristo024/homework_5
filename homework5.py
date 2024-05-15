my_list=['apple','banana','kiwi','orange','lemon','pear']
print('my-list: ', my_list)
print('first element: ', my_list[0])
print('last element: ', my_list[-1])
print('sublist: ', my_list[2:4]) # c третьего ДО пятого.
my_list[2]='avocado'
print('modified list: ', my_list)
#словарь
my_dict={}
a={'apple':'яблоко','banana':'банан','kiwi':'киви'}
my_dict=a
print('my_dict:', my_dict)
print("kivi - ", my_dict['kiwi'])
my_dict['grape']='виноград'
print("modified dictionary: ", my_dict)