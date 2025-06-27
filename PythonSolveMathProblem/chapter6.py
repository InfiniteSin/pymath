"""《Python玩转数学问题》Chapter 6 类和面向对象编程."""

import math
from math import isclose, pi, sin
from typing import TYPE_CHECKING, Any, Callable  # noqa: UP035

import matplotlib.pyplot as plt
import sympy
from scipy.constants import G

if TYPE_CHECKING:
    from matplotlib.axes import Axes


class UniGravity:
    """两个物体间的万有引力.

    Attributes:
        m1 (float): 物体 1 的质量
        m2 (float): 物体 2 的质量

    """

    def __init__(self, m1: float, m2: float) -> None:
        """Init attributes."""
        self.m1 = m1
        self.m2 = m2

    def value(self, r: float) -> float:
        """计算并返回两个物体间的万有引力结果.

        Args:
            r (float): 两个物体间的距离

        Returns:
            float: 两个物体间的万有引力

        """
        return self.m1 * self.m2 * G / (r**2)


class ClassTemplate:
    """类的通用模板."""

    # 类属性
    class_var1: int = 0
    class_var2: str = ""

    def __init__(self, p1: int) -> None:
        """构造函数, 初始化类的实例的属性."""
        self.attr1: int = p1

        # 访问类属性, 前缀是类名
        ClassTemplate.class_var1 += 1

    def method1(self, p2: int) -> int:
        """实例方法说明."""
        result: int = self.attr1 + p2

        # 创建新的实例属性
        if True:
            self.attr2: int = p2
        return result

    # 实例方法
    def instance_method(self) -> str:
        """实例方法例子."""
        return f"instance method called {self}"

    @classmethod
    def class_method(cls) -> str:
        """类方法例子."""
        return f"class method called {cls}"

    @staticmethod
    def static_method() -> str:
        """静态方法例子."""
        return "static method called"


class Derivative2:
    """求二阶导数."""

    def __init__(self, f: Callable, h: float = 1e-6) -> None:
        r"""构造函数.

        Args:
            f (Callable): 数学函数 $f(x) = x^2 - 1$
            h (float): 公差值, 默认为 1e-6

        """
        self.f: Callable = f
        self.h: float = float(h)

    def __call__(self, x: float) -> float:
        """调用函数."""
        f: Callable = self.f
        h: float = self.h
        r: float = (f(x - h) - 2 * f(x) + f(x + h)) / float(h * h)
        return r

    def __str__(self) -> str:
        """print(Instance)时打印返回的字符串."""
        return "函数 f(x)=x^2 - 1 的二阶导数形式为:\
            \nf(x-h) - 2*f(x) + f(x+h)"


def test_Derivative2() -> None:
    """Derivative2的测试函数."""

    def f(x: float) -> float:
        r"""函数 $f(x) = x^2 -1$.

        Args:
            x (float): 函数入参

        Returns:
            float: 函数运算结果

        """
        return x**2 - 1

    d2f = Derivative2(f)
    d2sin = Derivative2(sin)
    assert isclose(d2f(1.5), 1.999733711954832), "函数f(x)的二阶导数在 x = 1.5 时计算有误"
    assert isclose(d2sin(pi), 0.0), "三角函数 sin 的二阶导数在 x = math.pi 时计算有误"
    assert isclose(d2sin(pi / 2), -1.000088900582341), "三角函数 sin 的二阶导数在 x = math.pi/2 时计算有误"


class Teacher1:
    """Teacher."""

    def __init__(self, name: str, age: int, gender: str, salary: float, course: list[str] | str) -> None:
        """Init teacher attributes."""
        self.name: str = name
        self.age: int = age
        self.gender: str = gender
        self.salary: float = salary
        self.course: list[str] = []
        if isinstance(course, list):
            self.course.extend(course)
        else:
            self.course.append(course)

    def __del__(self) -> None:
        """Trigger when delete instance."""
        print(f"[{self.name}] is unsigned.")

    def tell(self) -> None:
        """Represent all attributes and values."""
        print(f"{self.name:^9-}")
        for k, v in self.__dict__.items():
            print(k, v)
        print("----End----")

    def teaching(self) -> None:
        """Represent all cources the teacher is teaching."""
        print(f"Teacher {self.name} is teaching {', '.join(self.course)}")


class Student1:
    """Student."""

    def __init__(self, name: str, age: int, gender: str, course: list[str] | str, tuition: float) -> None:
        """Init student's attributes."""
        self.name: str = name
        self.age: int = age
        self.gender: str = gender
        self.course: list[str] = []
        if isinstance(course, list):
            self.course.extend(course)
        else:
            self.course.append(course)
        self.tuition: float = tuition  # 学费
        self.credit: int = 0

    def __del__(self) -> None:
        """Trigger when delete instance."""
        print(f"[{self.name}] is graduated.")

    def tell(self) -> None:
        """Represent all attributes and values."""
        print(f"{self.name:^9-}")
        for k, v in self.__dict__.items():
            print(k, v)
        print("----End----")

    def get_credit(self, credit: int) -> None:
        """Set credit."""
        self.credit += credit
        print(f"Student {self.name} has just got {credit} points of credits.")


# 类与继承
class SchoolMember2:
    """School member base class."""

    __member_num: int = 0

    def __init__(self, name: str, age: int, gender: str) -> None:
        """Init attributes."""
        # 将所有属性设为受保护属性, 对外部修改封闭
        self._name: str = name
        self._age: int = age
        self._gender: str = gender
        self.__enroll()

    def __del__(self) -> None:
        """Trigger when delete instance."""
        self.__unregister()

    def __enroll(self) -> None:
        """Register when any instance of class or subclass is created."""
        SchoolMember2.__member_num += 1

    def __unregister(self) -> None:
        """Unregister when any instance of class or subclass is deleted."""
        SchoolMember2.__member_num -= 1

    def tell(self) -> None:
        """Represent all attributes and values."""
        print(f"----{self._name}----")
        for k, v in self.__dict__.items():
            print(k, v)
        print("----End----")


class Teacher2(SchoolMember2):
    """Teacher but subclass of SchoolMember2."""

    def __init__(self, name: str, age: int, gender: str, course: list[str] | str, salary: float) -> None:
        """Init teacher attributes.

        Init super class's attributes use super()
        Init extra attributes.
        """
        super().__init__(name, age, gender)  # 通过 super() 继承基类的属性
        self._salary: float = float(salary)
        self._course: list[str] = []
        if isinstance(course, list):
            self._course.extend(course)
        else:
            self._course.append(course)
        print(f"Teacher {self._name} is registered.")

    def __del__(self) -> None:
        """Trigger when delete instance."""
        super().__del__()
        print(f"Teacher {self._name} is unregistered.")

    def teaching(self) -> None:
        """Represent all cources the teacher is teaching."""
        print(f"Teacher {self._name} is teaching {', '.join(self._course)}")


class Student2(SchoolMember2):
    """Student but subclass of SchoolMember2."""

    def __init__(self, name: str, age: int, gender: str, course: list[str] | str, tuition: float) -> None:
        """Init student attributes.

        Init super class's attributes use super()
        Init extra attributes.
        """
        super().__init__(name, age, gender)  # 通过 super() 继承基类的属性
        self._tuition: float = float(tuition)
        self._course: list[str] = []
        if isinstance(course, list):
            self._course.extend(course)
        else:
            self._course.append(course)
        self._credit: int = 0
        print(f"Student {self._name} is registered.")

    def __del__(self) -> None:
        """Trigger when delete instance."""
        super().__del__()
        print(f"Student {self._name} is unregistered.")

    def get_credit(self, credit: int) -> None:
        """Set credit."""
        self._credit += credit
        print(f"Student {self._name} has just got {credit} points of credits.")


# 继承与 MRO
class Rectangle:
    """矩形(基类).

    Attrs:
        length (float): 长
        width (float): 宽

    """

    def __init__(self, length: float, width: float, **kwargs: dict[str, Any]) -> None:
        """初始化矩形的边长."""
        self._length: float = length
        self._width: float = width
        super().__init__(**kwargs)

    def area(self) -> float:
        """返回矩形面积."""
        return self._length * self._width

    def perimeter(self) -> float:
        """返回矩形周长."""
        return 2 * (self._length + self._width)


class Square(Rectangle):
    """正方形(继承矩形)."""

    def __init__(self, length: float, **kwargs: dict[str, Any]) -> None:
        """初始化正方形的边长."""
        super().__init__(length=length, width=length, **kwargs)


class Cube(Square):
    """立方体(继承正方体)."""

    def surface_area(self) -> float:
        """返回立方体表面积."""
        face_area = super().area()
        return face_area * 6

    def volume(self) -> float:
        """返回立方体体积."""
        face_area = super().area()
        return face_area * self._length


# 多重继承
class Triangle:
    """三角形(基类).

    Attrs:
        base (float): 三角形的底长
        height (float): 三角形的高

    """

    def __init__(self, base: float, height: float, **kwargs: dict[str, Any]) -> None:
        """初始化三角形的底边和高."""
        self._base: float = base
        self._height: float = height
        super().__init__(**kwargs)

    def tri_area(self) -> float:
        """返回三角形面积."""
        return 0.5 * self._base * self._height


# RightPyramid(Triangle, Square) 的 MRO 顺序为 RightPyramid -> Triangle -> Square -> Rectangle -> object(通用基类)
# 这会导致通过 super().area() 方法调用的 area() 是 Triangle 类中计算三角形面积的 area
# 由于缺乏 height 属性会报错 AttributeError
# 通过改变 RightPyramid 的继承签名, 可以改变 MRO 顺序
class RightPyramid(Square, Triangle):
    """金字塔(继承自三角形和正方形).

    Attrs:
        base (float): 底边长度
        slant_height (float): 斜高, 斜面三角形底边上的高

    """

    def __init__(self, base: float, slant_height: float, **kwargs: dict[str, Any]) -> None:
        """初始化金字塔的底边长度和斜高."""
        self._base: float = base
        self._slant_height: float = slant_height
        kwargs["height"] = self._slant_height
        kwargs["length"] = self._base
        super().__init__(base=self._base, **kwargs)

    def area(self) -> float:
        """金字塔的表面积(底面积 + 四面三角形面积)."""
        base_area: float = super().area()
        perimeter: float = super().perimeter()
        return 0.5 * perimeter * self._slant_height + base_area

    def area2(self) -> float:
        """计算金字塔的表面积, 使用 Triangle 类的面积方法结果."""
        base_area: float = super().area()
        triangle_area: float = super().tri_area()
        return 4 * triangle_area + base_area


# OOP 面向对象实例
# 螺线
class Spiral:
    """螺线(基类).

    Attrs:
        theta (list[float]): 弧度
        radii (list[float]): 极径

    """

    def __init__(self) -> None:
        """初始化螺线的弧度及极径空列表."""
        self._theta: list[float] = []  # 转角
        self._radii: list[float] = []  # 轴长

    def draw(self) -> None:
        """绘制螺线."""
        # 创建极坐标
        ax: Axes = plt.axes((0.025, 0.025, 0.95, 0.95), polar=True)  # noqa: F841
        plt.plot(self._theta, self._radii)

        # 将默认角度转换为弧度
        plt.thetagrids(
            [0, 45, 90, 135, 180, 225, 270, 315],
            [
                "0",
                f"{sympy.pi}/4",
                f"{sympy.pi}/2",
                f"3{sympy.pi}/4",
                f"{sympy.pi}",
                f"5{sympy.pi}/4",
                f"3{sympy.pi}/2",
                f"7{sympy.pi}",
            ],
        )
        plt.show()


class Archimedes(Spiral):
    r"""阿基米德螺线.

    极坐标方程: $r = a\theta + b (a != 0)$
    """

    def __init__(self, a: float, b: float) -> None:
        """初始化阿基米德螺线的属性."""
        super().__init__()
        self._a: float = a
        self._b: float = b
        self.f()

    def f(self) -> None:
        """使用极坐标方程计算轴长和转角."""
        N: int = 200
        i: int = 0
        while i < N:
            t: float = i * 4 * math.pi / N
            self._theta.append(t)
            self._radii.append(self._a + self._b * t)
            i += 1


class Log(Spiral):
    r"""对数螺线.

    极坐标方程: $r = ae^(b\theta)$
    """

    def __init__(self, a: float, b: float) -> None:
        """初始化对数螺线的属性."""
        super().__init__()
        self._a: float = a
        self._b: float = b
        self.f()

    def f(self) -> None:
        """使用极坐标方程计算轴长和转角."""
        N: int = 800
        i: int = 0
        while i < N:
            t: float = i * 10 * math.pi / N
            self._theta.append(t)
            self._radii.append(self._a * pow(math.e, self._b * t))
            i += 1


class Hyperbolic(Spiral):
    r"""双曲螺线.

    极坐标方程: $r = a/\theta$
    """

    def __init__(self, a: float) -> None:
        """初始化双曲螺线的属性."""
        super().__init__()
        self._a: float = a
        self.f()

    def f(self) -> None:
        """使用极坐标方程计算轴长和转角."""
        N: int = 50
        i: int = 1
        while i < N:
            t: float = i * math.pi / 10
            self._theta.append(t)
            self._radii.append(self._a / t)
            i += 1


class Fermat(Spiral):
    r"""费马螺线.

    极坐标方程: $r^2 = \theta * a^2$
    """

    def __init__(self, a: float) -> None:
        """初始化费马螺线的属性."""
        super().__init__()
        self._a: float = a
        self.f()

    def f(self) -> None:
        """使用极坐标方程计算轴长和转角."""
        N: int = 500
        i: int = 0
        while i < N:
            t: float = i * math.pi / 50
            self._theta.append(t)
            self._radii.append(self._a * math.sqrt(t))
            i += 1


def main() -> None:
    """Entry function."""
    # 类的各种方法测试
    # test_c: ClassTemplate = ClassTemplate(p1=2)
    # print(test_c.instance_method())
    # print(test_c.class_method())
    # print(test_c.static_method())
    # print(ClassTemplate.class_method())
    # print(ClassTemplate.static_method())

    # 通过公共基类减少大量代码重复情况, 子类仅需添加基类不存在的代码(属性、方法的额外实现、新方法)
    # s2 = Student2("Richard", 12, "M", "Math", 1200)
    # s2.tell()
    # del s2
    # t2 = Teacher2("Sam", 36, "F", "Math", 12000)
    # t2.tell()
    # del t2

    # 连续继承
    # cube = Cube(3)
    # print(Cube.__mro__)
    # print(cube.__dict__)
    # print(
    #     f"立方体 cube 的表面积为: {cube.surface_area()}\
    #     \n             体积为: {cube.volume()}",
    # )

    # 多重继承
    # pyramid: RightPyramid = RightPyramid(4, 5)
    # print(RightPyramid.__mro__)
    # print(f"金字塔 pyramid 的表面积为: {pyramid.area()}")
    # print(f"金字塔 pyramid 的表面积为: {pyramid.area2()}")

    # 螺线绘图
    # a: Archimedes = Archimedes(10, 5)
    # a.draw()
    # l: Log = Log(20, 0.1)
    # l.draw()
    # h: Hyperbolic = Hyperbolic(1)
    # h.draw()
    # f: Fermat = Fermat(10)
    # f.draw()


if __name__ == "__main__":
    main()
