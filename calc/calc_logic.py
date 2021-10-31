import sys

class CalcLogic:

    def __init__(self):
        pass

    @staticmethod
    def multi_handler():
        print("im Here")

    @staticmethod
    def single_handler(char,act):
      
        try:
            if char == 'q':
                sys.exit()
            check = float(char)
            act.operand_arr.append(check)
        except ValueError:
            print('Invalid Input Enter a number')
    

    @staticmethod
    def single_operator_check(act):
        op_switch = True
        char = input("> ")
        while op_switch:
            if char == '-':
                print(difference(act.operand_arr[0],act.operand_arr[1]))
                act.operand_arr = []
                act.start_math_engine()
                op_switch = False
            elif char == '+':
                print(sum(act.operand_arr[0],act.operand_arr[1]))
                act.operand_arr = []
                act.start_math_engine()
                op_switch = False
            elif char == '*op_switch = True':
                print(product(act.operand_arr[0],act.operand_arr[1]))
                act.operand_arr = []
                act.start_math_engine()
                op_switch = False
            elif char == '/':
                print(quotient(act.operand_arr[0],act.operand_arr[1]))
                act.operand_arr = []
                act.start_math_engine()
                op_switch = False
            elif char == "q":
                sys.exit()
            else:
                print(" Please inter a valid operator + , - , * , /")
                char = input("> ")

class CalcState:

    def __init__ (self,curr_num = 0):
        pass
    def update_state(self,result):
        self.curr_num = result




class Actor(CalcState):
    
    def __init__(self, calc_count = 0):
        self.calc_count = 0 
        self.num_state = self.num_state = CalcState()
        self.operand_arr = []

    def start_math_engine(self):
        operand = ''
        #take and parse input
        while len(self.operand_arr) < 2:
            operand = input('> ')
            if len(operand.split()) > 1:
                CalcLogic.multi_handler()
            else:
                CalcLogic.single_handler(operand,self)
        
        CalcLogic.single_operator_check(self)
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


