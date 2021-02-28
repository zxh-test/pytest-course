import pytest
import yaml

from pythoncode.Calculator import Calculator


# 参数化与数据驱动的区别？
# yaml保存测试数据的使用

def get_datas(path="./data/calc.yaml"):
    with open(path) as f:
        datas = yaml.safe_load(f)
    return datas


class TestCalc:
    dates: list = get_datas()

    def setup_class(self):
        self.calc = Calculator()
        print("用例执行")

    @pytest.mark.parametrize("a, b, result", dates["add"]["datas"])
    def test_add(self, a, b, result):
        assert result == self.calc.add(a, b)

    # todo: 相除功能
    @pytest.mark.parametrize("a, b, result", [[8, 4, 2], [3, 1, 3]])
    def test_div(self, a, b, result):
        assert result == self.calc.div(a, b)

    @pytest.mark.parametrize("a, b", [[2, 0], [3, 0]])
    def test_raises_div(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    def test_multiplication(self):
        assert 7 == self.calc.multiplication(1, 7)

    def test_subtraction(self):
        assert 6 == self.calc.subtraction(7, 1)

    def teardown_class(self):
        print("执行结束")


if __name__ == "__main__":
    pytest.main()
