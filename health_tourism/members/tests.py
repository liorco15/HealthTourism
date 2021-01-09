from django.test import TestCase


def add_numbers(first, second):
    return first + second


def test_add_numbers():
    assert add_numbers(5, 3) == 8

