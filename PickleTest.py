import pickle 


# cars = ["Audi", "BMW", "Maruti Suzuki", "dfjsdkfh" ]
# file = "mycar.pkl"
# fileobj = open(file,'wb') # write in binary mode 
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)

