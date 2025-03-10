# 流浪地球计划在赤道上均匀部署了 N 个转向发动机，按位置顺序编号为 0 ~ N
#
# 初始状态下所有的发动机都是未启动状态
# 发动机启动的方式分为“手动启动”和“关联启动”两种方式
# 如果在时刻 1 一个发动机被启动，下一个时刻 2 与之相邻的两个发动机就会被“关联启动”
# 如果准备启动某个发动机时，它已经被启动了，则什么都不用做
# 发动机 0 与发动机 N-1 是相邻的
# 地球联合政府准备挑选某些发动机在某些时刻进行“手动启动”。当然最终所有的发动机都会被启动。哪些发动机最晚被启动呢？
# 输入描述
# 第一行两个数字 N 和 E，中间有空格
#
# N 代表部署发动机的总个数，1 < N ≤ 1000
# E 代表计划手动启动的发动机总个数，1 ≤ E ≤ 1000，E ≤ N
# 接下来共 E 行，每行都是两个数字 T 和 P，中间有空格
#
# T 代表发动机的手动启动时刻，0 ≤ T ≤ N
# P 代表次发动机的位置编号，0 ≤ P < N
# 输出描述
# 第一行一个数字 N， 以回车结束
#
# N 代表最后被启动的发动机个数
# 第二行 N 个数字，中间有空格，以回车结束
#
# 每个数字代表发动机的位置编号，从小到大排序

if __name__ == '__main__':
    # 发动机的总个数, 计划手动启动的发动机总个数
    n, e = map(int, input().split())

    # 记录每个发动机的最终启动时刻, 初始化为极大值，方便后面取最早启动时刻
    launches = [float('inf')] * n

    for _ in range(e):
        # 发动机的手动启动时刻, 发动机的位置编号
        t, p = map(int, input().split())

        if t > launches[p]:
            continue

        # 手动启动：p号发动机在t时刻手动启动
        launches[p] = t

        for q in range(n):
            innerDis = abs(p - q)  # 内关联距离
            outerDis = n - innerDis  # 外关联距离
            launches[q] = min(launches[q], launches[p] + min(innerDis, outerDis))

    last = []  # 最晚启动的发动机编号集合
    lastTime = -1  # 最晚启动时刻

    for i in range(n):
        if launches[i] > lastTime:
            last.clear()
            lastTime = launches[i]

        if launches[i] == lastTime:
            last.append(i)

    print(len(last))
    print(" ".join(map(str, last)))