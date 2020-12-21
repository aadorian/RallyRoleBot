from discord import Color

from constants import *
import math

def make_color_tuple(color):
    """
    Turn something like "#000000" into 0,0,0 or "#FFFFFF" into "255,255,255"
    """
    R = color[1:3]
    G = color[3:5]
    B = color[5:7]

    R = int(R, 16)
    G = int(G, 16)
    B = int(B, 16)

    return R, G, B


def interpolate_tuple(start_color, final_color, steps, index):
    """
    Take two RGB color sets and mix them over a specified number of steps and index
    """
    R = start_color[0]
    G = start_color[1]
    B = start_color[2]

    target_R = final_color[0]
    target_G = final_color[1]
    target_B = final_color[2]

    Diff_R = target_R - R
    Diff_G = target_G - G
    Diff_B = target_B - B

    iR = R + (Diff_R * index / steps)
    iG = G + (Diff_G * index / steps)
    iB = B + (Diff_B * index / steps)

    color = Color.from_rgb(int(iR), int(iG), int(iB))

    return color


def interpolate_color(start_color, final_color, steps, index):
    """
    Wrapper for interpolate_tuple that accepts colors as html ("#CCCCC" and such)
    """
    start_tuple = make_color_tuple(start_color)
    final_tuple = make_color_tuple(final_color)

    return interpolate_tuple(start_tuple, final_tuple, steps, index)


def get_gradient_by_percentage(start_color, goal_color, steps, percentage):
    """
    Get gradient color calculated by the percentage. Dont use negative values
    """
    if percentage >= 100:
        index = steps
    else:
        index = math.ceil(percentage / (100 / steps))

    return interpolate_color(start_color, goal_color, steps, index)