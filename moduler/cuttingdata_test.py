import pytest
import cuttingdata_calculations


def test_cuttingdata():
    result = cuttingdata_calculations.cuttingdata(210.0, 80.0, 6, 0.12)
    spindel_rpm = round(result[0], 0)
    feedrate = round(result[1], 0)

    assert spindel_rpm == 836
    assert feedrate == 602


def test_helixangle():

    assert round(cuttingdata_calculations.helix_angle(40, 20, 1), 2) == 0.91
    assert round(cuttingdata_calculations.helix_angle(20, 40, 1), 2) == -0.91



