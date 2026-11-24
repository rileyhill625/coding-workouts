from tcc import trip_time
import pytest


@pytest.mark.parametrize("current, pickup, td, curve, expected", [
    (2000, 400, 1,   "IEEE High",     1.308),
    (750,  500, 1,   "IEEE Extreme",  22.682),
    (2000, 200, 1,   "IEEE Moderate", 1.207),
    (2000, 400, 2,   "IEEE High",     2.616),
    (2000, 200, 1,   "SEL Moderate",  0.243),
    (2000, 400, 1,   "SEL CO-8",      0.428),
    (2000, 400, 1,   "SEL High",      0.258),
    (1500, 100, 0.5, "SEL CO-8",      0.103),
])


def test_trip_time(current, pickup, td, curve, expected):
    assert trip_time(current, pickup, td, curve) == pytest.approx(expected, abs=1e-3)
    
