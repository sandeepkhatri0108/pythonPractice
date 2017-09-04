class Drawer:

    def __init__(self):
        self.return_money = []
        self.penny = 0.01
        self.nickel = 0.05
        self.dime = 0.1
        self.quarter = 0.25
        self.one = 1
        self.five = 5
        self.ten = 10
        self.twenty = 20
        self.hundred = 100

    def checkCashRegister(self, price, cash, cid):
        penny_left = list(money for currency, money in cid if currency == "PENNY")[0]
        nickel_left = list(money for currency, money in cid if currency == "NICKEL")[0]
        dime_left = list(money for currency, money in cid if currency == "DIME")[0]
        quarter_left = list(money for currency, money in cid if currency == "QUARTER")[0]
        one_left = list(money for currency, money in cid if currency == "ONE")[0]
        five_left = list(money for currency, money in cid if currency == "FIVE")[0]
        ten_left = list(money for currency, money in cid if currency == "TEN")[0]
        twenty_left = list(money for currency, money in cid if currency == "TWENTY")[0]
        hundred_left = list(money for currency, money in cid if currency == "ONE HUNDRED")[0]

        total_money = penny_left + nickel_left + dime_left + quarter_left + one_left + five_left + ten_left + \
                      twenty_left + hundred_left

        change_due = cash - price

        if change_due > total_money:
            return "Insufficient Funds"

        elif change_due == total_money:
            return "Closed"

        elif change_due == 0:
            return "Not required"

        else:
            while change_due != 0:
                if (hundred_left > 0) & (change_due - self.hundred >= 0):
                    change_due -= self.hundred
                    hundred_left -= self.hundred
                    row = [self.hundred, "ONE HUNDRED", self.hundred]
                    self.return_money.append(row)
                elif (twenty_left > 0) & (change_due - self.twenty >= 0):

                    change_due -= self.twenty
                    twenty_left -= self.twenty
                    row = [self.twenty, "TWENTY", self.twenty]
                    self.return_money.append(row)
                elif (ten_left > 0) & (change_due - self.ten >= 0):
                    change_due -= self.ten
                    ten_left -= self.ten
                    row = [self.ten, "TEN", self.ten]
                    self.return_money.append(row)
                elif (five_left > 0) & (change_due - self.five >= 0):
                    change_due -= self.five
                    five_left -= self.five
                    row = [self.five, "FIVE", self.five]
                    self.return_money.append(row)
                elif (one_left > 0) & (change_due - self.one >= 0):
                    change_due -= self.one
                    one_left -= self.one
                    row = [self.one, "ONE", self.one]
                    self.return_money.append(row)
                elif (quarter_left > 0) & (change_due - self.quarter >= 0):
                    change_due -= self.quarter
                    quarter_left -= self.quarter
                    row = [self.quarter, "QUARTER", self.quarter]
                    self.return_money.append(row)
                elif (dime_left > 0) & (change_due - self.dime >= 0):
                    change_due -= self.dime
                    dime_left -= self.dime
                    row = [self.dime, "DIME", self.dime]
                    self.return_money.append(row)
                elif (nickel_left > 0) & (change_due - self.nickel >= 0):
                    change_due -= self.nickel
                    nickel_left -= self.nickel
                    row = [self.nickel, "NICKEL", self.nickel]
                    self.return_money.append(row)
                else:
                    change_due -= self.penny
                    penny_left -= self.penny
                    row = [self.penny, "PENNY", self.penny]
                    self.return_money.append(row)

            # Sum all having same first value
            d = {}
            for sub in self.return_money:
                d.setdefault(tuple(sub[:2]),[]).append(sub[2:])

            self.return_money = [k + tuple(map(sum, zip(*v))) for k, v in d.items()]
            self.return_money = sorted(self.return_money, key=lambda x: int(x[0]), reverse=True)
            self.return_money = [(sub[1], sub[2]) for sub in self.return_money]

            return self.return_money

if __name__ == '__main__':

    objDrawer = Drawer()
    output = objDrawer.checkCashRegister(19.50, 20.00, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25],
                                              ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00],
                                              ["ONE HUNDRED", 100.00]])

    print ("output")
