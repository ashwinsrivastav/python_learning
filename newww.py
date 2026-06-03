class Hero:
    def __init__(self,car,bike):
        self.carr=car
        self.bike=bike
    def show(self):
        print(self.carr,self.bike)
        self.price()
    def price(self):
        if self.carr=="honda":
            print("20 lakhs")
        else:
            print("not defined")

ashwin=Hero("honda","bullet")
rahul=Hero("mercedes","BMW")
#Hero.show(ashwin)
rahul.show()
print(ashwin.carr)