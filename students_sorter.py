lst_in = [
          'Номер;Имя;Оценка;Зачет',
          '1;Портос;5;Да',
          '2;Арамис;3;Да',
          '3;Атос;4;Да',
          '4;д\'Артаньян;2;Нет',
          '5;Балакирев;1;Нет'
         ]

lst_tuple = tuple(
    tuple(int(item) if item.isdigit() else item for item in line.split(';'))
    for line in lst_in
)

t_sorted = tuple(
    (row[1], row[3], row[2], row[0])
    for row in lst_tuple
)


print(t_sorted)