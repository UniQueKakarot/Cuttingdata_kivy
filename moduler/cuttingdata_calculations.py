
""" This is planned to be a module for cuttingspeed calculations, write once and reuse """

import math


def spindel_speed(cutting_speed: float, mill_dia: float) -> float:

    """ Calculating the spindel speed based on given cutting speed and mill diameter """

    return (cutting_speed * 1000) / (math.pi * mill_dia)
