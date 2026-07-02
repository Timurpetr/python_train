lst_in = ['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан",
          'Арамис=лейтенант', 'Балакирев=рядовой']
rank = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант',
        'капитан', 'майор', 'подполковник', 'полковник']

nes_lst_sort  = list(list(item for item in line.split('=')) for line in lst_in)

lst = sorted(nes_lst_sort , key=lambda item: rank.index(item[1]))

print(lst)