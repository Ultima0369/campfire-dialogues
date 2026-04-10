"""
三进制操作封装
灵枢的"心跳"基础
"""

from tritlib import Trit, P, Z, N

# 状态映射：三进制 -> 整数 (便于 numpy 可视化)
TRIT_TO_INT = {P: 1, Z: 0, N: -1}
INT_TO_TRIT = {1: P, 0: Z, -1: N}

def trit_from_int(i: int) -> Trit:
    """从整数 -1, 0, 1 构造 Trit"""
    if i not in INT_TO_TRIT:
        raise ValueError("灵枢只接受 -1, 0, 1")
    return INT_TO_TRIT[i]

def int_from_trit(t: Trit) -> int:
    """Trit 转整数"""
    return TRIT_TO_INT[t]

def consensus_gate(a: Trit, b: Trit, c: Trit) -> Trit:
    """
    三进制共识门：多数表决
    若 +1 占优返回 +1，-1 占优返回 -1，否则返回 0
    这是灵枢处理 L3 共识的基本运算
    """
    vals = [int_from_trit(x) for x in (a, b, c)]
    s = sum(vals)
    if s > 1:
        return P
    elif s < -1:
        return N
    else:
        return Z
