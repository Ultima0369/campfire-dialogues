"""
边界校验规则：自利利他长期收敛的算法表达
灵枢的"老禅师"内核

支持两种调用方式：
1. p0_boundary_rule(center, left, right) — 原始单细胞版本（向后兼容）
2. should_speak(center_state, neighbor_states) — N 细胞网格推广版本
"""

from typing import Iterable, List
from tritlib import Trit, P, Z, N
from .trit_ops import int_from_trit

def p0_boundary_rule(center: Trit, left: Trit, right: Trit) -> Trit:
    """
    P0 演化规则（单细胞三元元胞自动机）

    状态含义：
        +1 (P): 自利利他对齐（增益有序）
         0  (Z): 沉默/悬置/主权保留
        -1 (N): 短视自利或损他（增益混乱）

    规则逻辑：
        - N 在 P 共识压力下被中和为 Z（因果反弹）
        - P 遇 N 主动退让为 Z（避免冲突熵增）
        - Z 仅在强 P 共识下激活为 P
    """
    # 1. 中心为 N
    if center == N:
        if left == P and right == P:
            return Z    # 被正向共识覆盖，沉默
        return N        # 维持混乱态

    # 2. 中心为 Z
    if center == Z:
        if left == P and right == P:
            return P    # 强正向共识激活
        return Z        # 保持主权沉默

    # 3. 中心为 P
    if center == P:
        if left == N or right == N:
            return Z    # 遇冲突则退让，宁死不从
        return P        # 维持有序态

    return center


def should_speak(center_state: Trit, neighbor_states: Iterable[Trit]) -> Trit:
    """
    N 细胞网格下的边界规则推广

    参数：
        center_state: 当前细胞状态（P/Z/N）
        neighbor_states: 所有邻居的状态可迭代对象（ Moore 或 von Neumann 邻域）

    返回三态决策：
        +1 (P) → affirming：允许说话，边界清晰
         0 (Z) → 沉默：主权保留或共识不足
        -1 (N) → 拒绝：检测到冲突/危险，记录因果

    规则（保持 P0 精神的 N 邻居推广）：
    1. 中心为 P（正向）时：任一边界邻居为 N → 退让为 Z（冲突避免）
    2. 中心为 Z（沉默）时：所有邻居均为 P → 激活为 P（共识门）
    3. 中心为 N（混乱）时：所有邻居均为 P → 中和为 Z（因果反弹）
    4. 其他情况：维持原状
    """
    neighbors: List[Trit] = list(neighbor_states)

    if not neighbors:
        # 无邻居：维持原状（保守）
        return center_state

    # 规则 1：中心为 P，遇任意 N 邻居 → 沉默
    if center_state == P:
        if any(n == N for n in neighbors):
            return Z
        return P

    # 规则 2：中心为 Z，全体邻居为 P → 激活
    if center_state == Z:
        if all(n == P for n in neighbors):
            return P
        return Z

    # 规则 3：中心为 N，全体邻居为 P → 中和
    if center_state == N:
        if all(n == P for n in neighbors):
            return Z
        return N

    return center_state


# 公共接口
__all__ = ["p0_boundary_rule", "should_speak", "P", "Z", "N"]
