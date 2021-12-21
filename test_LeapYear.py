import pytest
import LeapYear1


@pytest.mark.parametrize("year, month, expected", [(1900,1,31), (1900,12,31), (2000,2,29), (1900,2,28), (1900,2,29)])
def tests_how_many_days_in_a_month(year, month, expected):
    assert LeapYear1.how_many_days_in_a_month(year,month) == expected

@pytest.mark.parametrize("year,expected", [(2000, True), (4, True), (4, False),(1900, False), (3, False), (3, True)])
def test_is_leap_year(year, expected):
    assert LeapYear1.is_leap_year(year) == expected

@pytest.mark.parametrize("year,month,day,expected", [(2000,12,31,366), (1900,12,31,365), (1900,12,31,366)])
def test_which_day_of_the_year(year,month,day,expected):
    assert LeapYear1.which_day_of_the_year(year,month,day) == expected

def test_end_to_end():
    year = 2020
    month = 12
    day = 31
    assert LeapYear1.is_leap_year(year) == True
    assert LeapYear1.how_many_days_in_a_month(year,month) == LeapYear1.days_in_a_month_leap_year[month - 1]
    assert LeapYear1.which_day_of_the_year(year,month,day) == 366

def test_end_to_end_fail():
    year = 2020
    month = 12
    day = 31
    assert LeapYear1.is_leap_year(year) == True
    assert LeapYear1.how_many_days_in_a_month(year,month) == LeapYear1.days_in_a_month_leap_year[month - 1]
    assert LeapYear1.which_day_of_the_year(year,month,day) == 365

def test_year_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    year = int(input("Enter year: "))    
    assert LeapYear1.check_if_year_is_valid() == year

def test_year_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 9999)
    year = int(input("Enter year: "))    
    assert LeapYear1.check_if_year_is_valid() == year

def test_month_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    month = int(input("Enter month: "))    
    assert LeapYear1.check_if_month_is_valid() == month

def test_month_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 12)
    month = int(input("Enter month: "))    
    assert LeapYear1.check_if_month_is_valid() == month

def test_day_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    LeapYear1.year = 2000
    LeapYear1.month = 1
    day = int(input("Enter day: "))    
    assert LeapYear1.check_if_day_is_valid() == day

def test_day_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 31)
    LeapYear1.year = 2000
    LeapYear1.month = 1
    day = int(input("Enter day: "))    
    assert LeapYear1.check_if_day_is_valid() == day
