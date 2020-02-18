import pytest
from moduler import cuttingdata_calculations


def test_cuttingdata():
    result = cuttingdata_calculations.cuttingdata(210.0, 80.0, 6, 0.12)
    spindel_rpm = round(result[0], 0)
    feedrate = round(result[1], 0)

    assert spindel_rpm == 836
    assert feedrate == 602


def test_helixangle():

    assert round(cuttingdata_calculations.helix_angle(40, 20, 1), 2) == 0.91
    assert round(cuttingdata_calculations.helix_angle(20, 40, 1), 2) == -0.91


def test_materialremoval():

    assert cuttingdata_calculations.material_removal(2, 60, 602) == 72.24
    assert cuttingdata_calculations.material_removal(1, 60, 602) == 36.12


def test_ra():

    assert round(cuttingdata_calculations.ra(0.2, 0.8), 2) == 2.08
    assert round(cuttingdata_calculations.ra(0.1, 0.8), 2) == 0.52
