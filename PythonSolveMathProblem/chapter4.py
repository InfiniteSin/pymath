"""《Python玩转数学问题》Chapter 4 循环."""

import math
from collections.abc import Callable


def bisection(f: Callable, x1: float, x2: float, tol: float = 1e-6) -> float | None:
    """使用二分法求方程近似解.

    Args:
        f (Callable): 待解方程的函数
        x1 (float): 求近似解的区间下界
        x2 (float): 求近似解的区间上界
        tol (float): 可选参数, 近似解的公差值, 默认为 1e-6

    Returns:
        float | None: 方程 f = 0 的近似解

    """
    if f(x1) * f(x2) > 0:
        print(f"区间[{x1}, {x2}]内不一定有解!")
        return None
    m: float = (x1 + x2) / 2
    while abs(f(m)) > tol:
        if f(x1) * f(m) < 0:
            x2: float = m
        else:
            x1: float = m
        m: float = (x1 + x2) / 2
    return m


def newton_iter(f: Callable, dfdx: Callable, x0: float, tol: float = 1e-6) -> float:
    """使用牛顿迭代法求方程近似解.

    Args:
        f (function): 待解方程的函数
        dfdx (function): 待解方程的导函数
        x0 (float): 求近似解的迭代起点
        tol (float): 可选参数, 近似解的公差值, 默认为 1e-6

    Returns:
        float: 方程 f = 0 的近似解

    """
    f0: float = f(x0)
    while abs(f0) > tol:
        x1: float = x0 - f0 / dfdx(x0)
        x0: float = x1
        f0: float = f(x0)
    return x0


# Exercises
# Exercise 4.1
def is_prime(n: float) -> bool:
    """Return True when n is a prime number."""
    if n <= 1:
        # 质数必须大于 1
        return False
    # return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    for i in range(2, int(n**0.5) + 1):  # noqa: SIM110
        # 从 2 到 n 的平方根遍历, 检查能否整除 n
        if n % i == 0:
            return False
    return True


def prime_filter(start: int, end: int) -> list[int]:
    """求出给定范围内的所有质数.

    Args:
        start (int): 求质数范围的下界
        end (int): 求质数范围的上界

    Returns:
        list[int]: 给定数据范围内的所有质数

    """
    return list(filter(is_prime, list(range(start, end + 1))))


def test_prime_filter() -> None:
    """prime_filter()的测试函数."""
    assert prime_filter(1, 10) == [2, 3, 5, 7], "质数计算错误"


def cal_prime() -> int:
    """证伪: 对于任意质数 p, 2**p - 1 也是质数, 求出第一个反例.

    Returns:
        int: 对于任意质数 p, 第一个非质数的 2**p - 1

    """
    i: int = 1
    while True:
        i: int = i + 1
        if not is_prime(i):
            continue
        n: int | float = math.pow(2, i) - 1
        if not is_prime(n):
            print(f"质数 {i} 的 2^p - 1 = {n} 不是质数, 成功证伪")
            return i


def mason_prime(limit: int = 40) -> list[int]:
    """找出 40 以内的所有梅森质数.

    梅森质数是形如 $2^p -1$ 的质数, 其中 p 也是质数

    Args:
        limit (int): 给定的数据范围

    Returns:
        list[int]: 给定数据范围内的所有梅森质数

    """
    primes: list[int] = list(filter(is_prime, range(1, limit + 1)))
    print(f"1 ~ 40 的质数包括 {primes}")
    # mason_primes: list[int] = list(filter(lambda x: is_prime(math.pow(2, x) - 1), primes))
    mason_primes: list[int] = [i for i in primes if is_prime((1 << i) - 1)]  # 使用 1 << p - 1 计算 $2^p -1$
    print(f"其中的梅森质数有 {mason_primes}")
    print(f"其梅森质数计算结果为 {[((1 << i) - 1) for i in mason_primes]}")
    return mason_primes


def test_mason_prime() -> None:
    """mason_prime()的测试函数."""
    assert mason_prime() == [2, 3, 5, 7, 13, 17, 19, 31], "40 以内的梅森质数计算错误"


# Exercise 4.4
def factors(n: int) -> list[int]:
    """对整数 n 进行质因子分解.

    Args:
        n (int): 给定的正整数

    Returns:
        list[int]: 给定正整数的质因子列表

    """
    factor_lst: list[int] = []
    prime_lst: list[int] = prime_filter(start=1, end=int(math.sqrt(n) + 1))
    for i in prime_lst:
        while n % i == 0:
            factor_lst.append(i)
            n: int = n // i
    if n > 2:
        factor_lst.append(n)
    return factor_lst


def test_factors() -> None:
    """factors()的测试函数."""
    assert factors(60) == [2, 2, 3, 5], "正整数 60 的质因子计算错误"
    assert factors(36) == [2, 2, 3, 3], "正整数 36 的质因子计算错误"


# Exercise 4.5 计算给定正整数 n 的真因数
def true_factors(n: int) -> list[int]:
    """计算正整数 n 的真因素.

    Args:
        n (int): 给定的正整数

    Returns:
        list[int]: 给定正整数的真因素列表

    """
    true_factor_lst: list[int] = [i for i in range(1, n) if n % i == 0]
    return true_factor_lst


def test_true_factors() -> None:
    """true_factors()的测试函数."""
    assert true_factors(12) == [1, 2, 3, 4, 6], "正整数 12 的真因数计算错误"
    assert true_factors(21) == [1, 3, 7], "正整数 21 的真因数计算错误"


# Exercise 4.6 计算 10_000 以内的所有完美数
# 完美数定义: 所有真因数的和等于完美数本身
def perfect_num(limit: int = 10_000) -> list[int]:
    """计算 10_000 以内的完美数.

    Returns:
        list[int]: 10_000 以内完美数的列表

    """
    result_lst: list[int] = []
    for i in range(1, limit + 1):
        true_factor_lst: list[int] = true_factors(i)
        if sum(true_factor_lst) == i:
            result_lst.append(i)
    return result_lst


def test_perfect_num() -> None:
    """perfect_num()的测试函数."""
    assert perfect_num(limit=100) == [6, 28], "100 以内的完美数计算错误"
    assert perfect_num() == [6, 28, 496, 8128], "10_000 以内的完美数计算错误"


def main() -> None:
    """Entry function."""
    # # 求解函数 f(x) = x**2 - 4*x + exp(-x)
    # # 利用二分法在区间 [-0.5, 1] 上求解
    # f: Callable = lambda x: x**2 - 4 * x + math.exp(-x)
    # sol: float | None = bisection(f, -0.5, 1)
    # print(f"利用二分法求得近似解 x = {sol:.6f}, f({sol:.6f}) = {f(sol):.5e}")

    # # 使用牛顿迭代法求解
    # dfdx: Callable = lambda x: 2 * x - 4 - math.exp(-x)  # f(x)的导函数
    # sol: float = newton_iter(f, dfdx, 0)
    # print(f"利用牛顿迭代法求得近似解 x = {sol:.6f}, f({sol:.6f}) = {f(sol):.5e}")

    # Exercise 4.1 求 1~100 区间内的所有质数
    prime_nums: list[int] = prime_filter(1, 100)
    print(prime_nums)

    # Exercise 4.2 证伪: 对于所有质数 p, 2**p - 1 也是质数。求出第一个反例。
    exc42_result: int = cal_prime()  # noqa: F841

    # Exercise 4.3 找出 40 以内的梅森质数
    mason_prime()


if __name__ == "__main__":
    main()
