#convert from degrees kelin to degrees Celsius and Fahrenheit.
conversion_celcius = 273.15
conversion_fahrenheit = (273.15) * 9/5 + 32

my_degrees_in_kelvin = [1, 6, 8, 12, 16, 18]
my_degrees_in_celcius = [(round(degrees - conversion_celcius, 2)) for degrees in my_degrees_in_kelvin] 
my_degrees_in_fahrenheit = [(round((degrees - conversion_celcius)*9/5 +32, 2)) for degrees in my_degrees_in_kelvin] 

print(my_degrees_in_celcius)
print(my_degrees_in_fahrenheit) 