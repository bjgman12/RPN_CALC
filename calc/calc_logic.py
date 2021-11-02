import sys

class CalcLogic:

    def __init__(self):
        pass

    @staticmethod
    def multi_handler(input_str,act):
        """[Handles parsing multi operator inputs]

        Args:
            input_str ([string]): [string of operands and or operators ]
            act ([object]): [instance of Actor class]
        """
        input_arr = input_str.split(' ')
        if len(input_arr) > 3:
            print("Invalid chain input chained input should have 2 operands followed by one operator")
            act.start_math_engine()
        elif len(input_arr) == 3:
            try:
                act.operand_arr.append(float(input_arr.pop(0)))
                act.operand_arr.append(float(input_arr.pop(0)))
                CalcLogic.op_check(act,input_arr.pop(0))
            except ValueError:
                print("Invalid Input looking for 2 operands followed by an operator")
        elif len(input_arr) == 2 :
            try:
                act.operand_arr.append(float(input_arr.pop(0)))
                act.operand_arr.append(float(input_arr.pop(0)))
                CalcLogic.single_operator_check(act)
            except ValueError:
                print("Invalid chain Input looking for 2 operands followed by an operator")

        # check if input_arr is correct length
        # check if lastChain is operator

    @staticmethod
    def single_handler(char,act):
        """[handles single ichar inputs]

        Args:
            char ([string]): [a sting of a number]
            act ([obj]): [instance of Actor class]
        """
        try:
            if char == 'q':
                sys.exit()
            check = float(char)
            act.operand_arr.append(check)
        except ValueError:
            print('Invalid Input Enter a number')
    

    @staticmethod
    def single_operator_check(act):
        """[checks input when only an operator is needed]

        Args:
            act ([obj]): [instance of Actor Class]
        """
        char = input("> ")
        CalcLogic.op_check(act,char)

    @staticmethod
    def op_check(act,char):
        """[checks if input is a valid operator]

        Args:
            act ([obj]): [instance of Actor Instance]
            char ([string]): [string input for operator]
        """
        op_switch = True
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
                print( char, ": Is not a valid operator. Please inter a valid operator + , - , * , /")
                try:
                    char = input("> ")
                except EOFError:
                    sys.exit()



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
        """[starts taking in input for math engine]
        """
        operand = ''
        self.calc_count += 1
        #take and parse input
        while len(self.operand_arr) < 2:
            try:
                operand = input('> ')
            except EOFError:
                sys.exit()
            if len(operand.split()) > 1:
                CalcLogic.multi_handler(operand,self)
            else:
                CalcLogic.single_handler(operand,self)
        
        CalcLogic.single_operator_check(self)
        #operate on input
        #print and store result


# Arithmetic globals

from decimal import *
getcontext().prec = 4

def sum(a,b):
    """sums 2 numbers

    Args:
        a ([str]): [input representing a float]
        b ([str]): [input representing a float]

    Returns:
        [float]: [sum of a and b]
    """
    try:
        return float(Decimal(a) + Decimal(b))
    except ValueError:
        print(f'Must add 2 numbers not ${type(a)} and ${type(b)}')
        return 0

def difference(a,b):
    """ subtracts 2 numbers

    Args:
        a ([str]): [input representing a float]
        b ([str]): [input representing a float]

    Returns:
        [float]: [difference of a and b]
    """
    try:
        return  float(Decimal(a) - Decimal(b))
    except ValueError:
        print(f'Must subtract 2 numbers not ${type(a)} and ${type(b)}')
        return 0


def product(a,b):
    """multiplies 2 numbers

    Args:
        a ([str]): [input representing a float]
        b ([str]): [input representing a float]

    Returns:
        [float]: [product of a and b]
    """
    try:
        return float(Decimal(a) * Decimal(b))
    except ValueError:
        print(f'Must multiply 2 numbers not ${type(a)} and ${type(b)}')
        return 0

def quotient(a,b):
    """divides 2 numbers

    Args:
        a ([str]): [input representing a float]
        b ([str]): [input representing a float]

    Returns:
        [float]: [difference of a and b]
    """
    try:
        return float(Decimal(a) / Decimal(b)) 
    except:
        print(f'Must multiply 2 numbers not ${type(a)} and ${type(b)}')
        return 0


