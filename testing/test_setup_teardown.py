def test_a():
    print("测试用例")


def setup():
    print("测试前")


def teardown():
    print("测试后")


def setup_module():
    print("模块级--前")


def teardown_module():
    print("模块级别--后")


# 在类里不生效
def setup_function():
    print("测试函数--前")


def teardown_function():
    print("测试函数--后")


class TestCases1():
    def setup_class(self):
        print("类级别--前")

    def teardown_class(self):
        print("类级别--后")

    def setup_method(self):
        print("测试方法--前")

    def teardown_method(self):
        print("测试方法--后")

    def test_1(self):
        print("测试用例11执行")

    def test_2(self):
        print("测试用例22执行")
