import pytest

from utils import utils

class TestReversed:
    @pytest.mark.parametrize("number, expected",[
        (123, 321),
        (100, 1),
        (7, 7),
        (0, 0),
        (-123, -321),
    ])
    def test_integers(self, number, expected):
        assert utils.reversed(number) == expected
    
    @pytest.mark.parametrize("number", ["123", "abc", ""])
    def test_strings_rejected(self, number):
        with pytest.raises(TypeError):
            utils.reversed(number)
    
    @pytest.mark.parametrize("number", [1.23, 123.0, -4.5])
    def test_floats_rejected(self, number):
        with pytest.raises(TypeError):
            utils.reversed(number)


class TestFormatter:
    @pytest.mark.parametrize("number, expected", [
        (0, ("0b0", "0o0")),
        (8, ("0b1000", "0o10")),
        (255, ("0b11111111", "0o377")),
        (-8, ("-0b1000", "-0o10")),
    ])
    def test_integers(self, number, expected):
        assert utils.formatter(number) == expected
    
    @pytest.mark.parametrize("number", ["8", "abc", ""])
    def test_strings_rejected(self, number):
        with pytest.raises(TypeError):
            utils.formatter(number)

    @pytest.mark.parametrize("number", [8.0, 1.5, -2.5])
    def test_floats_rejected(self, number):
        with pytest.raises(TypeError):
            utils.formatter(number)
    