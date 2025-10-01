# Crear prueba en test_sample.py:

import pytest
from calculator import add

def test_add():
     assert add(2, 3) == 5

