


import os
from dagster import get_dagster_logger, job, op

# 获取当前文件夹的大小
@op
def get_file_sizes():
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    return {f: os.path.getsize(f) for f in files}

# 获取文件夹的总大小
@op
def get_total_size(file_sizes):
    return sum(file_sizes.values())

# 计算文件夹大小的最大值
@op
def get_largest_size(file_sizes):
    return max(file_sizes.values())

# 输出一下日志
@op
def report_file_stats(total_size, largest_size):
    # In real life, we'd send an email or Slack message instead of just logging:
    get_dagster_logger().info(f"Total size: {total_size}, largest size: {largest_size}")

# 定义任务
@job
def diamond():
    file_sizes = get_file_sizes()
    report_file_stats(
        total_size=get_total_size(file_sizes),
        largest_size=get_largest_size(file_sizes),
    )
