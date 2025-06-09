# -*- coding: utf-8 -*-

"""
《Python玩转数学问题》Chapter 2 用Python处理计算公式 章末习题
"""
from functools import reduce
from math import fatorial, pi, isclose


# Exercise 2.1 计算 15! n! = n * (n-1) * ... * 2 * 1
def factorial_recurse(n: int) -> int:
    """
    Return factorial result of n, using recursive.

    Args:
        n (int): max number in factorial calculation

    Returns:
        int: result of factorial calculation
    """
    # Basic Condition: when n == 1, return 1
    if n == 1:
        return 1
    # Recursive Condition: when n != 1, return n * factorial(n-1)
    else:
        return n * factorial_recurce(n - 1)

def factorial_forloop(n: int) -> int:
    """
    Return factorial result of n, using for loop.

    Args:
        n (int): max number in factorial calculation

    Returns:
        int: result of factorial calculation
    """
    
    if n < 0:
        return 0

    if n == 0:
        return 1

    templist = list(range(1, n + 1))
    result = 1
    for item in templist:
        result *= item
    return result

def factorial_reduce(n:int) -> int:
    """
    Return factorial result of n, using reduce function from functools module.

    Args:
        n (int): max number in factorial calculation

    Returns:
        int: result of factorial calculation
    """
    
    if n < 0:
        return 0

    if n == 0:
        return 1

    return reduce(lambda x, y: x*y, list(range(1, n + 1)))

def factorial_mathmodule(n: int) -> int:
    """
    Return factorial result of n, using factorial function from math module.

    Args:
        n (int): max number in factorial calculation

    Returns:
        int: result of factorial calculation
    """
    return factorial(n)

# Exercise 2.3 摄氏度与华氏度相互转换 F = 9/5*C + 32
def temperature_transform(base: str, temperature: int) -> None:
    """
    Transform temperature between Fahrenheit and Celsius.

    华氏温度(Fahrenheit): 使用水银作为测温物质，定冰的熔点为32度，沸点为212度，
            中间分为180度，以°F表示
    摄氏温度(Celsius)   : 使用标准大气压下的水作为测温物质，把冰水混合物温度
            定为0摄氏度，水的沸点定为100摄氏度，根据水的这两个固定温度点对温度
            进行分度，两点之间作100等分，每段间隔称为1摄氏度，记作1°C

    Args:
        base (str): standards for provided temperature
        temperature (int): number of temperature
    """
    def f_to_c(temperature: int) -> int:
        """
        Transform temperature from Fahrenheit to Celsius.

        C = (F - 32) / 1.8

        Args:
            temperature (int): Fehrenheit temperature number

        Returns:
            int: Celsius temperature result
        """
        return (temperature - 32) / 1.8

    def c_to_f(temperature: int) -> int:
        """
        Transform temperature from Celsius to Fehrenheit.

        F = C * 1.8 + 32

        Args:
            temperature (int): Celsius temperature number

        Returns:
            int: Fehrenheit temperature result
        """
        return temperature * 1.8 + 32

    match base.lower():
        case "fehrenheit":
            f_temp = temperature
            c_temp = f_to_c(temperature)
            print(f"Fehrenheit temperature: {f_temp:.1f}°F\
                    \nCelsius temperature: {c_temp:.1f}°C")
        case "celsius":
            f_temp = c_to_f(temperature)
            c_temp = temperature
            print(f"Fehrenheit temperature: {f_temp:.1f}°F\
                    \nCelsius temperature: {c_temp:.1f}°C")
        case _:
            print("Please provide correct temp standard.\
                    \nOnly support Fehrenheit and Celsius.")

# Exercise 2.4 计算n年后银行存款总资产 A * ((1 + p / 100) ** n)
def total_refund(origin_refund: int, n: int) -> float:
    """
    Return total refund after n years with origin_refund.

    result = origin_refund * ((1 + percent / 100)  ** n)

    Args:
        origin_refund (int): money store in bank at first year
        n (int): number of years pass through

    Returns:
        float: result of total refund after n years
    """
    percent = 3
    return origin_refund * ((1 + percent / 100) ** n)

# Exercise 2.5 计算不同半径 r 和时间 T 下物体保持匀速圆周运动所需的向心力
def centripetal_force(radius: float, time: float) -> float:
    """
    返回匀速圆周运动下，不同半径 r 和时间 T 的物体向心力

    $a_c = frac{v^2}{r}$
    $v = frac{2 * pi * r}{T}
    T为物品途径一周的时间，单位秒(s)

    Args:
        radius (float): 物体匀速圆周运动的半径,单位：厘米(cm)
        time (float): 物体运动途径一周的时间，单位：秒(s)

    Returns:
        float: 物体匀速圆周运动下的向心力
    """
    v = (2 * pi * radius) / time
    return v ** 2 / radius

# Exercise 2.6 验证浮点数运算精度对计算结果的影响
def float_close() -> None:
    """
    验证浮点数运算精度对计算结果的影响。
    
    """
    x = 1
    y = 1 + 10**(-14) * 3**0.5
    result1 = 10**14 * (y-x)
    result2 = 3 ** 0.5
    # 结果差值
    print(f"结果差值(绝对值)为：{abs(result1-result2):.16f}")
    
    # 数学意义上 $10^14(y-x) = \sqrt{3}$
    # 无处理情况下浮点数运算精度对计算结果的影响
    print(f"无处理情况下 10^14(y-x) = sqrt(3) 的结果是{result1 == result2}")
    
    # 通过使用公差值
    toc = 1e-14
    print(f"使用公差值情况下 10^14(y-x) = sqrt(3) 的结果是\
              {abs(result1 - result2) < toc}")
    
    # 通过 math 模块的 isclose() 函数
    # 当满足以下条件时，math.isclose()返回值为 True
    # $abs(a-b)<=max(rel_{tol} * max(abs(a), abs(b)), abs_{tol})$
    # 相对容差 $rel_{tol}$ 指实际值与预期值之间的差异相对于预期值的量值(百分比)
    # 默认相对容差为1e-09
    # 绝对容差 $abs_{tol}$ 指认为"接近"的最大差值，不管输入值的大小
    # 默认绝对容差为0.0，可以考虑调整为绝对容差为公差值1e-14
    # 默认参数下的 isclose() 函数
    print(f"使用默认参数 isclose() 情况下 10^14(y-x) = sqrt(3) 的结果是\
              {isclose(result1, result2)}")
    print(f"使用0.001 相对容差 isclose() 情况下 10^14(y-x) = sqrt(3) 的结果是\
              {isclose(result1, result2, rel_tol=0.001)}")
    print(f"使用0.001 绝对容差 isclose() 情况下 10^14(y-x) = sqrt(3) 的结果是\
            {isclose(result1, result2, abs_tol=0.001)}")
    print(f"使用1e-14 绝对容差 isclose() 情况下 10^14(y-x) = sqrt(3) 的结果是\
            {isclose(result1, result2, abs_tol=1e-14)}")

def main() -> None:
    # Exercise 2.1
    print(factorial_recurse(4))
    print(factorial_forloop(4))
    print(factorial_reduce(4))
    print(factorial_mathmodule(4))

    # Exercise 2.3
    temperature_transform(base="fehrenheit", temperature=104) # c_temp=40
    temperature_transform(base="celsius", temperature=30) # f_temp=86

    # Exercise 2.4
    print(f"初始存入1_000元，每年3%利率，5年后该账户资产值为\
            {total_refund(origin_refund=1_000, n=5)}")

    # Exercise 2.5
    print(f"半径5cm， 环绕一圈20s的匀速圆周运动物体，承受的向心力为\
            {centripetal_force(radius=5, time=20):.3f}N")

    # Exercise 2.6
    float_close()

if __name__ == "__main__":
    main()
