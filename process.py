import subprocess
import utils
from dataclasses import dataclass

class Process:

    @dataclass
    class Metric:
        cpu: float
        mem: int
        files: int

    metrics = []

    @staticmethod
    def metrics_average():
        size = len(Process.metrics)
        if size == 0:
            return None, None, None
        cpu_avg = round(sum(metric.cpu for metric in Process.metrics) / size, 1)
        mem_avg = int(sum(metric.mem for metric in Process.metrics) / size)
        files_avg = int(sum(metric.files for metric in Process.metrics) / size)
        return cpu_avg, mem_avg, files_avg

    @staticmethod
    def monitor(name, iteration):
        if Process.exists(name):
            cpu = Process.get_cpu_usage(name)
            mem = Process.get_private_memory_usage(name)
            files = Process.get_number_of_open_files(name)
            Process.metrics.append(Process.Metric(cpu,mem,files))
            print(f"Metrics #{iteration}: %CPU: {cpu}, MEMORY(B): {mem}, OPEN FILES: {files}")
            return True
        else:
            print(f"process \'{name}\' unknown")
            return False

    @staticmethod
    def exists(name):
        cmd = f"pgrep {name}"
        rc = subprocess.call(
                cmd,
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT)
        return rc == 0

    @staticmethod
    def get_cpu_usage(name):
        try:
            cmd = f"ps -p \"$(pgrep -d, -f {name})\" -o %cpu"
            output = subprocess.check_output(
                        cmd,
                        shell=True)
        except:
            return None
        values = output.decode('utf-8').strip().split('\n')[1:]
        return round(sum(float(val.replace(',','.')) for val in values), 1)

    @staticmethod
    def get_private_memory_usage(name):
        try:
            cmd = f"top -l 1 -s 0 -stats command,mem | grep {name}"
            output = subprocess.check_output(
                        cmd,
                        shell=True)
        except:
            return None
        rows = output.decode('utf-8').strip().split('\n')
        values = [row[row.strip().rfind(' '):].strip().rstrip('+') for row in rows]
        return sum(utils.mem_to_octet(val) for val in values)

    @staticmethod
    def get_number_of_open_files(name):
        cmd = f"lsof -c {name} | wc -l"
        output = subprocess.check_output(
                    cmd,
                    shell=True)
        val = int(output.decode('utf-8').strip())
        return val - 1 if val > 0 else 0

    @staticmethod
    def has_memory_leaks(name):
        pids = Process.get_pids(name)
        for pid in pids:
            cmd = f"sudo leaks {pid}"
            rc = subprocess.call(
                    cmd,
                    shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
            # EXIT STATUS:
            #  0     No leaks were detected.
            #  1     One or more leaks were detected.
            #  >1    An error occurred.
            if rc == 1:
                return True
        return False

    @staticmethod
    def get_pids(name):
        try:
            cmd = f"pgrep {name}"
            output = subprocess.check_output(
                        cmd,
                        shell=True)
        except:
            return []
        return output.decode('utf-8').strip().split('\n')
