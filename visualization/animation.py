import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

def animate(history):
    history = history[::2]  # slows down playback
    fps = 30                # good viewing speed
    interval = 1000 / fps   # override real-time to slow it down

    fig, ax = plt.subplots()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    line, = ax.plot([], [], 'o-', lw=2.5)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        x1, y1, x2, y2 = history[i]
        line.set_data([0, x1, x2], [0, y1, y2])
        return line,

    anim = animation.FuncAnimation(
        fig, animate, init_func=init,
        frames=len(history), interval=interval, blit=True
    )

    # Save animation as GIF file
    anim.save('visualization/output/pendulum.gif', writer=PillowWriter(fps=fps))
    plt.show()

