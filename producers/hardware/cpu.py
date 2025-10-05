import psutil


class CPU:

    def __init__(self):
        ...

    def get_times(self) -> dict:
        times_agg = psutil.cpu_times(percpu=False)
        times_per_cpu = psutil.cpu_times(percpu=True)
        return {
            "agg": times_agg._asdict(),
            "per_cpu": [
                {"cpu_index": idx, **cpu._asdict()}
                for idx, cpu in enumerate(times_per_cpu)
            ]
        }

    def get_times_percent(self) -> dict:
        interval = 0.1
        times_percent_agg = psutil.cpu_times_percent(interval, percpu=False)
        times_percent_per_cpu = psutil.cpu_times_percent(interval, percpu=True)
        return {
            "agg": times_percent_agg._asdict(),
            "per_cpu": [
                {"cpu_index": idx, **cpu._asdict()}
                for idx, cpu in enumerate(times_percent_per_cpu)
            ]
        }

    def get_usage_percent(self) -> dict:
        interval = 0.1
        usage_percent_agg = psutil.cpu_percent(interval, percpu=False)
        usage_percent_per_cpu = psutil.cpu_percent(interval, percpu=True)
        return {
            "agg": usage_percent_agg,
            "per_cpu": [
                {"cpu_index": idx, "usage": cpu_usage}
                for idx, cpu_usage in enumerate(usage_percent_per_cpu)
            ]
        }

    def get_cores(self) -> dict:
        return {
            "physical": psutil.cpu_count(logical=False),
            "logical": psutil.cpu_count(logical=True)
        }

    def get_stats(self) -> dict:
        return psutil.cpu_stats()._asdict()

    def get_frequency(self) -> dict:
        freq_agg = psutil.cpu_freq(percpu=False)
        freq_per_cpu = psutil.cpu_freq(percpu=True)
        return {
            "agg": freq_agg._asdict(),
            "per_cpu": [
                {"cpu_index": idx, **cpu._asdict()}
                for idx, cpu in enumerate(freq_per_cpu)
            ]
        }

    def get_load_avg(self) -> dict:
        load_1, load_5, load_15 = psutil.getloadavg()
        return {
            "load_avg_1_min": load_1,
            "load_avg_5_min": load_5,
            "load_avg_15_min": load_15,
        }

    def get_data(self) -> dict:
        return {
            "times": self.get_times(),
            "times_percent": self.get_times_percent(),
            "usage_percent": self.get_usage_percent(),
            "cores": self.get_cores(),
            "stats": self.get_stats(),
            "frequency": self.get_frequency(),
            "load_avg": self.get_load_avg()
        }