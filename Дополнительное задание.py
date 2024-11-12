                                #Дополнительное задание - средний бал учащихся


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  #Список оценок учеников
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                          #Список учащихся (множества)
ss=sorted(students)                                                                 #ss=переменная учащихся остортир.
ag=(sum(grades[0]) / len(grades[0]),sum(grades[1]) / len(grades[1]),                #Вычисления для каждого ученика
    sum(grades[2]) / len(grades[2]),sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4]))
AG=dict(zip(ss,ag))                                             #Преобразование и соединение списка и кортежа в словарь
print('Средние балы учеников:',AG)                                                  #Вывод итога


