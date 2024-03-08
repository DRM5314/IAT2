class Rules:
    rules = {
        "sin-moneda": "pedir-moneda",
        "recibi-moneda": "pedir-codigo",
        "sirviendo-c1": "servir-c1-esperar",
        "sirviendo-c2": "servir-c2-esperar",
        "sirviendo-c3": "servir-c3-esperar"
    }

    def __init__(self,rules):
        if(rules!=None):
            print("Update rules")
            self.rules = rules
    def getRule(self,code):
        print("\n Get rule with: ")
        print("Code is: ",code)
        try:
            return self.rules[code]
        except KeyError:
            print("Rule is not exist")
            return code

    def setRule(self,code,value):
        self.rules[code] = value