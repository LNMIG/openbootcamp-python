import pickle

class Vehicle:
    wheels = 0
    doors = 0
    engine = 0

    def __init__(self,wheels,doors,engine):
        self.wheels = wheels
        self.doors = doors
        self.engine = engine

vehicle = Vehicle(4,4,1500)

f = open('testVehicle.bin', 'wb')
pickle.dump(vehicle, f)
f.close()

f = open('testVehicle.bin', 'rb')
data = pickle.load(f)
f.close()
# print(type(data))
print(f'The vehicle has {data.wheels} wheels, {data.doors} doors and the engine is of {data.engine} centiliters')
