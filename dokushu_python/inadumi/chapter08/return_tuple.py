import collections

def group_func(*args):
    Group = collections.namedtuple("Group", ["sum_v", "avg_v", "max_v", "min_v", "count_v"])
    return Group(sum(args), sum(args)/len(args), max(args), min(args), len(args))

result = group_func(8, 3, -3, 12, 9, 1, 4, 7, -2, 5)
print(f"合計: {result.sum_v} 平均: {result.avg_v} 最大: {result.max_v} 最小: {result.min_v} 件数: {result.count_v}")
