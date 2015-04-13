class LogicGate:
  
  def __init__(self, n):
    self.label = n
    self.output = None

  def getLabel(self):
    return self.label;

  def getOutput(self):
    self.output = self.PerformGateLogic()
    return self.output

class BinaryGate(LogicGate):
  def __init__(self, n):
      LogicGate.__init__(self, n)

      self.pinA = None
      self.pinB = None

  def getPinA(self):
    if self.pinA == None:
      return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
    else:
      return self.pinA.getFrom().getOutput()

  def getPinB(self):
    if self.pinB == None:
      return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
    else:
      return self.pinB.getFrom().getOutput()

  def setNextPin(self, source):
    if self.pinA == None:
      self.pinA = source
    else:
      if self.pinB == None:
        self.pinB = source
      else:
        raise RuntimeError("Error: No empty Pins!")


class UnaryGate(LogicGate):
  def __init__(self, n):
    LogicGate.__init__(self, n)

    self.pin = None

  def getPin(self):
    if self.pin == None:
      return int(input("Enter pin input for gate " + self.getLabel() + "-->"))
    else:
      return self.pin.getFrom().getOutput()

  def setNextPin(self, source):
    if self.pin == None:
      self.pin = source
    else:
      raise RuntimeError("Error: No empty Pins!")

class AndGate(BinaryGate):

  def __init__(self, n):
    BinaryGate.__init__(self, n)

  def PerformGateLogic(self):
    a = self.getPinA()
    b = self.getPinB()

    if a == 1 and b == 1:
      return 1
    else:
      return 0

class OrGate(BinaryGate):
  def __init__(self, n):
    BinaryGate.__init__(self, n)

  def PerformGateLogic(self):
    a = self.getPinA()
    b = self.getPinB()

    if a == 1 or b == 1:
      return 1
    else: 
      return 0

class NotGate(UnaryGate):
  def __init__(self ,n):
    UnaryGate.__init__(self, n)

  def PerformGateLogic(self):
    if self.getPin():
      return 0
    else:
      return 1


class Connector:
  def __init__(self, fgate, tgate):
    self.fromgate = fgate
    self.togate = tgate

    tgate.setNextPin(self)

  def getFrom(self):
    return self.fromgate

  def getTo(self):
    return self.togate

def main():
  g1 = AndGate("G1")
  g2 = AndGate("G2")
  g3 = OrGate("G3")
  g4 = NotGate("G4")
  c1 = Connector(g1,g3)
  c2 = Connector(g2,g3)
  c3 = Connector(g3,g4)
  print(g4.getOutput())



main()
