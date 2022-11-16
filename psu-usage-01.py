import psutil
network_stats = psutil.net_io_counters(pernic=True)
bytes_sent = getattr(network_stats, 'bytes_sent')
print(bytes_sent)
bytes_recv = getattr(network_stats, 'bytes_Recv')
print(bytes_recv)
print("Bytes send = {0} | Bytes recv = {1}".format(bytes_sent,bytes_recv))