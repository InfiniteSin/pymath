"""《Python玩转数学问题》Chapter 6 类和面向对象编程."""

from math import isclose, pi, sin
from typing import Callable  # noqa: UP035

from scipy.constants import G


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


class SchoolMember2:
    """School member base class."""

    __member_num: int = 0

    def __init__(self, name: str, age: int, gender: str) -> None:
        """Init attributes."""
        # 将所有属性设为私有属性, 对外部修改封闭
        self.name: str = name
        self.age: int = age
        self.gender: str = gender
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
        print(f"----{self.name}----")
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
        self.__name: str = self.name
        self.__age: int = self.age
        self.__gender: str = self.gender
        self.__salary: float = float(salary)
        self.__course: list[str] = []
        if isinstance(course, list):
            self.__course.extend(course)
        else:
            self.__course.append(course)
        print(f"Teacher {self.__name} is registered.")

    def __del__(self) -> None:
        """Trigger when delete instance."""
        super().__del__()
        print(f"Teacher {self.__name} is unregistered.")

    def teaching(self) -> None:
        """Represent all cources the teacher is teaching."""
        print(f"Teacher {self.__name} is teaching {', '.join(self.__course)}")


class Student2(SchoolMember2):
    """Student but subclass of SchoolMember2."""

    def __init__(self, name: str, age: int, gender: str, course: list[str] | str, tuition: float) -> None:
        """Init student attributes.

        Init super class's attributes use super()
        Init extra attributes.
        """
        super().__init__(name, age, gender)  # 通过 super() 继承基类的属性
        self.__name: str = self.name
        self.__age: int = self.age
        self.__gender: str = self.gender
        self.__tuition: float = float(tuition)
        self.__course: list[str] = []
        if isinstance(course, list):
            self.__course.extend(course)
        else:
            self.__course.append(course)
        self.__credit: int = 0
        print(f"Student {self.__name} is registered.")

    def __del__(self) -> None:
        """Trigger when delete instance."""
        super().__del__()
        print(f"Student {self.__name} is unregistered.")

    def get_credit(self, credit: int) -> None:
        """Set credit."""
        self.__credit += credit
        print(f"Student {self.__name} has just got {credit} points of credits.")


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
    s2 = Student2("Richard", 12, "M", "Math", 1200)
    s2.tell()
    del s2
    t2 = Teacher2("Sam", 36, "F", "Math", 12000)
    t2.tell()
    del t2


if __name__ == "__main__":
    main()
