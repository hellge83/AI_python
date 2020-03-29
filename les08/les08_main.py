import requests

url = 'https://api.github.com/users/hellge83'

class Some:
    var1 = 2

    def __init__(self, a):
        self.var_a = a

    def some_sum(self, b):
        if self.var_a > b:
            return self.var_a + b
        raise SomeError('var b <= a')

    @staticmethod
    def my_func(a, b):
        return a + b

    @classmethod
    def my_cls_m(cls, *args):
        return [cls(itm) for itm in args]

class SomeError(Exception):
    def __init__(self, text='Some Error'):
        self.text = text

    def __str__(self):
        return self.text

user = requests.get(url)

a = Some(5)
b = Some(2)
# raise SomeError('Some unique error')
c = Some(3)

i = 0
while True:

    try:
        d = a.some_sum(i)
        break
    except SomeError:
        i +=1
    finally:
        print('Final', i)
else:
    print('else')

print(1)

if __name__ == '__main__':
    pass