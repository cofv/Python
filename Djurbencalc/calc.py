def calculate(a,b,c):
    kyckling = 2
    grisar = 4
    kossor = 4
    kyckben = a*kyckling
    grisben = b*grisar
    kossorben = c*kossor
    Total_legs = kyckben+grisben+kossorben
    print(Total_legs)

a = int(input("\n\tHur många kycklingar har du? "))
b = int(input("\n\tHur många grisar har du? "))
c = int(input("\n\tHur många kossor har du? "))

print(calculate(a, b, c))



#a lika med kyckling, b lika med grisar, c lika med kossor.
