def main():
    # Parse input
    instructions = []
    registers = dict()
    with open('./input.txt', 'r') as input_file:
        for line in input_file:
            line = line.replace("\n", "")
            data = line.split(" ")
            instructions.append(parseInstruction(data))

    maximum = 0
    for instruction in instructions:
        instruction.executeInstruction(registers)
        maximum = max(registers.values()) if max(registers.values()) > maximum else maximum

    print(maximum)
    
def parseInstruction(data):

    target_reg = data[0]
    operation = data[1]
    amount = int(data[2])
    cond_reg = data[4]
    conditional = data[5]
    cond_value = int(data[6])

    return Instruction(target_reg, operation, amount, cond_reg, conditional, cond_value)



class Instruction:

    def __init__(self, target_reg, op, amount, cond_reg, conditional, cond_value):
        self.target_reg = target_reg
        self.operation = op
        self.amount = amount
        self.cond_reg = cond_reg
        self.conditional = conditional
        self.cond_value = cond_value

    def executeInstruction(self, registers):

        self.instantiateRegisters(registers)

        if self.evalulateCondition(registers):
            self.updateRegister(registers)


    def instantiateRegisters(self, registers):
        if self.target_reg not in registers:
            registers[self.target_reg] = 0
        if self.cond_reg not in registers:
            registers[self.cond_reg] = 0
    
    def evalulateCondition(self, registers):
        cond_reg_value = registers[self.cond_reg]

        if self.conditional == ">":
            return cond_reg_value > self.cond_value
        elif self.conditional == ">=":
            return cond_reg_value >= self.cond_value
        elif self.conditional == "<":
            return cond_reg_value < self.cond_value
        elif self.conditional == "<=":
            return cond_reg_value <= self.cond_value
        elif self.conditional == "==":
            return cond_reg_value == self.cond_value
        elif self.conditional == "!=":
            return cond_reg_value != self.cond_value
        else:
            print("Unrecognized conditional: "  + self.conditional)
            exit(1)

    def updateRegister(self, registers):

        if self.operation == "inc":
            registers[self.target_reg] += self.amount
        elif self.operation == "dec":
            registers[self.target_reg] -= self.amount
        else:
            print("Unrecognized operation: "  + self.operation)
            exit(1)

if __name__ == "__main__":
    main()