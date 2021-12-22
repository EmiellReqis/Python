import pytest
import unittest.mock as mock
import LeapYear1


@pytest.mark.parametrize("year, month, expected", [(1900,1,31), (1900,12,31), (2000,2,29), (1900,2,28)])
def tests_how_many_days_in_a_month(year, month, expected):
    assert LeapYear1.how_many_days_in_a_month(year,month) == expected

@pytest.mark.parametrize("year,expected", [(2000, True), (4, True),(1900, False), (3, False)])
def test_is_leap_year(year, expected):
    assert LeapYear1.is_leap_year(year) == expected
    if expected == expected:
        print("Is it a leap year?: ",expected)

@pytest.mark.parametrize("year,month,day,expected", [(2000,12,31,366), (1900,12,31,365)])
def test_which_day_of_the_year(year,month,day,expected):
    assert LeapYear1.which_day_of_the_year(year,month,day) == expected

def test_end_to_end():
    year = 2020
    month = 12
    day = 31
    assert LeapYear1.is_leap_year(year) == True
    assert LeapYear1.how_many_days_in_a_month(year,month) == LeapYear1.days_in_a_month_leap_year[month - 1]
    assert LeapYear1.which_day_of_the_year(year,month,day) == 366

def test_year_input1(mocker):
    mocker.patch('builtins.input', side_effect=[10000,"sa",9999])
    year = LeapYear1.check_if_year_is_valid()
    assert year == 9999


def test_year_input2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    year = int(input("Enter year: "))    
    assert LeapYear1.check_if_year_is_valid() == year
    

def test_year_input3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 9999)
    year = int(input("Enter year: "))    
    assert LeapYear1.check_if_year_is_valid() == year

def test_month_input1(monkeypatch,):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    month = int(input("Enter month: "))
    assert LeapYear1.check_if_month_is_valid() == month

def test_month_input2(mocker):
    mocker.patch('builtins.input', side_effect=[13,"aaasd",6])
    month = LeapYear1.check_if_month_is_valid()
    assert month == 6

def test_month_input3(monkeypatch,):
    monkeypatch.setattr('builtins.input', lambda _: 12)
    month = int(input("Enter month: "))
    assert LeapYear1.check_if_month_is_valid() == month

def test_day_input1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    LeapYear1.year = 2000
    LeapYear1.month = 1
    day = int(input("Enter day: "))    
    assert LeapYear1.check_if_day_is_valid() == day

def test_day_input2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 31)
    LeapYear1.year = 2000
    LeapYear1.month = 1
    day = int(input("Enter day: "))    
    assert LeapYear1.check_if_day_is_valid() == day

def test_day_input3(mocker):
    LeapYear1.year = 1900
    LeapYear1.month = 2
    mocker.patch('builtins.input', side_effect=[40,"ddscd",28])
    day = LeapYear1.check_if_day_is_valid()
    assert day == 28
