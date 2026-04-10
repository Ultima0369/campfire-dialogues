#!/usr/bin/env python3

"""
灵枢 · 初息
P0 阶段启动脚本

运行此脚本，观测三进制元胞自动机的第一次呼吸。

"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.automaton import LingShuAutomaton
from visualization.animate import run_animation

def main():
    print("=" * 50)
    print("灵枢 · LingShu")
    print("自利利他长期收敛 · 三进制边界校验")
    print("=" * 50)

    # 创建一个 100 元胞的环
    size = 100

    # 自定义初始状态 (可选)
    # 例如：中央放一个 +1，两侧放 -1，观察冲突演化
    initial = [0] * size
    initial[size//2] = 1
    initial[size//2 - 2] = -1
    initial[size//2 + 2] = -1

    print(f"\n元胞数量: {size}")
    print("初始状态: 中央 +1，两侧 -1，其余 0")
    print("\n启动演化...\n")

    automaton = LingShuAutomaton(size=size, initial_state=initial)

    # 运行动画并保存为GIF文件（无GUI环境）
    output_path = "lingshu_first_breath.gif"
    run_animation(automaton, frames=300, interval=100, save_path=output_path)

    print("\n演化结束。灵枢已呼吸 300 次。")

if __name__ == "__main__":
    main()
