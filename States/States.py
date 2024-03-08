class States:
    states = {
        ("sin-moneda", "pedir-moneda", "moneda"): "recibi-moneda",
        ("recibi-moneda", "pedir-codigo", "c1"): "sirviendo-c1",
        ("recibi-moneda", "pedir-codigo", "c2"): "sirviendo-c2",
        ("recibi-moneda", "pedir-codigo", "c3"): "sirviendo-c3",
        ("servido-c1", "servir-c1-esperar", "servido"): "sin-moneda",
        ("servido-c2", "servir-c2-esperar", "servido"): "sin-moneda",
        ("servido-c3", "servir-c3-esperar", "servido"): "sin-moneda",
        ("recibi-moneda", "pedir-codigo", "moneda"): "recibi-moneda",
    }

    def __init__(self,states):
        if(states!=None):
            print("Update default states")
            self.states = states

    def getState(self,state,action,perception):
        print("\nGet state with: ")
        print("State is: ", state)
        print("Action is: ",action)
        print("Perception is: ", perception)
        try:
            return self.states[(state,action,perception)]
        except KeyError:
            return "sin-moneda"