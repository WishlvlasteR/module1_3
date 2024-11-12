immutable_var=('Hello',123,True)            #создаем кордеж
print(type(immutable_var),immutable_var)    #выводим кордеж на экран
mutable_list=([321,'list'])                 #создаем список #Задать вопрос
mutable_list.append('year')                 #Добавление в конец списка
mutable_list.extend([2024])                 #Добавление в конец списка подсписка
mutable_list.remove('list')                 #Убираем строку list из списка
mutable_list[0]='Good '                     #меняем int число под нулевым индексом в списке на строку Good
print(type(mutable_list),mutable_list)      #выводим итоговый результат
