# -*- coding: utf-8 -*-

"""
《Python玩转数学问题》Chapter 3 函数与分支
"""

import math

# 使用阶乘计算组合数和排列数
def permutation(total_amount: int, pick_amount: int) -> float:
    """
    使用阶乘计算排列

    排列：从 n 个不同的元素中，取 r 个不重复的元素，按次序排列
    其全体集合用 A(n, r) 表示

    计算公式：$A_n^r = n*(n-1)*...*(n-r+1) = \\frac{n!}{(n-r)!}$

    可以使用 math.perm(n, r) 直接获取结果

    Args:
        total_amount (int): 元素的总集合
        pick_amount (int): 预期取出的不重复元素个数

    Returns:
        float: 从 n 个元素中取 r 个的不重排列个数
    """

    return math.factorial(total_amount) \
            / math.factorial(total_amount - pick_amount)

def combination(total_amount: int, pick_amount: int) -> float:
    """
    使用阶乘计算组合

    排列：从 n 个不同的元素中，取 r 个不重复的元素，不考虑其元素顺序
    其全体集合用 C(n, r) 表示
    相当于把排列带来的顺序去掉

    计算公式：$C_n^r = n*(n-1)*...*(n-r+1) = \\frac{n!}{(r)!*(n-r)!}$
    $C_n^r  = A_n^r / A_r^r$
    $C_n^r = $

    可以使用 math.comb(n, r) 直接获取结果

    Args:
        total_amount (int): 元素的总集合
        pick_amount (int): 预期取出的不重复元素个数

    Returns:
        float: 从 n 个元素中取 r 个的无重组合个数
    """
    factorial = math.factorial

    return factorial(total_amount) \
            / (factorial(pick_amount) * factorial(total_amount - pick_amount))

# math 模块中的常量
# 圆周率 math.pi
# Tau math.tau
def circle(radius: int) -> None:
    """
    使用 math.pi 及 radius 计算圆的周长及面积

    圆周率是圆的周长与直径之比 $\\pi = C / d$
    Tau 是圆的周长与半径之比，恒等于 $2\\pi$，常用于简化带有 $2\\pi$的公式

    圆的周长公式: $C = 2 * \\pi * r$
    变体： $C = \\pi * \\tau$

    圆的面积公式: $S = \\pi * (r ** 2)$
    
    Args:
        radius (int): 圆的半径
    """
    circumference = 2 * math.pi * radius
    # circumference = math.tau * radius # 使用 math.tau 代替 2 * math.pi

    square = math.pi * (radius ** 2)

    print(f"圆的周长 = 2 * {math.pi} * {radius} = {circumference}\
            \n圆的面积 = {math.pi} * ({radius} ** 2) = {square}")

# 欧拉数 math.e
def exponential(origin: int, time: int) -> float:
    """
    计算指数增长与指数衰变

    指数增长 $y(t) = y_0 * e^{kt}$
    指数衰变 $y(t) = y_0 * e^{-kt}$
    y(t): 表示时间t时的数量
    y_0: 表示初始数量
    k: 表示增长率/衰减率
    e: 自然对数，math.e

    Args:
        origin: 初始数量
        time: 时间

    Returns:
        float: 时间 time 时的数量
    """
    k = 0.025
    increase_result = origin * math.exp(k * time)
    decrease_result = origin * math.exp(-k * time)
    print(f"初始数量 {origin}g 经过时间 {time}s 后：\
            指数增长结果 {increase_result}\
            \n指数衰减结果 {decrease_result}\
            \n增长率为 {k}")

# 无穷大 math.inf，相当于float("inf")，大于任何数(包括双精度浮点数最大值10e308)
# 负无穷大 -math.inf
# 非数值NaN math.nan，相当于float("nan")

# math 内置库提供的数学运算函数
# 阶乘函数 math.factorial(<int>)，只接受非负整数
# 大于或等于给定值的最小整数 math.ceil(<float>)，向上取整
# 小于或等于给定值的最接近整数 math.floor(<float>)，向下取整
# 完全舍弃小数位 math.trunc(<float>)，正数向下取整，负数向上取整
# 判断两个数是否足够接近 math.isclose(a, b[, rel_tol, abs_tol])
# 求幂 math.pow(base, power)，不能处理复数，对比BIF及**运算符效率最高
# BIF pow(base, power[, modulus]) 等价于 base ** power % modulus，可以处理复数
# 以欧拉数作为底数的指数函数(自然对数) math.exp(power)

def si_exp(time: int | None = 100) -> None:
    """
    计算100毫克 锶-90 衰变100年后剩余的质量.

    放射性衰变公式：$N(t) = N(0) * e^{\\frac{-693t}{T}}$
    N(0): 初始质量
    N(t): 经过一段时间t后还没有衰减的量
    T: 衰变的半衰期
    e: 欧拉数 math.e

    Args:
        time (int | None): 放射性元素衰变时间，默认值为 100 年
    """
    initial = 100 # 单位：毫克(mg)
    half_life = 38.1 # 单位：年
    remaining = initial * math.exp( -0.693 * time / half_life )
    print(f"100 毫克 锶-90 经过 {time}年衰变后剩余的量为 {remaining}毫克")

# 对数函数 math.log(x[, base])，其中base默认为math.e(相当于数学意义ln(x))
# math.log10(x) 与 math.log2(x) 是专用于计算以10和2为底的对数
# 对比math.log()精度更高

# 函数的意义是使具有明确功能的代码可以被复用
def gaussian(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    实现高斯函数，计算正态分布概率密度

    标准差 $\sigma$ 固定为 1 ， 数学期望 $\mu$ 固定为 2

    高斯函数公式：$g = 1/\sqrt{2*\sigma*\pi } \
                        * \exp( -0.5 * ((x-\mu) ** 2/\sigma))$

    Args:
        x (float): 随机变量 x 的值
        mu (float): 数学期望
        sigma (float): 标准差

    Returns:
        float: 随机变量的概率密度
    """
    g = 1 / math.sqrt(2*sigma*math.pi) \
            * math.exp(-0.5 * ((x - mu) ** 2/sigma))
    return g


def main() -> None:
    ...

if __name__ == "__main__":
    main()
