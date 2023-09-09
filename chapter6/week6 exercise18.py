# Write the function f2c(t) designed to return the integer value of the nearest degree Celsius for given temperature in Fahrenheit.

def f2c(t):
    celcius = round(((t-32)*5)/9)    # round fonksiyonu tam sayı kısmını verir.

    return celcius

print(f2c(212))