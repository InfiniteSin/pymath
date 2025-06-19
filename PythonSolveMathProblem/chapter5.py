"""《Python玩转数学问题》Chapter 5 Python 绘图."""

from collections.abc import Callable
from math import pi, sin
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.ticker import Locator

# from matplotlib.pyplot import plot, show


# 折线图
def line_chart(data: list[list[int]]) -> None:
    """Draw line chart.

    Args:
        data (list[list[int]]): test data

    """
    x_axis: list[int] = data[0]
    y_axis: list[int] = data[1]
    plt.plot(x_axis, y_axis)
    plt.show()


def line_chart_marker(data: list[list[int]]) -> None:
    """Draw line chart, with markers.

    Args:
        data (list[list[int]]): test data

    """
    x_axis: list[int] = data[0]
    y_axis: list[int] = data[1]
    plt.plot(x_axis, y_axis, marker="o")
    plt.show()


def line_chart_nomarker(data: list[list[int]]) -> None:
    """Draw line chart, with markers, without "marker" key word.

    Args:
        data (list[list[int]]): test data

    """
    x_axis: list[int] = data[0]
    y_axis: list[int] = data[1]
    plt.plot(x_axis, y_axis, "o")
    plt.show()


# 散点图
def scatter_chart(data: list[list[int]]) -> None:
    """Draw scatter chart.

    Args:
        data (list[list[int]]): test data

    """
    x_axis: list[int] = data[0]
    y_axis: list[int] = data[1]
    plt.scatter(x_axis, y_axis)
    plt.show()


# 柱状图
def bar_chart(data: list[list[int]]) -> None:
    """Draw bar chart.

    Args:
        data (list[list[int]]): test data

    """
    x_axis: list[int] = data[0]
    y_axis: list[int] = data[1]
    plt.bar(x_axis, y_axis)
    plt.show()


# 关键字参数 color(代码中为 c) 可以指定线条颜色
# 可选颜色字符集合: {'b': blue, 'g': green, 'r': red, 'c': cyan(青色),
#                   'm': magenta(洋红色), 'y': yellow, 'k': black, 'w':white}
# 关键字参数 linestyle(代码中为 ls) 指定线条类型


# 同时绘制多条线条
def weather_linechart() -> None:
    """Draw line chart using weather data."""
    month: list[int] = list(range(1, 13))
    beijing: list[int] = [-3, 0, 6, 13, 20, 24, 26, 25, 20, 13, 5, -5]
    shanghai: list[int] = [4, 5, 8, 15, 20, 23, 28, 27, 23, 18, 12, 6]
    guangzhou: list[int] = [14, 15, 18, 22, 26, 27, 28, 28, 27, 24, 20, 15]
    # plt.subplot(121)
    # plt.plot(month, beijing, month, shanghai, guangzhou)  # 最后一组只有 Y 坐标, X 坐标将只用默认值(range(0~len()))
    # plt.legend(["Beijing", "Shanghai", "Guangzhou"], loc="best")  # 图例

    # plt.subplot(122)
    # plt.plot(month, beijing, month, shanghai, month, guangzhou)
    # plt.legend(["Beijing", "Shanghai", "Guangzhou"], loc="best")  # 图例

    # plot() 返回 list[Line2D], 可以通过setp()修改每个 Line2D 对象的属性
    # bj, sh, gz = plt.plot(month, beijing, month, shanghai, month, guangzhou)
    # plt.setp(bj, c="k", ls="-", label="Beijing")
    # plt.setp(sh, c="r", ls="-.", label="Shanghai")
    # plt.setp(gz, c="b", ls="--", label="Guangzhou")

    # 可以直接使用 plot() 依次创建 Line2D 对象并指明对象属性
    plt.plot(month, beijing, c="k", ls="-", label="Beijing")
    plt.plot(month, shanghai, c="r", ls="-.", label="Shanghai")
    plt.plot(month, guangzhou, c="b", ls="--", label="Guangzhou")

    # 当只含有一个子图时, 对子图对象设置属性相当于对整个图形对象设置属性
    plt.legend(loc="best")  # 当 Line2D 对象创建时已经指定 label 属性, legend() 不需要额外传入 label 列表
    plt.title("Average temperature in Beijing, Shanghai & Guangzhou")
    plt.xlabel("Month")
    plt.ylabel("Degrees Celsius")

    plt.show()


# 绘制函数图像: 通过足够多的数据点使线条平滑
def sin_chart() -> None:
    """Draw sin() function chart."""
    x: list[float] = [0.01 * i for i in range(201)]
    y: list[float] = [sin(pi * i * 0.01) * 2 for i in range(201)]
    plt.plot(x, y, linewidth=1, c="k", marker=".", markerfacecolor="k", markersize=8)
    plt.show()


def func_plot(f: Callable, start: int, stop: int, step: float, lab: str) -> None:
    """绘制函数图形.

    Args:
        f (Callable): 待绘制的函数
        start (int): 自变量的起始值, 默认为 0
        stop (int): 自变量的终止值, 默认为 100
        step (int): 自变量递增值, 默认为 1
        lab (str): 函数说明字符串

    """
    i = start
    # 生成 x, y 一一对应的函数数值列表
    x: list[float] = []
    y: list[float] = []
    while i < stop:
        x.append(i)
        y.append(f(i))
        i += step  # 通过足够小的步进使函数图像更加平滑

    # 绘图
    plt.plot(x, y)
    plt.xlabel(r"$ x $")
    plt.ylabel(r"$ y $")
    if lab is None:
        plt.title("Plot for simple function")
    else:
        plt.title("Plot for func: " + lab)
    plt.show()


# 中文标签及 text(), annotate()
def cn_chart() -> None:
    """Figure with Chinese characters."""
    # 修改全局字体库
    # plt.rcParams["font.sans-serif"] = ["SimHei"]  # 将字体替换为黑体
    # plt.rcParams["axes.unicode_minus"] = False  # 解决坐标轴负数的负号显示问题

    fig: Figure = plt.figure()  # 创建图形
    ax: Axes = fig.add_subplot(111)  # 创建子图 1行 1列 第一个位置
    ax.set(xlim=(0, 10), ylim=(0, 10))  # 设置 x 轴和 y 轴的长度

    # 为不同 label 设置不同的字体
    ax.set_xlabel("黑体 x 轴", fontproperties="SimHei", size=18)  # 黑体
    ax.set_ylabel("宋体 y 轴", fontproperties="SimSun", size=18)  # 宋体
    ax.set_title("楷体 标题", fontproperties="KaiTi", size=28)  # 楷体

    # 在指定坐标点添加文字
    ax.text(2, 6, r"$E = mc^2$", fontsize=15)  # 在 (2, 6) 处添加质能方程
    ax.text(4, 0.05, "X 轴上的彩色文本", font="SimHei", verticalalignment="bottom", color="green", fontsize=15)

    # 在指定坐标绘制点, 并为其增加注释
    ax.plot([2], [1], "o")  # plot() 前两位参数类型必须为 list[int | float]
    ax.annotate(
        "注释",
        xy=(2, 1),
        xytext=(3, 4),
        font="SimHei",
        fontsize=18,
        arrowprops={"facecolor": "black", "shrink": 0.05},
    )

    plt.show()


# subplot(rows, cols, loc) 添加单个子图
# 其中 loc 可以是包含两个正整数的元组 (a:int, b:int), 表示包含同一行连续多个网格的子图
def weather_subplot() -> None:
    """使用 subplot() 绘制多个子图."""
    # 修改全局字体库
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 将字体替换为黑体
    plt.rcParams["axes.unicode_minus"] = False  # 解决坐标轴负数的负号显示问题

    # 创建 12*8 的图形对象
    plt.figure(figsize=(12, 8))

    # 折线图数据
    month: list[int] = list(range(1, 13))
    beijing: list[int] = [-3, 0, 6, 13, 20, 24, 26, 25, 20, 13, 5, -5]
    shanghai: list[int] = [4, 5, 8, 15, 20, 23, 28, 27, 23, 18, 12, 6]
    guangzhou: list[int] = [14, 15, 18, 22, 26, 27, 28, 28, 27, 24, 20, 15]

    # 创建第一个子图 - 折线图
    plt.subplot(211)
    plt.plot(month, beijing, c="k", label="北京")
    plt.plot(month, shanghai, c="r", ls="-.", label="上海")
    plt.plot(month, guangzhou, c="b", ls=(0, (1, 2, 4, 8)), label="广州")
    plt.legend(loc="best")
    plt.title("北、上、广的月平均温度")
    plt.xlabel("月")
    plt.ylabel("摄氏度")

    # 柱状图数据
    bj_h: list[int] = [1, 3, 11, 19, 25, 29, 30, 29, 25, 18, 9, 2]
    sh_h: list[int] = [7, 8, 11, 18, 23, 27, 31, 30, 26, 22, 16, 10]
    gz_h: list[int] = [17, 17, 20, 25, 28, 30, 32, 32, 31, 17, 23, 20]
    w: float = 0.2
    bj_x: list[float] = [i - w for i in range(1, 13)]
    sh_x: list[float] = month
    gz_x: list[float] = [i + w for i in range(1, 13)]

    # 创建第二个子图 - 柱状图
    plt.subplot(212)
    plt.bar(bj_x, bj_h, w, label="北京")
    plt.bar(sh_x, sh_h, w, hatch="/", label="上海")
    plt.bar(gz_x, gz_h, w, hatch="O", label="广州")
    plt.legend(loc="best")
    plt.title("北、上、广的月平均最高温度")
    plt.xlabel("月")
    plt.ylabel("摄氏度")
    # plt.legend(loc="best")

    # 重置 x 轴主刻度
    x_major_locator: Locator = plt.MultipleLocator(1)  # 主刻度间隔 1
    ax: Axes = plt.gca()  # 当前子图为柱状图 get_current_axes
    print(ax.xaxis.get_major_locator()())
    ax.xaxis.set_major_locator(x_major_locator)
    plt.tight_layout()  # 通过默认参数调整子图在图形对象中的呈现
    plt.show()


# subplots() 创建一幅图形和一组子图
def weather_subplots() -> None:
    """使用 subplots() 绘制多个子图."""
    # 修改全局字体库
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 将字体替换为黑体
    plt.rcParams["axes.unicode_minus"] = False  # 解决坐标轴负数的负号显示问题

    # 数据
    month: list[int] = list(range(1, 13))
    beijing: list[int] = [-3, 0, 6, 13, 20, 24, 26, 25, 20, 13, 5, -5]
    shanghai: list[int] = [4, 5, 8, 15, 20, 23, 28, 27, 23, 18, 12, 6]
    guangzhou: list[int] = [14, 15, 18, 22, 26, 27, 28, 28, 27, 24, 20, 15]
    bj_h: list[int] = [1, 3, 11, 19, 25, 29, 30, 29, 25, 18, 9, 2]
    sh_h: list[int] = [7, 8, 11, 18, 23, 27, 31, 30, 26, 22, 16, 10]
    gz_h: list[int] = [17, 17, 20, 25, 28, 30, 32, 32, 31, 17, 23, 20]

    # 创建图形和子图列表
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))

    # 获取各子图默认主刻度
    print(ax2.xaxis.get_major_locator()())
    print(ax2.yaxis.get_major_locator()())

    # 绘制月平均温度曲线
    bj, sh, gz = ax1.plot(month, beijing, month, shanghai, month, guangzhou)
    plt.setp(bj, c="k", label="北京")
    plt.setp(sh, c="r", ls="-.", label="上海")
    plt.setp(gz, c="b", ls=(0, (1, 2, 4, 8)), label="广州")
    ax1.legend(loc="best")
    ax1.set_title("北、上、广的月平均温度")
    ax1.set_xlabel("月")
    ax1.set_ylabel("摄氏度")

    # 绘制月平均最高温度柱状图
    w: float = 0.2
    bj_x: list[float] = [i - w for i in range(1, 13)]
    sh_x: list[float] = month
    gz_x: list[float] = [i + w for i in range(1, 13)]
    ax2.bar(bj_x, bj_h, w, label="北京")
    ax2.bar(sh_x, sh_h, w, hatch="/", label="上海")
    ax2.bar(gz_x, gz_h, w, hatch="O", label="广州")
    ax2.legend(loc="best")
    ax2.set_title("北、上、广的月平均最高温度")
    ax2.set_xlabel("月")
    ax2.set_ylabel("摄氏度")

    # 显示当前 x 轴和 y 轴的主刻度
    print(ax2.xaxis.get_major_locator()())
    print(ax2.yaxis.get_major_locator()())

    # 重置 x 轴主刻度
    x_major_locator: Locator = plt.MultipleLocator(1)  # 主刻度间隔 1
    ax2.xaxis.set_major_locator(x_major_locator)
    x_minor_locator: Locator = plt.MultipleLocator(1)  # 从刻度间隔 1
    ax2.xaxis.set_minor_locator(x_minor_locator)

    # 优化子图呈现
    plt.tight_layout()
    plt.show()


# 通过 subplot2grid() 更灵活地创建子图
def test_subplot2grid() -> None:
    """使用 subplot2grid() 灵活创建子图."""
    # 修改全局字体库
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 将字体替换为黑体
    plt.rcParams["axes.unicode_minus"] = False  # 解决坐标轴负数的负号显示问题

    def annotate_axes(fig: Figure) -> None:
        """修改子图参数并在子图中心位置添加说明文本."""
        for i, ax in enumerate(fig.axes):
            ax.set_xticks([])  # 清除 x 轴刻度
            ax.set_yticks([])  # 清除 y 轴刻度
            ax.text(0.5, 0.5, f"子图{i + 1}", va="center", ha="center")

    fig: Figure = plt.figure()
    ax1: Axes = plt.subplot2grid((3, 3), (0, 0), colspan=3)
    ax2: Axes = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    ax3: Axes = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    ax4: Axes = plt.subplot2grid((3, 3), (2, 0))
    ax5: Axes = plt.subplot2grid((3, 3), (2, 1))

    annotate_axes(fig)

    plt.show()


def main() -> None:
    """Entry Function."""
    test_data1: list[list[int]] = [[2, 3, 4, 5], [4, 9, 16, 25]]  # noqa: F841
    # line_chart(test_data1) # 无标记折线图
    # line_chart_marker(test_data1)  # 带标记折线图
    # line_chart_nomarker(test_data1)  # 通过折线图去除线条实现的散点图
    # scatter_chart(test_data1) # 散点图
    # bar_chart(test_data1) # 柱状图
    # weather_linechart()
    # sin_chart()
    # func: Callable = lambda x: exp(-x) * sin(2 * pi * x)
    # func_plot(func, 0, 4, 0.01, r"$\exp^{-x}\sin(2\pi{x})$")
    # cn_chart()
    # weather_subplot()
    # weather_subplots()
    test_subplot2grid()


if __name__ == "__main__":
    main()
