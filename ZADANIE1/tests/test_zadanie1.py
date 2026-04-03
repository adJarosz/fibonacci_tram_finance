import gmpy2
import pytest

from ZADANIE1 import zadanie1


# Kilka pierwszych wyrazów ciągu Fibonacciego
F_SMALL = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# --- fib_iter --------------------------------------------------------------

def test_fib_iter_small_values():
    for n, expected in enumerate(F_SMALL):
        assert zadanie1.fib_iter(n) == expected


def test_fib_iter_zero_and_one():
    assert zadanie1.fib_iter(0) == 0
    assert zadanie1.fib_iter(1) == 1


def test_fib_iter_negative_raises():
    with pytest.raises(ValueError):
        zadanie1.fib_iter(-1)


# --- mat_mul ---------------------------------------------------------------

def test_mat_mul_identity():
    A = (3, 4, 5, 6)
    I = (1, 0, 0, 1)
    assert zadanie1.mat_mul(A, I) == A
    assert zadanie1.mat_mul(I, A) == A


# --- mat_pow ---------------------------------------------------------------

def test_mat_pow_zero_is_identity():
    M = (2, 3, 4, 5)
    I = (1, 0, 0, 1)
    assert zadanie1.mat_pow(M, 0) == I


def test_mat_pow_A_powers():
    A = (1, 1, 1, 0)
    # A^1 = A
    assert zadanie1.mat_pow(A, 1) == A
    # A^2 = [[2,1],[1,1]] -> (2,1,1,1)
    assert zadanie1.mat_pow(A, 2) == (2, 1, 1, 1)
    # A^3 = [[3,2],[2,1]] -> (3,2,2,1)
    assert zadanie1.mat_pow(A, 3) == (3, 2, 2, 1)


def test_mat_pow_negative_raises():
    A = (1, 1, 1, 0)
    with pytest.raises(ValueError):
        zadanie1.mat_pow(A, -1)


# --- fib_matrix ------------------------------------------------------------

def test_fib_matrix_matches_iter_for_small_n():
    for n in [0, 1, 2, 3, 5, 10, 20]:
        assert zadanie1.fib_matrix(n) == zadanie1.fib_iter(n)


def test_fib_matrix_matches_gmp_for_medium_n():
    # wartości małe na tyle, że test jest błyskawiczny
    for n in [50, 100, 300]:
        assert zadanie1.fib_matrix(n) == int(gmpy2.fib(n))


def test_fib_matrix_negative_raises():
    with pytest.raises(ValueError):
        zadanie1.fib_matrix(-5)
