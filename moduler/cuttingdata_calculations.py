
""" This is planned to be a module for cuttingspeed calculations, write once and reuse """

import math
from typing import Tuple


def cuttingdata(cut_speed: float, mill_dia: float, numz: float, feed_per_tooth: float) -> Tuple[float, float]:

    """ Calculating the spindel speed based on given cutting speed and mill diameter
        and feedrate based on the number of teeths on the mill and the feed per tooth"""

    spindel_speed = (cut_speed * 1000) / (math.pi * mill_dia)
    mill_feed = spindel_speed * numz * feed_per_tooth

    return spindel_speed, mill_feed
