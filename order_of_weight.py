lst_in = [
          'ножницы=100',
          'котелок=500',
          'спички=20',
          'зажигалка=40',
          'зеркальце=50'
         ]

lst_dict = {val:int(idx) for item in lst_in for val, idx in [item.split("=")]}

lst_result = [k for k,v in sorted(lst_dict.items(), key=lambda item: item[1], reverse=True)]

print(*lst_result)