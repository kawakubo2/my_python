class Car:
    def __init__(self, name, capacity, fuel, nenpi):
        self.name = name
        self.capacity = capacity
        self.fuel = fuel
        self.nenpi = nenpi

    def drive(self, hour):
        if self.fuel >= hour * self.nenpi:
            self.fuel -= hour * self.nenpi
        else:
            print('燃料が足りません')

    def refill(self, fuel):
        if self.fuel + fuel <= self.capacity:
            self.fuel += fuel
        else:
            print('容量を超えています')
    
    def get_fuel(self):
        return self.fuel
            
if __name__ == '__main__':
    car = Car('カローラ', 40, 40, 1)
    while True:
        sw = int(input('1.運転 2.給油 9.終了: '))
        if sw == 9:
            break

        if sw == 1:
            hour = int(input('何時間乗りますか: '))
            car.drive(hour)
            print('燃料:{}'.format(car.get_fuel()))
        elif sw == 2:
            litter = int(input('何リットル給油しますか: '))
            car.refill(litter)
            print('燃料:{}'.format(car.get_fuel()))
        else:
            print('1または2を選択してください')

    