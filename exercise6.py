print("What fahrenheit temperature would you like to convert?")
fahr = int(input())

def cels (fahr):
    return (fahr - 32) * (5/9)

print("{}°F is {:.0f}°C.".format(fahr, cels(fahr)))