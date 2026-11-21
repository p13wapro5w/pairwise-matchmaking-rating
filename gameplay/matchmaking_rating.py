import math

def mmr(rating):
    """统一 MMR。"""
    raise NotImplementedError("TODO: mmr")

def latency(ping, limit):
    """延迟阈值。"""
    raise NotImplementedError("TODO: latency")

def team_max(ratings):
    """按最高分。"""
    raise NotImplementedError("TODO: team_max")

def placement(is_new):
    """定级隔离。"""
    raise NotImplementedError("TODO: placement")

def k(base, streak):
    """动态 K 值。"""
    raise NotImplementedError("TODO: k")

def region(name):
    """地域分区。"""
    raise NotImplementedError("TODO: region")

def widen(base, wait, max_w):
    """放宽有上限。"""
    raise NotImplementedError("TODO: widen")

def party(size):
    """组队限制。"""
    raise NotImplementedError("TODO: party")

def soft(rating):
    """软重置。"""
    raise NotImplementedError("TODO: soft")

def dedupe(ids):
    """入队去重。"""
    raise NotImplementedError("TODO: dedupe")

def clamp(rating):
    """分数钳制。"""
    raise NotImplementedError("TODO: clamp")

def avg(ratings):
    """队伍平均。"""
    raise NotImplementedError("TODO: avg")

def placed(games):
    """定级完成。"""
    raise NotImplementedError("TODO: placed")

def key(team_id):
    """队伍键。"""
    raise NotImplementedError("TODO: key")

def tolerance(gap):
    """分差。"""
    raise NotImplementedError("TODO: tolerance")
