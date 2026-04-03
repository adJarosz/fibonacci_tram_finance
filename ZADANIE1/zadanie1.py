import time
import gmpy2
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def fib_iter(n: int) -> int:
    if n < 0:
        raise ValueError("podano argumnt ujmeny")
    if n == 0:
        return 0
    a = 0
    b = 1
    for _ in range(1, n):
        x = a
        a = b
        b = x + b
    return b



def mat_mul(A: tuple[int, int, int, int],
            B: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    """
    Mnożenie macierzy 2×2 zapisanych jako krotki (a, b, c, d).
    Zwróć krotkę (a', b', c', d') będącą wynikiem A·B.
    """
    a1, b1, c1, d1 = A
    a2, b2, c2, d2 = B
    return (a1*a2 + b1*c2,
            a1*b2 + b1*d2,
            c1*a2 + d1*c2,
            c1*b2 + d1*d2)


def mat_pow(M: tuple[int, int, int, int], n: int) -> tuple[int, int, int, int]:
    """
    Szybkie potęgowanie macierzy.
    R = (1, 0, 0, 1) – macierz jednostkowa.
    Pętla: jeśli bit n to 1 → R = R·M; zawsze M = M·M; n >>= 1.
    """
    if n < 0:
        raise ValueError("podano argumnt ujmeny")
    R = (1, 0, 0, 1)
    while n > 0:
        if n & 1:
            R = mat_mul(R, M)
        M = mat_mul(M, M)
        n >>= 1
    return R


def fib_matrix(n: int) -> int:
    """
    Zwraca F_n metodą macierzową.
    • Wyznacz A^n dla A = (1, 1, 1, 0).
    • Zwróć F_n = element [0][1].
    """
    if n < 0:
        raise ValueError("podano argumnt ujmeny")
    if n == 0:
        return 0
    A = (1, 1, 1, 0)
    Mn = mat_pow(A, n)
    return Mn[1]


def main() -> None:
    n = int(input("Podaj n: "))

    start = time.perf_counter()
    f1 = fib_iter(n)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    f2 = fib_matrix(n)
    t2 = time.perf_counter() - start

    start = time.perf_counter()
    f3 = gmpy2.fib(n)
    t3 = time.perf_counter() - start

    print(f"fib_iter:   {t1:.6f} s")
    print(f"fib_matrix: {t2:.6f} s")
    print(f"gmpy2.fib:  {t3:.6f} s")

    print("Długość wyników (liczba cyfr):")
    print("fib_iter:",   len(str(f1)))
    print("fib_matrix:", len(str(f2)))
    print("gmpy2.fib:",  len(str(f3)))


    with open("fib_iter.txt", "w") as f_iter, \
            open("fib_matrix.txt", "w") as f_mat, \
            open("fib_gmpy2.txt", "w") as f_gmpy2:
        f_iter.write(str(f1))
        f_mat.write(str(f2))
        f_gmpy2.write(str(f3))


    if f1 == f2 == f3:
        print("Wszystkie trzy metody dały ten sam wynik.")
    else:
        print("UWAGA: Wyniki różnią się!")

if __name__ == "__main__":
    main()

