
""" This is planned to be a module for cuttingspeed calculations, write once and reuse """

import math


def spindel_rpm(cutting_speed: float = 1, mill_dia: float = 1) -> float:

    """ Calculating the spindel speed based on given cutting speed and mill diameter """

    return (cutting_speed * 1000) / (math.pi * mill_dia)


def feedrate(spindel_rpm: float, num_of_teeth: int, feed_per_tooth: float) -> float:

    """ Feedrate calculations for the mill """

    return spindel_rpm * num_of_teeth * feed_per_tooth
