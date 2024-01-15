count_list = input()

for symbol in sorted(set(count_list)):
    print(f'{symbol}: {count_list.count(symbol)} time/s')


# 2 solution
# text = list(x for x in input())
# count_list = set(text.copy())
#
# sorted_text = sorted(count_list)
#
# for symbol in sorted_text:
#     print(f'{symbol}: {text.count(symbol)} time/s')
