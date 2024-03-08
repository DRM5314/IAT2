class Perception:
    Perception = {
        "moneda":"moneda",
        "c1":"c1",
        "c2":"c2",
        "c3":"c3",
        "servido":"servido",
    }

    def __init__(self, perceptions):
        if(perceptions!=None):
            print("Update perception")
            self.Perception = perceptions


    def getPerception(self,perception):
        try:
            return self.Perception[perception]
        except KeyError:
            print("Perception input not valid!")
            return None
        return self.Perception

    def showPerception(self):
        print("\n Perceptions available: moneda, c1, c2, c3, servido: ")