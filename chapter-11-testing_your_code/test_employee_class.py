# CloudOfNiko
# 23.04.2026
# Learning to use fixtures in pytest.
# Fixture did not work properly in my terminal, returned an AttributeError for give_raise().

import pytest
from employee_class import Employee

@pytest.fixture
def employee():
    """A testificate model."""
    first_name = 'Tohru'
    last_name = 'Adachi'
    salary = 0
    employee = Employee(first_name, last_name, salary)
    return employee

def test_give_default_raise():
    """Does the default amount for a raise work?"""
    employee.give_raise()
    assert employee.salary == 5000

def test_give_custom_raise():
    """Does a 1 amount for a raise work?"""
    employee.give_raise(1)
    assert employee.salary == 1