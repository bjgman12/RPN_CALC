# iMPORTS HERE
import sys
from calc_logic import Actor
class Calc():
    def __init__(self):
        pass

    def runCalc(self, actor=None ):
        """[summary]

        Args:
            actor ([function], optional): [description].
            Allows for custom inputs Defaults to None.
        """

        self.actor = actor

        print('Welcome to my RPN CALC please enter (s) to start or (q) to quit')

        res = input("> ")

        while res != 's' and res != 'q':
            print("Please enter a valid input (s)tart or (q)uit")
            res = input("> ")

        if res == 's':
            #start calculator
            self.start_app()
        elif res == 'q':
            # close application
            self.decline_app()

    def decline_app(self):
        print('Ok till next time.')
        sys.exit()
        # end app

    def start_app(self):
        # instatiate the actor
        # start calculations
        actor = Actor()
        actor.start_math_engine()


if __name__ == "__main__":
    calc = Calc();
    calc.runCalc()
