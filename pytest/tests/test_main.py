import os
import sys
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.main import Calc
# from tests import conftest as ct

class TestCalc():
    @pytest.mark.test01
    def test_add_01(self, func_comm):
        print('\n' + 'test_add_01----start')
        assert Calc(1,2).add() == 3
        print('test_add_01----end')

    @pytest.mark.skip(reason="test")
    def test_add_02(self, func_comm):
        print('\n' + 'test_add_02----start')
        print(func_comm)
        assert Calc(2,3).add() == 4
        print('test_add_02----end')


class TestTarget(object):
    # ダミーメソッドを用意して差し替える場合
    # pytestのテストコードの引数に、`monkeypatch`を追加
    def test_patch_by_dummy_function(self, monkeypatch):
        print('\n' + 'test_patch_by_dummy_function----start')

        # run_dummyというダミーメソッドを用意し、この中で差し替える戻り値を設定
        # Target.get_constは引数selfがあるため、差し替えメソッドでも引数(arg)を用意
        def run_dummy(arg):
            return 'ham'
        
        # monkeypatch.setattr()を使って差し替え
        # 第一引数：importしたプロダクションコードのクラス
        # 第二引数：差し替え対象のメソッド
        # 第三引数：差し替えたダミーメソッド
        from src.main import Target
        monkeypatch.setattr(Target, 'get_const', run_dummy)
        sut = Target()
        actual = sut.get_const()
        assert actual == 'ham'
        
        print('test_patch_by_dummy_function----end')


from src.main import CsvSample
import pandas
import pandas.testing as pd_testing
class TestCsvSample():
    @pytest.mark.test01
    def test_csv_sample_1(self, func_comm):
        print('\n' + 'test_csv_sample_1----start')
        result = CsvSample().get_csv()
        print(result)
        answer = pandas.read_csv('./tests/input.csv')
        print(answer)
        # assert x == answer
        pd_testing.assert_frame_equal(result, answer)
