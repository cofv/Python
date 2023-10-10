import random
class Lotteri:
    def __init__(self):
        self.list_vinster = [
         "hundra kubik tvål",
         "Ett vildsvin",
         "200 kubik kattmat",
         "zaztava m70 fullautomatisk",
         "mjöl",
         "röd dacha",
         "bluecatsmurf",
         "Kommunistisk revolution med dina kamrater",
         "En laddad rpg 7 och en skåpbil med borgarjävlar i",
         "VÄRLDSREVOLUTION! Långe leve friheten och kommunismen!",
         "Lenin, Marx, Engels, El Che, Castro, Allende, Luxembourg, Trotzky, Stalin, Ho Chi Ming och Mao Ze Tong kommer tillbaka till liv!"
    ]
    def get_vinst(self):
        #print("getvista")
        slumptal = random.randint(0, 10)
        return self.list_vinster[slumptal]
        

