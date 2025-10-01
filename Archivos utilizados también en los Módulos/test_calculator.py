# Crear prueba en test_calculator.py:

from calculator import add
import pytest

def test_add():
     assert add(2, 3) == 5

