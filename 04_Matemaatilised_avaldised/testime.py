import pytest
from quadratic_equation import solve_quadratic_equation as solve

# 1. test mis õnnestub (täisarvulised lahendid)
def test_integer_values():
    assert solve(1, -3, 2) == (1, 2)

# 2. test komaga lahendused
def test_float_values():
    assert solve(1, -4, 3.75) == (1.5, 2.5)

# 3. üks lahend
def test_one_solution():
    assert solve(1, -4, 4) == (2,)

# 4. lahend puudub
def test_no_solution():
    assert solve(1, -4, 5) == ()

# 5. nulliga jagamine (a = 0)
def test_division_by_zero():
    assert solve(0, -4, 2) == ()