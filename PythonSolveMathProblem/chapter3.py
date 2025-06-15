"""《Python玩转数学问题》Chapter 3 函数与分支."""

import math

import pytest


# 使用阶乘计算组合数和排列数
def permutation(total_amount: int, pick_amount: int) -> float:
    r"""使用阶乘计算排列.

    排列: 从 n 个不同的元素中, 取 r 个不重复的元素, 按次序排列
    其全体集合用 A(n, r) 表示

    计算公式: $A_n^r = n*(n-1)*...*(n-r+1) = \\frac{n!}{(n-r)!}$

    可以使用 math.perm(n, r) 直接获取结果

    Args:
        total_amount (int): 元素的总集合
        pick_amount (int): 预期取出的不重复元素个数

    Returns:
        float: 从 n 个元素中取 r 个的不重排列个数

    """
    return math.factorial(total_amount) / math.factorial(total_amount - pick_amount)


def combination(total_amount: int, pick_amount: int) -> float:
    r"""使用阶乘计算组合.

    排列: 从 n 个不同的元素中, 取 r 个不重复的元素, 不考虑其元素顺序
    其全体集合用 C(n, r) 表示
    相当于把排列带来的顺序去掉

    计算公式: $C_n^r = n*(n-1)*...*(n-r+1) = \\frac{n!}{(r)!*(n-r)!}$
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

    return factorial(total_amount) / (factorial(pick_amount) * factorial(total_amount - pick_amount))


# math 模块中的常量
# 圆周率 math.pi
# Tau math.tau
def circle(radius: int) -> None:
    r"""使用 math.pi 及 radius 计算圆的周长及面积.

    圆周率是圆的周长与直径之比 $\\pi = C / d$
    Tau 是圆的周长与半径之比, 恒等于 $2\\pi$, 常用于简化带有 $2\\pi$的公式

    圆的周长公式: $C = 2 * \\pi * r$
    变体: $C = \\pi * \\tau$

    圆的面积公式: $S = \\pi * (r ** 2)$

    Args:
        radius (int): 圆的半径

    """
    circumference = 2 * math.pi * radius
    # circumference = math.tau * radius # 使用 math.tau 代替 2 * math.pi

    square = math.pi * (radius**2)

    print(
        f"圆的周长 = 2 * {math.pi} * {radius} = {circumference}\
            \n圆的面积 = {math.pi} * ({radius} ** 2) = {square}",
    )


# 欧拉数 math.e
def exponential(origin: int, time: int) -> None:
    r"""计算指数增长与指数衰变.

    指数增长 $y(t) = y_0 * e^{kt}$
    指数衰变 $y(t) = y_0 * e^{-kt}$
    y(t): 表示时间t时的数量
    y_0: 表示初始数量
    k: 表示增长率/衰减率
    e: 自然对数,math.e

    Args:
        origin: 初始数量
        time: 时间

    """
    k = 0.025
    increase_result = origin * math.exp(k * time)
    decrease_result = origin * math.exp(-k * time)
    print(
        f"初始数量 {origin}g 经过时间 {time}s 后: \
            指数增长结果 {increase_result}\
            \n指数衰减结果 {decrease_result}\
            \n增长率为 {k}",
    )


# 无穷大 math.inf, 相当于float("inf"), 大于任何数(包括双精度浮点数最大值10e308)
# 负无穷大 -math.inf
# 非数值NaN math.nan, 相当于float("nan")

# math 内置库提供的数学运算函数
# 阶乘函数 math.factorial(<int>), 只接受非负整数
# 大于或等于给定值的最小整数 math.ceil(<float>), 向上取整
# 小于或等于给定值的最接近整数 math.floor(<float>), 向下取整
# 完全舍弃小数位 math.trunc(<float>), 正数向下取整, 负数向上取整
# 判断两个数是否足够接近 math.isclose(a, b[, rel_tol, abs_tol])
# 求幂 math.pow(base, power), 不能处理复数, 对比BIF及**运算符效率最高
# BIF pow(base, power[, modulus]) 等价于 base ** power % modulus, 可以处理复数
# 以欧拉数作为底数的指数函数(自然对数) math.exp(power)


def si_exp(time: int = 100) -> None:
    r"""计算100毫克 锶-90 衰变100年后剩余的质量.

    放射性衰变公式: $N(t) = N(0) * e^{\\frac{-693t}{T}}$
    N(0): 初始质量
    N(t): 经过一段时间t后还没有衰减的量
    T: 衰变的半衰期
    e: 欧拉数 math.e

    Args:
        time (int | None): 放射性元素衰变时间, 默认值为 100 年

    """
    initial = 100  # 单位: 毫克(mg)
    half_life = 38.1  # 单位: 年
    remaining = initial * math.exp(-0.693 * time / half_life)
    print(f"100 毫克 锶-90 经过 {time}年衰变后剩余的量为 {remaining}毫克")


# 对数函数 math.log(x[, base]), 其中base默认为math.e(相当于数学意义ln(x))
# math.log10(x) 与 math.log2(x) 是专用于计算以10和2为底的对数
# 对比math.log()精度更高


# 函数的意义是使具有明确功能的代码可以被复用
def gaussian(x: float, mu: float = 0, sigma: float = 1) -> float:
    r"""实现高斯函数, 计算正态分布概率密度.

    标准差 $\\sigma$ 固定为 1 , 数学期望 $\\mu$ 固定为 2

    高斯函数公式: $g = 1/\\sqrt{2*\\sigma*\\pi } \
                        * \\exp( -0.5 * ((x-\\mu) ** 2/\\sigma))$

    Args:
        x (float): 随机变量 x 的值
        mu (float): 数学期望
        sigma (float): 标准差

    Returns:
        float: 随机变量的概率密度

    """
    g = 1 / math.sqrt(2 * sigma * math.pi) * math.exp(-0.5 * ((x - mu) ** 2 / sigma))
    return g  # noqa: RET504


# Exercise
# Exercise 3.1 编写计算长方形体积的函数及其测试函数
def volume_cal(length: float, width: float, height: float) -> float:
    """计算长方体的体积.

    公式 V = length * width * height

    Args:
        length (float): 长方体的长
        width (float): 长方体的宽
        height (float): 长方体的高

    Returns:
        float: 长方体的体积

    """
    err_condition: list = [length <= 0, width <= 0, height <= 0]
    err_msg: str = "长方体的任一边长均必须大于0."
    if any(err_condition):
        raise ValueError(err_msg)
    volume = length * width * height
    return float(volume)


def test_volume_cal() -> None:
    """volume_cal()函数的测试函数."""
    assert volume_cal(1, 1, 1) == 1.0, "边长为 1 的立方体面积不为 1"
    assert volume_cal(1, 2, 3.5) == 7.0, "边长分别为 1, 2, 3.5 的长方体面积不为 7.0"

    with pytest.raises(ValueError, match="长方体的任一边长均必须大于0."):
        volume_cal(0, 1, 1)
    with pytest.raises(ValueError, match="长方体的任一边长均必须大于0."):
        volume_cal(2, -1, 1)


# Exercise 3.2 编写使用指定公式计算三角形面积的函数及其测试函数
def triangle_area(a: int, b: int, c: int) -> float:
    r"""计算根据 3 边长计算三角形的面积.

    计算公式: $A = \sqrt{s(s-a)(s-b)(s-c)}, s=\frac{a+b+c}{2}$

    Args:
        a (int): 三角形的边长
        b (int): 三角形的边长
        c (int): 三角形的边长

    Returns:
        float: 三角形的面积

    """
    err_condition: list = [a <= 0, b <= 0, c <= 0]
    err_msg: str = "三角形的任一边长均必须大于0."
    if any(err_condition):
        raise ValueError(err_msg)
    s: float = (a + b + c) / 2
    area: float = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 3)


def test_triangle_area() -> None:
    """triangle_area()的测试函数."""
    assert triangle_area(1, 1, 1) == 0.433, "边长均为 1 的三角型面积不为 0.433"
    assert triangle_area(3, 4, 5) == 6.000, "边长分别为 3, 4, 5 的三角型面积不为 6.000"
    assert triangle_area(7, 8, 9) == 26.833, "边长分别为 7, 8, 9 的三角型面积不为 26.833"
    with pytest.raises(ValueError, match="三角形的任一边长均必须大于0."):
        triangle_area(2, -1, 1)


# Exercise 3.3 计算物体从高度 H(单位: m)处下落所需要的时间 t, 及其测试函数
def droptime(height: float) -> float:
    r"""计算物体从高度 H(单位: m)处下落所需要的时间 t.

    由自由落体公式: $h = \frac{g * t^2}{2}$可知, 下落时间 $t = \sqrt{2h / g}$

    Args:
        height (float): 物体下落的高度

    Returns:
        float: 物体从高度 H 处下落所需要的时间

    """
    if height < 0:
        height = abs(height)
    g: float = 9.8
    time: float = math.sqrt(2 * height / g)
    return round(time, 3)


def test_droptime() -> None:
    """droptime()的测试函数."""
    assert math.isclose(droptime(1), 0.452), "H = 1m 时物体自由下落的时间 ≠ 0.452s"
    assert math.isclose(droptime(10), 1.428), "H = 10m 时物体自由下落的时间 ≠ 1.428s"
    assert math.isclose(droptime(0), 0.000), "H = 0m 时物体自由下落的时间 ≠ 0.000s"

    # 当 H 为负数时, 正常情况为无解, 但若考虑从 H = 0m 下落至给定 H 时, 则相当于计算 abs(H) 的下落时间 t
    assert math.isclose(droptime(-1), 0.452), (
        "H = -1m 时, 等价于计算物体从 H = 0m 下落至 H = -1m 时自由下落的时间 ≠ 0.452s"
    )


# Exercise 3.4 计算若干年后某人银行账户内的资产总额
def deposit(origin_deposit: float, year: int) -> float:
    r"""计算若干年后某人银行账户内的资产总额.

    计算公式: $f(n) = A(1 + \frac{p}{100})^n$
    A: 某人存入的初始资金
    p: 银行一年定期的存款利率
    n: 存款年限

    Args:
        origin_deposit (float): 初始资金
        year (int): 存款年限

    Returns:
        float: 若干年后银行账户内的资产总额

    """
    deposit_err_msg: str = "初始资金必须 >= 0"
    year_err_msg: str = "存款年限必须 >= 0"
    if origin_deposit < 0:
        raise ValueError(deposit_err_msg)
    if year < 0:
        raise ValueError(year_err_msg)
    p: int = 3  # 银行一年定期的存款利率, 频数形式形式
    p: float = p / 100  # 银行一年定期的存款利率, 频率形式
    final_deposit: float = origin_deposit * ((1 + p) ** year)
    return final_deposit


# Exercise 3.5 计算木卫四距离木星的距离、
def distance(t_a: float, t_b: float, r_b: float) -> float:
    r"""使用开普勒第三定律计算木卫四距离木星的距离.

    由开普勒第三定律: $(\frac{T_a}{T_b})^2 = (\frac{r_a}{r_b})^3$ 可得
    $r_a = r_b\sqrt[3]{(\frac{T_a}{T_b})^2}$

    Args:
        t_a (float): 木卫四围绕木星的公转周期(单位: 天)
        t_b (float): 木卫一围绕木星的公转周期(单位: 天)
        r_b (float): 木卫一距离木星的距离长度(单位: 距离长度)

    Returns:
        float: 木卫四距离木星的距离长度(单位: 距离长度)

    """
    r_a: float = r_b * math.cbrt(math.pow(t_a / t_b, 2))
    return round(r_a, 1)


def test_distance() -> None:
    """distance()的测试函数."""
    assert distance(t_a=16.7, t_b=1.8, r_b=4.2) == 18.544, "计算错误"


# Exercise 3.6 使用一元二次方程的求根公式求任意一元二次方程的实数解
def quadratic_formula(a: float, b: float, c: float) -> list[float] | None:
    r"""使用求根公式计算任意一元二次方程的实数解.

    一元二次方程形如: $ax^2 + bx + c = 0 (a!=0)$
    求根公式为: $x = \frac{-b\pm\sqrt{b^2 - 4ac}}{2a}$
    其中 $\Delta = b^2 - 4ac$ 为方程判别式, 可用于判断该方程是否具有实数根及实数根的个数
    当 $\Delta$ > 0, 方程具有 2 个实数根, 分别是 $x1 = \frac{-b+\sqrt{b^2 - 4ac}}{2a}$
    和 $x2 = \frac{-b-\sqrt{b^2 - 4ac}}{2a}$
    当 $\Delta$ = 0, 方程只有 1 个实数根, 可简化为 $x = \frac{-b}{2a}$
    当 $\Delta$ < 0, 方程没有实数根, 但在复数范围,
    方程有两个共轭复数跟 $x = \frac{-b}{2a} \pm \frac{\sqrt{-(b^2 - 4ac)}}{2a}i$

    Args:
        a (float): 二次项系数
        b (float): 一次项系数
        c (float): 常数项系数

    Returns:
        list[float] | None: 实数根

    """
    delta: float = b**2 - 4 * a * c
    if delta > 0:
        x_1: float = ((-b) + math.sqrt(delta)) / (2 * a)
        x_2: float = ((-b) - math.sqrt(delta)) / (2 * a)
        print(f"方程具有 2 个实数根, 分别是 {x_1} 和 {x_2}")
        return [x_1, x_2]
    elif delta == 0:
        x: float = (-b) / (2 * a)
        print(f"方程只有 1 个实数根 {x}")
        return [x]
    else:
        print("方程没有实数根")
        return None


def main() -> None:
    """Entry function."""


if __name__ == "__main__":
    main()
