from vendingMachine.Machine import Machine
from States.Rules import Rules
from States.Perception import Perception
from States.States import States
from MachineController.MachineController import MachineController

machine = Machine("Robot 1")
rules = Rules(None)
perceptions = Perception(None)
states = States(None)
machineController = MachineController(machine, rules, perceptions, states)
in_ = "n"

while(True):
    machineController.init()
