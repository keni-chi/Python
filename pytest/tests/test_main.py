import os
import sys
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.main import Calc
# from tests import conftest as ct

class TestCalc():
    @pytest.mark.test01
    def test_add_01(self, func_comm):
        print('test_add_01----start')
        assert Calc(1,2).add() == 3
        print('test_add_01----end')

    @pytest.mark.skip(reason="test")
    def test_add_02(self, func_comm):
        print('test_add_02----start')
        print(func_comm)
        assert Calc(2,3).add() == 4
        print('test_add_02----end')
