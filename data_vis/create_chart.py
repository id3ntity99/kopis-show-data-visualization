import pygal
from pygal.style import Style


def create_double_bars(x_label, y_label, x_ticks, **y_vals):
    custom_style = Style(
        background="#FFFFFF",
        plot_background="#FFFFFF",
        colors=("#E853A0", "#E87653"),
    )

    arg_key_list = list(y_vals.keys())
    arg_val_list = list(y_vals.values())
    bar_val_1 = list(map(float, arg_val_list[0]))
    bar_val_2 = list(map(float, arg_val_list[1]))

    bar_chart = pygal.Bar(style=custom_style)

    bar_chart.x_labels = map(str, x_ticks)
    bar_chart.add(arg_key_list[0], bar_val_1)
    bar_chart.add(arg_key_list[1], bar_val_2)
    svg_byte = bar_chart.render()
    bar_chart.render_to_file("./double_bars.svg")
    return svg_byte


def create_double_line(x_labels, y_labels, x_ticks, **y_vals):
    custom_style = Style(
        background="#FFFFFF",
        plot_background="#FFFFFF",
        colors=("#E853A0", "#E87653"),
    )

    arg_key_list = list(y_vals.keys())
    arg_val_list = list(y_vals.values())
    ln_val_1 = list(map(float, arg_val_list[0]))
    ln_val_2 = list(map(float, arg_val_list[1]))

    line_chart = pygal.Line(style=custom_style)
    line_chart.x_labels = map(str, x_ticks)
    line_chart.add(arg_key_list[0], ln_val_1)
    line_chart.add(arg_key_list[1], ln_val_2)
    svg_byte = line_chart.render()
    line_chart.render_to_file("./double_lines.svg")
    return svg_byte
