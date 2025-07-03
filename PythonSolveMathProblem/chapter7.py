"""《Python玩转数学问题》Chapter 7 Numpy 与矩阵."""

from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

if TYPE_CHECKING:
    from matplotlib.figure import Figure


class Wave:
    r"""使用函数表示的物理中的波.

    函数表达式: $W(x,t) = Asin(\frac{2\pi}{\lambda}(x-vt))W(x,t) = Asin()$
    x: 位置
    t: 时间
    A: 波的振幅
    λ: 波长
    v: 波的速度
    """

    def __init__(self, amp: float, wl: float, v: float) -> None:
        """初始化波的波幅, 波长及速度.

        Args:
            amp (float): 波幅
            wl (float): 波长
            v (float): 波的速度

        """
        self.__amp: float = amp
        self.__wl: float = wl
        self.__v: float = v

    def get_wave(self, x: float, t: float = 0) -> float:
        """返回波在位置x及时间t时在坐标轴上的位置y.

        Args:
            x (float): 波的位置
            t (float): 时间

        Returns:
            float: 波在位置 x, 时间 t 时的坐标

        """
        wave: float = self.__amp * np.sin((2 * np.pi / self.__wl) * (x - self.__v * t))
        return wave

    @staticmethod
    def plot_wave(x: np.ndarray, ax: Axes, wave: float) -> None:
        """画出给定时刻波形图.

        Args:
            x (np.ndarray): 波的位置
            ax (Axes): matplotlib 的绘图对象
            wave: (float): 给定时刻波的坐标

        """
        ax.set_xlabel("x")
        ax.set_ylabel("W(x)")
        ax.set_title("给定时刻波形图", fontproperties="SimHei", size=28)  # 楷体
        ax.plot(x, wave)


def main() -> None:
    """Entry function."""
    # 使用 Numpy 创建波形图(波幅为2, 波长为5, 波速为2, 区间[-10, 10])
    # x: np.ndarray = np.linspace(-10, 10, 100)
    # wl: Wave = Wave(amp=2, wl=5, v=2)
    # fig: Figure = plt.figure()
    # wl.plot_wave(x=x, ax=plt.gca(), wave=wl.get_wave(x=x, t=0))
    # plt.show()
    # 创建2个波并把它们加起来
    sampling: int = 100
    x_range: list[int] = [-10, 10]
    amplitudes: list[float] = [1.7, 0.8]
    wavelengths: list[float] = [4, 7, 5]
    velocities: list[float] = [2, 1.5]

    x: np.ndarray = np.linspace(x_range[0], x_range[1], sampling)
    w1: Wave = Wave(amp=amplitudes[0], wl=wavelengths[0], v=velocities[0])
    w2: Wave = Wave(amp=amplitudes[1], wl=wavelengths[1], v=velocities[1])

    fig: Figure = plt.figure()  # noqa: F841
    # w1.plot_wave(x=x, ax=plt.gca(), wave=w1.get_wave(x=x, t=0))
    # w2.plot_wave(x=x, ax=plt.gca(), wave=w2.get_wave(x=x, t=0))
    # plt.show()

    # 将两个波叠加后呈现
    # Wave.plot_wave(x=x, ax=plt.gca(), wave=(w2.get_wave(x=x, t=0) + w1.get_wave(x=x, t=0)))

    # 绘制不同时间 t 的叠加波运动
    for time in np.arange(0, 40, 0.2):
        plt.clf()  # Clear last figure
        Wave.plot_wave(x=x, ax=plt.gca(), wave=(w2.get_wave(x=x, t=time) + w1.get_wave(x=x, t=time)))
        plt.ylim(-3, 3)  # Fix the limits on the y-axis
        plt.pause(0.1)
    plt.show()


if __name__ == "__main__":
    main()
