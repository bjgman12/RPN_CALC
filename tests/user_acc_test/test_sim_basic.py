import pytest

from tests.user_acc_test.flo import diff

from calc.calc import Calc

# pytestmark = [pytest.mark.version_2, pytest.mark.version_3]

def test_quitter():
    calc = Calc()
    errors = diff(calc.runCalc, path="tests/user_acc_test/sim_txt_files/quitter.sim.txt")
    assert not errors, errors[0]

def test_each_op_single_in_quit():
    calc = Calc()
    errors = diff(calc.runCalc, path="tests/user_acc_test/sim_txt_files/each_op_then_quit.sim.txt")
    assert not errors, errors[0]

def test_input_exceptions():
    calc = Calc()
    errors = diff(calc.runCalc, path="tests/user_acc_test/sim_txt_files/exception_handle.sim.txt")
    assert not errors, errors[0]

def test_fat_fingers():
    calc = Calc()
    errors = diff(calc.runCalc, path="tests/user_acc_test/sim_txt_files/fat_finger.sim.txt")
    assert not errors, errors[0]