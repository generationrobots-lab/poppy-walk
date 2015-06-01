import random

class WalkerModule:
    def __init__(self):
        pass
        
    def execute(self, motorPositions, motorNextPositions, phase=""):
        if phase == "right step":
            self.stepRightExecute(motorPositions, motorNextPositions)
        elif phase == "right double support":
            self.doubleSupportRightExecute(motorPositions, motorNextPositions)
        elif phase == "left step":
            self.stepLeftExecute(motorPositions, motorNextPositions)
        elif phase == "left double support":
            self.doubleSupportLeftExecute(motorPositions, motorNextPositions)
            
    def stepRightExecute(self, motorPositions, motorNextPositions):
        pass
        
    def stepLeftExecute(self, motorPositions, motorNextPositions):
        pass
        
    def doubleSupportRightExecute(self, motorPositions, motorNextPositions):
        pass
        
    def doubleSupportLeftExecute(self, motorPositions, motorNextPositions):
        pass
        
        
        
        
class PlayStepModule(WalkerModule):
    def __init__(self, file):
        WalkerModule.__init__(self)
        self.file = file
        
    def execute(self, motorPositions, motorNextPositions):
        print "playing file"
        pass
        #play one step of the file
        
    def footLanded(self):
        #is file finished
        
        r = random.randint(0, 10)
        if r == 0:
            print "foot landed"
            return True
            
        print "foot not landed"
        return False
        
        
class ControlZMP(WalkerModule):
    def __init__(self):
        WalkerModule.__init__(self)
        self.ZMPpos = []
    
    def stepRightExecute(self, motorPositions, motorNextPositions):
        ZMPpos = [] #position under right foot
        self.controlZMP( motorPositions, motorNextPositions)
        
    def stepLeftExecute(self, motorPositions, motorNextPositions):
        ZMPpos = [] #position under left foot
        self.controlZMP( motorPositions, motorNextPositions)
        
    def doubleSupportRightExecute(self, motorPositions, motorNextPositions):
        ZMPpos = [] #between feet
        self.controlZMP( motorPositions, motorNextPositions)
        
    def doubleSupportLeftExecute(self, motorPositions, motorNextPositions):
        ZMPpos = [] #between feet
        self.controlZMP( motorPositions, motorNextPositions)
        
        
    def controlZMP(self, motorPositions, motorNextPositions):
        print "controlling ZMP"
        pass
        
        