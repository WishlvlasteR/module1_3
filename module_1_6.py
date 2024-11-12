                                    #Работа со словарями
my_dict={'Alexa':1990, 'Alex':1992,'Sasha':1988}
print('Словарь №1',my_dict)
print('Год рождения студента Alexa из первого словаря:',(my_dict['Alexa']))
print(my_dict.get('asd','Данные о студенте "asd" в словаре №1 не найдены'))
my_dict.update({'Nata':1900,'Timur':1993})
Sasha=my_dict.pop('Sasha')
print('Год рождения студента, Sasha:',Sasha)
print(my_dict)
                                    #Работа с множествами
my_set={1,2,0.2,3,False,4,3,2,False,1, 'U','U',False,2,0.2}
print(my_set)
my_set.update({'V',True,8})             #Почему не добавилось True?
my_set.remove(2)
print(my_set)