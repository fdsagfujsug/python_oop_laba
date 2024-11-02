class Car:
 color = None # цвет автомобиля
 fuel = None #количество топлива

 def go(self):
  # Команда ехать:
  pass
	
 def turn(self):
  # Команда поворачивать:
  pass

 def stop(self):
 # Команда остановиться:
  pass
myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.go() 
myCar.turn() 
myCar.stop() 
