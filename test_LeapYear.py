import pytest
import LeapYear1
from LeapYear1 import how_many_days_in_a_month

def test_how_many_days_in_a_month():
    for x in range(1,13):
        LeapYear1.month = x
    assert LeapYear1.how_many_days_in_a_month(4 ,LeapYear1.month) == LeapYear1.days_in_a_month_leap_year[LeapYear1.month-1]

@pytest.mark.parametrize("test_input,expected", [(1, 31), (2, 28), (4, 30), (10, 31)])
def tests_how_many_days_in_a_month(test_input,expected):
    assert LeapYear1.how_many_days_in_a_month(4,test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(4, True), (3, False), (4, False)])
def test_is_leap_year_param(test_input, expected):
    assert LeapYear1.is_leap_year(test_input) == expected

def test_which_day_of_the_year():
    assert LeapYear1.which_day_of_the_year(4,2,29) == 60

def test_which_day_of_the_year_fail():
    assert LeapYear1.which_day_of_the_year(3,12,31) == 366

@pytest.mark.parametrize("test_input,expected", [(23, 23), (10000, ValueError), ("sd", ValueError), (10, 10)]) 
def test_input(test_input, expected):
    assert LeapYear1.check_if_year_is_valid(test_input) == expected