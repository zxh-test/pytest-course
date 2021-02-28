import yaml


def test_yaml():
    with open("./data/calc.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)

test_yaml()