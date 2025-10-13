import psutil


class Disk:

    def __init__(self):
        ...

    def get_io_counters(self):
        return {
            "agg": psutil.disk_io_counters(perdisk=False, nowrap=True)._asdict(),
            "per_disk": [
                {disk_name: stats._asdict()} 
                for disk_name, stats in psutil.disk_io_counters(perdisk=True, nowrap=True).items()
            ]
        }     

    def get_partition_and_usage(self):
        return [
            {
                **partition._asdict(),
                **{f"usage_{key}": value 
                  for key, value in psutil.disk_usage(partition.mountpoint)._asdict().items()}
            }
            for partition in psutil.disk_partitions(all=True)
            if partition is not None
        ]