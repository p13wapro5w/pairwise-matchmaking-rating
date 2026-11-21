import pytest
import math
from gameplay import matchmaking_rating as mod

CASES = [
    ("mmr", 'm.mmr(1500) == 1500'),
    ("latency", 'm.latency(50, 100) is True'),
    ("team", 'm.team_max([1200, 1800]) == 1800'),
    ("placement", 'm.placement(True) is True'),
    ("k", 'm.k(16, 3) == 19'),
    ("region", 'm.region("cn") == "cn"'),
    ("widen", 'm.widen(50, 3, 100) == 80'),
    ("party", 'm.party(5) == 1'),
    ("soft", 'm.soft(1000) == 800'),
    ("dedupe", 'm.dedupe([2, 1, 2]) == [1, 2]'),
    ("clamp", 'm.clamp(-10) == 0'),
    ("avg", 'm.avg([1000, 2000]) == 1500'),
    ("placed", 'm.placed(5) is True'),
    ("key", 'm.key(1) == "t:1"'),
    ("tol", 'm.tolerance(100) == 100')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
