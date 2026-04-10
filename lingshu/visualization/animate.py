"""
演化可视化模块
灵枢的"小仙女"之舞
"""

import matplotlib
matplotlib.use('Agg')  # 使用非交互后端，支持无GUI环境
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from core.automaton import LingShuAutomaton

def run_animation(automaton: LingShuAutomaton,
                  frames: int = 500,
                  interval: int = 100,
                  cmap: str = 'coolwarm',
                  save_path: str = None):
    """
    运行动画并显示或保存

    Args:
        automaton: 灵枢自动机实例
        frames: 演化帧数
        interval: 帧间隔(毫秒)
        cmap: 颜色映射
        save_path: 若指定路径则保存为视频文件 (支持 .mp4, .gif)
    """
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.set_title(f"灵枢 · 呼吸 · 第 {automaton.generation} 代", fontsize=14, pad=20)

    # 初始图像
    im = ax.imshow(
        automaton.get_grid_2d(),
        cmap=cmap,
        vmin=-1,
        vmax=1,
        aspect='auto',
        interpolation='nearest'
    )
    ax.set_yticks([])
    ax.set_xlabel('元胞索引', fontsize=10)

    def update(frame):
        automaton.step()
        im.set_data(automaton.get_grid_2d())
        ax.set_title(f"灵枢 · 呼吸 · 第 {automaton.generation} 代", fontsize=14, pad=20)
        return [im]

    ani = animation.FuncAnimation(
        fig, update, frames=frames, interval=interval, blit=True
    )

    plt.tight_layout()

    if save_path:
        print(f"正在保存演化动画到: {save_path}")

        # 根据扩展名选择写入器
        ext = save_path.split('.')[-1].lower()

        if ext in ('mp4', 'avi', 'mov'):
            # 视频格式需要 ffmpeg
            try:
                Writer = animation.writers['ffmpeg']
                writer = Writer(fps=1000//interval, metadata=dict(artist='LingShu'), bitrate=1800)
                ani.save(save_path, writer=writer)
                print(f"✓ 视频保存成功: {save_path}")
            except Exception as e:
                print(f"✗ ffmpeg 不可用，无法保存视频: {e}")
                print("提示：请安装 ffmpeg (sudo apt install ffmpeg) 以支持视频输出")
                print("      或改用 .gif 格式输出")
                return ani
        else:
            # GIF 或其他格式使用 PillowWriter
            try:
                ani.save(save_path, writer='pillow', fps=1000//interval)
                print(f"✓ 动画保存成功: {save_path}")
            except Exception as e2:
                print(f"✗ 保存失败: {e2}")
                return ani
    else:
        plt.show()

    plt.close(fig)
    return ani
