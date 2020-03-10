goods = []
while True:
    length = input('input length of list:\n')
    if not length.isdigit():
        continue
    for i in range(0, int(length)):
        dict = {'item_name': '', 'item_price': '', 'item_qty': '', 'item_unit': ''}
        dict['item_name'] = input('item_name')
        dict['item_price'] = input('item_price')
        dict['item_qty'] = input('item_qty')
        dict['item_unit'] = input('item_unit')
        lst = []
        lst.extend([i+1, dict])
        my_tuple = tuple(lst)
        goods.append(my_tuple)
    item_name = set()
    item_price = set()
    item_qty = set()
    item_unit = set()
    for i in range(0, int(length)):
        item_name.add(goods[i][1]['item_name'])
        item_price.add(goods[i][1]['item_price'])
        item_qty.add(goods[i][1]['item_qty'])
        item_unit.add(goods[i][1]['item_unit'])

    pivot = {'item_name': list(item_name), 'item_price': list(item_price), 'item_qty': list(item_qty), 'item_unit': list(item_unit)}

    print(goods)
    print(pivot)
    break