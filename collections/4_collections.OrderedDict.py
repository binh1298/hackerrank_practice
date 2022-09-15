from collections import OrderedDict
standard_input = """9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30"""

N = int(input())

ordered_dictionary = OrderedDict()
for i in range(N):
    nameAndPrice = input().split()
    item_name = " ".join(nameAndPrice[:-1])
    net_price = nameAndPrice[len(nameAndPrice)-1]
    if (item_name in ordered_dictionary):
        ordered_dictionary[item_name] = ordered_dictionary[item_name] + \
            int(net_price)
    else:
        ordered_dictionary[item_name] = int(net_price)

[print(f"{list(ordered_dictionary.keys())[i]} {list(ordered_dictionary.values())[i]}")
 for i in range(len(ordered_dictionary))]
