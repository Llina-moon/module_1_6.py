my_dict = {'Anna' : 1998 , 'Alex' : 1990 , 'Bob' : 2001 }
print(my_dict)
print(my_dict['Bob'])
print(my_dict.get('Lola'))

my_dict.update({'Alice' : 1973 ,'Nikolay' : 2003})

a=my_dict.pop('Anna')
print(a)
print(my_dict)


my_set = {'cola', 3,'cola' , 3, 2.18}
print(my_set)

my_set.add(1)
my_set.add(3.14)
my_set.remove(2.18)
print(my_set)
