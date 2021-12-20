import pytest
import LeapYear1

def test_how_many_days_in_a_month():
    for x in range(1,13):
        LeapYear1.month = x
        assert LeapYear1.how_many_days_in_a_month(4 ,LeapYear1.month) == LeapYear1.days_in_a_month_leap_year[LeapYear1.month - 1]

@pytest.mark.parametrize("year, month, expected", [(4,1,31), (4,2,28), (3,4,30), (3,10,31)])
def tests_how_many_days_in_a_month(year, month, expected):
    assert LeapYear1.how_many_days_in_a_month(year,month) == expected

@pytest.mark.parametrize("year,expected", [(2020, True), (3, False), (4, False)])
def test_is_leap_year(year, expected):
    assert LeapYear1.is_leap_year(year) == expected

@pytest.mark.parametrize("year,month,day,expected", [(4,2,40,71), (3,2,29,60), (3,12,32,366)])
def test_which_day_of_the_year(year,month,day,expected):
    assert LeapYear1.which_day_of_the_year(year,month,day) == expected

def test_which_day_of_the_year_fail():
    assert LeapYear1.which_day_of_the_year(3,12,31) == 366

year = 2020
month = 12
day = 31
def test_end_to_end():
    assert LeapYear1.is_leap_year(year) == True
    assert LeapYear1.how_many_days_in_a_month(year,month) == LeapYear1.days_in_a_month_leap_year[LeapYear1.month - 1]
    assert LeapYear1.which_day_of_the_year(year,month,day) == 366

def test_end_to_end_fail():
    assert LeapYear1.is_leap_year(year) == True
    assert LeapYear1.how_many_days_in_a_month(year,month) == LeapYear1.days_in_a_month_leap_year[LeapYear1.month - 1]
    assert LeapYear1.which_day_of_the_year(year,month,day) == 365


def test_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1000)
    year = int(input("Enter year: "))   
    assert LeapYear1.check_if_year_is_valid() == year
