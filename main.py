class BankInterest(object):
    def __init__(self, summ, period, perc):
        self.summ = summ
        self.period = period
        self.perc = perc

    def diff_int(self):
        arr = []
        mp_cnt = self.period * 12
        rest = self.summ
        mp_real = self.summ / (self.period * 12.0)
        while mp_cnt != 0:
            mp = mp_real + (rest * self.perc / 1200)
            arr.append(round(mp, 2))
            rest = rest - mp_real
            mp_cnt = mp_cnt - 1
        return arr, round(sum(arr), 2)

    def ann_int(self):
        mp_cnt = self.period * 12
        r = self.perc / 1200.0
        ak = (r * (1 + r) ** mp_cnt) / (((1 + r) ** mp_cnt) - 1)
        mp = self.summ * ak
        total = mp * mp_cnt
        return round(mp, 2), round(total, 2)


if __name__ == '__main__':
    bank = BankInterest(100000, 2, 10)
    print(bank.ann_int())