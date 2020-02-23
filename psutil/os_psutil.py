#!/usr/bin/python3.8
# encoding:utf-8
# pip install psutil

import psutil

### https://www.liaoxuefeng.com/wiki/1016959663602400/1183565811281984


psutil.cpu_count() # CPU逻辑数量
psutil.cpu_count(logical=False) # CPU物理核心

#统计CPU的用户／系统／空闲时间：
psutil.cpu_times()
#scputimes(user=10963.31, nice=0.0, system=5138.67, idle=356102.45)

#获取物理内存和交换内存信息
psutil.virtual_memory()
#svmem(total=8589934592, available=2866520064, percent=66.6, used=7201386496, free=216178688, active=3342192640, inactive=2650341376, wired=1208852480)
psutil.swap_memory()
#sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)

psutil.disk_partitions() # 磁盘分区信息
psutil.disk_usage('/') # 磁盘使用情况
psutil.disk_io_counters() # 磁盘IO


print( psutil.cpu_times() )
