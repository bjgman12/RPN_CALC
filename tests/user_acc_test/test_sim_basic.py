import pytest

from tests.user_acc_test.flo import diff

from calc.calc import Calc

pytestmark = [pytest.mark.version_2, pytest.mark.version_3]

def test_quitter():
    calc = Calc()
    errors = diff(calc.runCalc, path="tests/user_acc_test/sim_txt_files/quitter.sim.txt")
    assert not errors, errors[0]