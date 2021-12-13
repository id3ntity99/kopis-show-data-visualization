import mpld3
import matplotlib.pyplot as plt
import numpy as np


def create_double_bars(x_label, y_label, x_ticks, **y_vals):
    arg_key_list = list(y_vals.keys())
    arg_val_list = list(y_vals.values())
    # arg_len = len(y_vals.keys())
    x = np.arange(len(x_ticks))
    bar_val_1 = list(map(float, arg_val_list[0]))
    bar_val_2 = list(map(float, arg_val_list[1]))

    distance = 0.15
    width = 0.1

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - distance/2, bar_val_1, width, label=arg_key_list[0])
    rects2 = ax.bar(
            x + distance/2, bar_val_2, width,
            label=arg_key_list[1]
    )

    # labeling and add ticks
    ax.bar_label(rects1, padding=7)
    ax.bar_label(rects2, padding=3)
    ax.set_ylabel("Amounts")
    ax.set_title("Genre Statistic")
    ax.set_xticks(x)
    ax.set_xticklabels(x_ticks, rotation=45)
    ax.legend()
    fig.tight_layout()

    return mpld3.fig_to_html(fig)


def create_double_line(x_labels, y_labels, x_ticks, **y_vals):
    arg_key_list = list(y_vals.keys())
    arg_val_list = list(y_vals.values())
    ln_val_1 = list(map(float, arg_val_list[0]))
    ln_val_2 = list(map(float, arg_val_list[1]))

    fig = plt.figure()
    gs = fig.add_gridspec(2, hspace=0)
    ax = gs.subplots(sharex=True, sharey=False)
    ax[0].plot(x_ticks, ln_val_1, 'tab:orange', label=arg_key_list[0])
    ax[1].plot(x_ticks, ln_val_2, label=arg_key_list[1])

    ax[0].legend()
    ax[1].legend()
    fig.tight_layout()

    plt.show()
    return mpld3.fig_to_html(fig)
