from configs.config import *
import re

def create_gradient(start_color, end_color, num_steps):
    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    return colors

def CenterMultilineText(text,line_len):
    out = r""
    for a in text.split("\n"):
        out += a.center(line_len)+"\n"
    return out



def UnStyleText(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

def StyleText(
    text, use_character_set=False, character_set="\\┴┼┘┤└┐─┬├┌└│]░▒░▒█▓▄▌▀()[].-"
):
    text = UnStyleText(text)
    colors = create_gradient(accent_color_a, accent_color_b, 15)
    colors += list(reversed(colors[:-1]))
    # gradient color list

    def get_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    lines = text.split("\n")
    num_colors = len(colors)

    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not char.startswith("\x1b"):
                if use_character_set:
                    if char in character_set:
                        color_index = (i + j) % num_colors
                        color = colors[color_index]
                        result.append(get_color(*color) + char + "\033[0m")
                    else:
                        result.append(char)
                else:
                    color_index = (i + j) % num_colors
                    color = colors[color_index]
                    result.append(get_color(*color) + char + "\033[0m")

        if i < len(lines) - 1:
            result.append("\n")
    return "".join(result)
