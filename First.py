

master = {}
key_check = master.keys()
stations = [11, 12, 13, 14, 15, 16, 17]


class Uerror(Exception):
    pass


def user_auth(f):

    def wrap(*args, **kwargs):

        if args[1] in key_check:
            amt = f(args[0], args[1])
            return amt
        else:
            raise Uerror("Invalid User")
    return wrap


class Metro:

    def __init__(self, phone):

        self.min = 15
        self.damt = 20
        self.disc = 5
        self.cost = 5
        self.phone = phone
        self.start = 0
        self.end = 0

    def new(self, phone):
        try:
            if phone not in key_check:
                master[phone] = {'amount': self.damt, 'trips': 0, "discount_fg":0, "station_cnt": 0}
                print("created New Card for: ", phone)
            else:
                print("A user should be able to purchase 1 card only.")
        except Exception as e:
            print(e)

    @user_auth
    def check_bal(self, a):
        amt = master[a]['amount']
        return amt

    def topup(self, phone, amt):
        amt_master = self.check_bal(phone)
        amt_master += amt
        master[phone]['amount'] = amt_master

    def gate_open(self, phone):
        print("gate open")

    def check_min_bal(self, phone):

        amt_master = self.check_bal(phone)
        if self.min > amt_master:
            raise Uerror("Low Balance")

    def entry(self, phone, station):
        self.start = stations.index(station)
        print("Welcome to station: ", station, self.start)
        print("*********** Enter Dore Open *****************")

    def mexit(self, phone, station):
        amt_master = self.check_bal(phone)
        self.end = stations.index(station)
        distance = abs(self.end - self.start)
        station_cnt = master[phone]['station_cnt']
        total = station_cnt + distance
        cost = self.cost * distance if total > self.disc else self.min
        print(distance, "distance", total)

        if total >= self.disc:
            new_station_cnt = abs(total - self.disc)
            check_discount = True
        else:
            new_station_cnt = total
            check_discount = False

        if check_discount:
            tmp = (cost * self.disc) / 100
            tmp1 = abs(tmp - cost)
            remain = amt_master - tmp1
        else:
            remain = amt_master - cost
        if remain < 0:
            print("Please Check balance")
            print("*********** Not Open *****************")
        else:
            master[phone]['station_cnt'] = new_station_cnt
            master[phone]['amount'] = remain
            print("*********** Exit Open *****************")
        print(master)

# Please Uncomment the below Method Calls one by one to see the output 



# obj = Metro(77950)
# obj.new(77950) # New user
# print(master)
# print("Balence Amount : ", obj.check_bal(77950)) # Balance Check
# obj.entry(77950, 12) # Trip start
# obj.mexit(77950, 13) # Ended with Minimum Cost
# 
# print("Balence Amount : ", obj.check_bal(77950))
# # #
# obj.entry(77950, 12) # Trip start with out topup
# obj.mexit(77950, 13) # Try exit with low balance
# print("Balence Amount : ", obj.check_bal(77950))
# obj.topup(77950, 21)
# obj.mexit(77950, 13) # Try after topup
# 
# 
# obj.entry(77950, 11) # Trip start with out topup
# obj.mexit(77950, 17) # Try exit with low balance
# print(obj.check_bal(77950))
# obj.topup(77950, 21)
# obj.mexit(77950, 17) # Try after topup
