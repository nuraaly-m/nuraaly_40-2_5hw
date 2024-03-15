class Bank:
    def __init__(self,name,age,money,key):
        self._name=name
        self._age=age
        self.__money=money
        self.__key=key

    def set_name(self,name):...

    def get_name(self):...

class Kyrgyzbanks(Bank):
    def get_name(self):
        return self._name

    def set_name(self, x):
        self._name = x

# mbank = Kyrgyzbanks('umar', 12, 1000, 2223)
# print(mbank.get_name())
# mbank.set_name('nuraaly')
# print(mbank.get_name())
# print(mbank._name)

class RskBank(Kyrgyzbanks):
    def get_name(self):
        print('getter method')
        return self._name

    def set_name(self, x):
        print('setter method')
        self._name = x

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name)

# bank = RskBank('nuraaly', 18, 100, 1212)
# bank.name = 'melisbekov'
# print(bank.name)

    def get_age(self):
        print('getter method')
        return self._age

    def set_age(self, x):
        print('setter method')
        self._age = x

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


    def get_money(self):
        print('getter method')
        return self._money

    def set_money(self, x):
        print('setter method')
        self._money = x

    def del_money(self):
        del self._money

    money = property(get_money, set_money, del_money)


    def get_key(self):
        print('getter method')
        return self._key

    def set_key(self, x):
        print('setter method')
        self._key = x

    def del_key(self):
        del self._key

    key = property(get_key, set_key, del_key)

    def __str__(self):
        return (f'name: {self._name}\n'
                f'age: {self._age}\n'
                f'money: {self._money}\n'
                f'key: {self._key}')

