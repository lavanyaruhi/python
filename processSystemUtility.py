import psutil
result1=psutil.cpu_times()
result2=psutil.cpu_stats()
result3=psutil.cpu_freq()
result4=psutil.disk_partitions()
result5=psutil.net_io_counters(pernic=True)
print(result1)  #scputimes(user=48511.234375, system=81686.421875, idle=4816366.34375, interrupt=1097.28125, dpc=1987.84375)

print(result2) #scpustats(ctx_switches=3499381340, interrupts=693371494, soft_interrupts=0, syscalls=703091092)

print(result3)
 #scpufreq(current=2300.0, min=0.0, max=2300.0)
print(result4)
#[sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260), sdiskpart(device='D:\\', mountpoint='D
#:\\', fstype='', opts='cdrom', maxfile=255, maxpath=260)]

print(result5)
#{'Ethernet0': snetio(bytes_sent=79677237, bytes_recv=324691722, packets_sent=288896, packets_recv=1833717, errin=0, errout=0, dropin=0, dropou
#t=0),
#'VirtualBox Host-Only Network': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
#'VMware Network Adapter VMnet1': snetio(bytes_sent=19419, bytes_recv=750, packets_sent=19419, packets_recv=750, errin=0, errout=0, dropin=
#0, dropout=0),
#'VMware Network Adapter VMnet8': snetio(bytes_sent=64298, bytes_recv=2001, packets_sent=64298, packets_recv=2001, errin=0, erro
#ut=0, dropin=0, dropout=0),
#'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=
# 0, dropin=0, dropout=0)}

