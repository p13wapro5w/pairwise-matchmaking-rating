import math

def mmr(rating):
    """统一 MMR：段位与匹配共用同一套分数。"""
    return rating

def latency(ping, limit):
    """延迟阈值：ping 不超过上限才允许入池。"""
    return ping <= limit

def team_max(ratings):
    """按最高分：队伍匹配分取队内最高，防止高分带新号压局。"""
    return max(ratings)

def placement(is_new):
    """定级隔离：新号在定级池内匹配。"""
    return bool(is_new)

def k(base, streak):
    """动态 K 值：连胜/连败加大浮动。"""
    return base + streak

def region(name):
    """地域分区：按区分池，不跨区合并。"""
    return name

def widen(base, wait, max_w):
    """放宽有上限：随等待每档放宽，但不超过 max_w。"""
    return min(base + wait * 10, max_w)

def party(size):
    """组队限制：满编五排按更严的跨度限制。"""
    return 1 if size >= 5 else 2

def soft(rating):
    """软重置：向基准分收敛一半，而不是归零。"""
    return (rating + 600) / 2

def dedupe(ids):
    """入队去重：同一玩家只入队一次。"""
    return sorted(set(ids))

def clamp(rating):
    """分数钳制：不为负。"""
    return max(0, rating)

def avg(ratings):
    """队伍平均。"""
    return sum(ratings) / len(ratings)

def placed(games):
    """定级完成：打满 5 把定级赛。"""
    return games >= 5

def key(team_id):
    """队伍键。"""
    return f"t:{team_id}"

def tolerance(gap):
    """分差。"""
    return abs(gap)
