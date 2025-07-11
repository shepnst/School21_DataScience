from financial import parsing
import pytest


def test_type_tuple():
    result = parsing('MSFT', 'Total Revenue')
    assert type(result) is tuple


def test_if_invalid_ticker():
    with pytest.raises(Exception):
        parsing('invalid_ticker', 'Total Revenue')


def test_if_invalid_field():
    with pytest.raises(Exception):
        parsing('MSFT', '')


def test_result():
    result = parsing('MSFT', 'Total Revenue')
    assert result[0]=='Total Revenue'


if __name__=="__main__":
    test_type_tuple()
    test_if_invalid_ticker()
    test_if_invalid_field()
    test_result()