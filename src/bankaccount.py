# The BankAccount class simulates a bank account

class BankAccount:

    # The __init__ method accepts an argument for
    # the accounts __balance. And it is assigned to
    # the __balance attribute.

    def __init__(self, bal):
        self.__balance = bal

    # The deposit method makes a deposit into the
    # account.

    def deposit(self, amount):
        self.__balance += amount

        # The withdrawal method withdraws an amount
        # from the account.

    def withdrawal(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('ERROR: Insufficient Funds')

        # The get balance method returns the
        # account balance.

    def get_balance(self):
        """
        Returns the account balance.
        :return:
        """
        return self.__balance
