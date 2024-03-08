
class MachineController:
    code = 0
    machine = None
    rules = None
    perceptions = None

    state = "sin-moneda"
    action = "pedir-moneda"

    def __init__(self,machine,rules,perceptions,states):
        print("Iniciando controlador: "+machine.getName())
        self.machine = machine
        self.rules = rules
        self.perceptions = perceptions
        self.states = states

    def init(self):
        self.perceptions.showPerception()
        perception = input("Enter a perception: ")
        perception = self.perceptions.getPerception(perception)

        self.state = self.updateState(self.state,self.action,perception)
        rule = self.rules.getRule(self.state)
        self.action = rule
        self.task(self.action)
    def updateState(self,state,action,perception):
        return self.states.getState(state,action,perception)

    def rule_Acction(self,perception,default):
        return self.rules.getRule(perception,default)

    def task(self,action):
        print("\n I machine response with action: " + action)
        if(action == "pedir-moneda"):
            self.machine.askForMoney()
        elif(action == "pedir-codigo"):
            self.machine.askCode()
        elif(action in ("servir-c1-esperar","servir-c1=2-esperar","servir-c3-esperar")):
            self.machine.giveSodad(action)