"""
一维三进制元胞自动机引擎
灵枢的"呼吸"循环
"""

from typing import List
from tritlib import Trit
from .trit_ops import trit_from_int, int_from_trit
from .boundary import p0_boundary_rule

class LingShuAutomaton:
    """
    灵枢元胞自动机

    属性:
        size: 元胞数量
        grid: 当前三进制状态列表
        generation: 演化代数
    """

    def __init__(self, size: int = 100, initial_state: List[int] = None):
        self.size = size
        self.generation = 0

        if initial_state is None:
            # 默认：80% 0，10% +1，10% -1
            import random
            initial_state = random.choices(
                [1, 0, -1],
                weights=[0.1, 0.8, 0.1],
                k=size
            )

        if len(initial_state) != size:
            raise ValueError("初始状态长度必须等于 size")

        self.grid = [trit_from_int(v) for v in initial_state]

    def step(self) -> None:
        """演化一步"""
        new_grid = []
        for i in range(self.size):
            left = self.grid[(i - 1) % self.size]
            center = self.grid[i]
            right = self.grid[(i + 1) % self.size]
            new_grid.append(p0_boundary_rule(center, left, right))

        self.grid = new_grid
        self.generation += 1

    def get_int_grid(self) -> List[int]:
        """返回整数形式的状态列表 (用于可视化)"""
        return [int_from_trit(t) for t in self.grid]

    def get_grid_2d(self) -> List[List[int]]:
        """返回二维形式 (单行) 用于 imshow"""
        return [self.get_int_grid()]
