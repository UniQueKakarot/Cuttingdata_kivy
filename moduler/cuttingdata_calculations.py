
""" This is planned to be a module for cuttingspeed calculations, write once and reuse """

import math
from typing import Tuple


def cuttingdata(cut_speed: float, mill_dia: float, numz: float, feed_per_tooth: float) -> Tuple[float, float]:

    """ Calculating the spindel speed based on given cutting speed and mill diameter
        and feedrate based on the number of teeths on the mill and the feed per tooth"""

    try:
        spindel_speed = (cut_speed * 1000) / (math.pi * mill_dia)
        mill_feed = spindel_speed * numz * feed_per_tooth
    except:
        spindel_speed = "Error"
        mill_feed = "Error"

    return spindel_speed, mill_feed


def helix_angle(hole_dia: float, mill_dia: float, zstep: float) -> float:

    """ Calculating the ramping angle of the toolpath """

    circumference = (hole_dia - mill_dia) * 3.14

    try:
        result = math.degrees((math.sin(1.57079633) * zstep) / ((hole_dia - mill_dia) * 3.14))
    except:
        result = "Error"

    return result


def material_removal(cut_depth: float, cut_width: float, feedrate: float) -> float:

    """ Calculates the amount of material beeing removed in cubic centimeters """
    try:
        result = (cut_depth * cut_width * feedrate) / 1000
    except:
        result = "Error"

    return result


def ra(feedrate: float, nose_radius: float) -> float:

    """ Calculates an estimate of the finished surface roughness """
    try:
        result = ((feedrate ** 2) / (nose_radius * 24)) * 1000
    except:
        result = "Error"

    return result


def fz_with_round_edge(insert_dia: float, hex_value: float, cut_depth: float) -> float:

    """ Calculate feed per tooth to get a constant hex with round cutting edge """
    try:
        result = (hex_value * insert_dia) / (2 * math.sqrt(cut_depth * insert_dia - cut_depth**2))
    except:
        result = "Error"

    return result
