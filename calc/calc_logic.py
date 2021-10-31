import sys

class CalcLogic:

    def __init__(self):
        pass

    @staticmethod
    def input_check(pending_rpn): 
        try:
            return float(pending_rpn)
        except:
            print("Please Enter a Number")
            return "Invalid input please enter a number"

class CalcState:

    def __init__ (self,curr_num = 0):
        pass
    def update_state(self,result):
        self.curr_num = result




class Actor(CalcState):
    
    def __init__(self, calc_count = 0):
        self.calc_count = 0 
        self.num_state = self.num_state = CalcState()

    def start_math_engine(self,operand_arr = []):
        op_switch = True
        operand = ''
        #take and parse input
        while len(operand_arr) < 2:
            operand = input('> ')
            try:
                if operand == 'q':
                    sys.exit()
                check = float(operand)
                operand_arr.append(check)
            except ValueError:
                print('Invalid Input Enter a number')
        operator = input("> ")
        
        while op_switch:
            if operator == '-':
                print(difference(operand_arr[0],operand_arr[1]))
                self.start_math_engine([difference(operand_arr[0],operand_arr[1])])
                op_switch = False
            elif operator == '+':
                print(sum(operand_arr[0],operand_arr[1]))
                self.start_math_engine([sum(operand_arr[0],operand_arr[1])])
                op_switch = False
            elif operator == '*':
                print(product(operand_arr[0],operand_arr[1]))
                self.start_math_engine([product(operand_arr[0],operand_arr[1])])
                op_switch = False
            elif operator == '/':
                print(quotient(operand_arr[0],operand_arr[1]))
                self.start_math_engine([quotient(operand_arr[0],operand_arr[1])])
                op_switch = False
            elif operator == "q":
                sys.exit()
            else:
                print(" Please inter a valid operator + , - , * , /")
                operator = input("> ")
            

        #operate on input
        #print and store result


# Arithmetic
from decimal import *
getcontext().prec = 4

def sum(a,b):

    return float(Decimal(a) + Decimal(b))

def difference(a,b):
    return  float(Decimal(a) - Decimal(b))

def product(a,b):
    return float(Decimal(a) * Decimal(b))

def quotient(a,b):
    return float(Decimal(a) / Decimal(b)) 


