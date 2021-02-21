from pythoncode.Calculator import Calculator


class TestCalc:
    def test_add(self):
        calc = Calculator()
        assert 2 == calc.add(2, 1)

    def test_div(self):
        pass
