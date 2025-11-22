def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

next(filter(lambda n: n > 2025, gen_fib())) 

def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    try:
        prev = next(t)
        while True:
            curr = next(t)
            yield curr - prev
            prev = curr
    except StopIteration:
        pass

#print(list(differences(iter([5, 2, -100, 103]))))


def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m."""
    assert n >= 0 and m >= 0
    # 基本情况：正好凑成 n
    if n == 0:
        yield ''   # 表示已经完成划分，空字符串作为后续拼接的基底
        return
    # 如果没有可用的部件且 n > 0，则无解（什么也不 yield）
    if m == 0:
        return

    # 1) 不使用 m，尝试用更小的部件
    for p in partition_gen(n, m - 1):
        yield p

    # 2) 使用 m（前提 n >= m），继续拆剩余的 n-m（仍允许使用 m）
    if n >= m:
        for p in partition_gen(n - m, m):
            if p:               # 子划分非空，前面加上 "m + "
                yield f"{m} + {p}"
            else:               # 子划分是空字符串，说明这是最后一个元素
                yield str(m)

for partition in sorted(partition_gen(6, 4)):
    print(partition)