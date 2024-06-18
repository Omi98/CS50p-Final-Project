
# imports for testing
import pytest
from project import calculatorGUI
from project import option, num1, num2, answer


# create instance of the class
cal = calculatorGUI()


# check if window is created
def test_createWindow():
    cal.createWindow()
    assert hasattr(cal, "myWindow")

# check if welcome frame is created
def test_welcomeFrame():
    cal.welcomeFrame()
    assert hasattr(cal, "wFrame")

# check submit function ... with answers
def test_submit_add():
    num1 = 3
    num2 = 4
    if option == 'a':
        answer = num1 + num2
        assert answer == 7

    num1 = 4
    num2 = 0
    if option == 'd':
        with pytest.raises(ValueError):
            answer = num1 // num2
