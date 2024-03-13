

# print(mungel)
# print(type(mungel))
#
# # {'apel': '123', 'google': '324', 'Yndex': '3333305'}
#
# mungel={'apel':"123",
#         "google":"324",
#         "Yndex":"3333305",
#         'apel':"5"}
#
# print(mungel)
#
# # {'apel': '5', 'google': '324', 'Yndex': '3333305'}

# обращение по ключу
# print(mungel['apel'])

# провнрка наличия елюча
# name = input()
#
# if name in mungel:
#     print(f'цена акции {name}={mungel[name]}')
# else:
#     print(f'{name} нет в списке')

# print(f'цена акции {mungel.get(input())}')
#get возвращает значеие или None
# print(f'цена акции {mungel.get(input(),"отсутствует")}')

# Yndex
# цена акции 3333305

# vk
# цена акции отсутствует

# mungel["vk"]="200"
# # print(mungel)
#
# mungel.update({"1c":"211111"})

# print(mungel)

# mungel.update({"Yndex":"0"})

# print(mungel)

# del mungel["vk"]
# print(mungel)

# print(mungel.pop("vk"))
# print(mungel)

# print(mungel.popitem())
# print(mungel)

# ('1c', '211111')
# {'apel': '123', 'google': '324', 'Yndex': '0', 'vk': '200'}

mungel={'apel':"123",
        "google":"324",
        "Yndex":"3333305"}


# metods

# print(mungel.keys())
# dict_keys(['apel', 'google', 'Yndex'])


# print(mungel.values())
# dict_values(['123', '324', '3333305'])

# print(mungel.items())
# dict_items([('apel', '123'), ('google', '324'), ('Yndex', '3333305')])

# mungel.clear()
# print(mungel)

# mungel_cost=mungel.copy()
# print(mungel)
#
# {'apel': '123', 'google': '324', 'Yndex': '3333305'}
