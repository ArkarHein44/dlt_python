class Car:
    SPEED_LIMIT:float = 150

    def __init__(self, brand:str)-> None:
        self.brand = brand
    
    def drive(self,*, speed:float)-> None: # keyword-only Arguments. use by asterisk(*) key
        if speed > self.SPEED_LIMIT:
            print(f'Speed Limit reached : Driving at {self.SPEED_LIMIT} km/h')
        else:
            print(f'Driving at {speed} km/h')

def main()-> None:
    bmw:Car = Car("BMW")
    bmw.drive(speed = 150)

    bmw.SPEED_LIMIT = 170
    bmw.drive(speed = 160)
    bmw.drive(speed = 200)

if __name__ == "__main__":
    main()

# 23CI