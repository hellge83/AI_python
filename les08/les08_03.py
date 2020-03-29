class Integer:
    # current_list = []

    def __init__(self, itm):
        self.current_list = []

    def digit_check(self):
        while True:
            next = input('input number or "stop":\n')
            if next == 'stop':
                print(f'Current list: {self.current_list} \n ')
                break
            else:
                try:
                    self.current_list.append(int(next))
                    print(f'Current list: {self.current_list} \n ')
                except:
                    print('It\'s not a digit')
                    # keep = input('input number or "stop":\n')
                    # if keep == 'stop':
                    #     break
                    # itm = Integer(keep)
                    # print(f'Current list: {self.current_list} \n ')
                    print(itm.digit_check())




# x = input('input number:\n')
itm = Integer(1)
print(itm.digit_check())