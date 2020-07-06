"""Process Monitor
Usage:
    processmonitor.py <process_name> <overall_duration> [<sampling_interval>]
    processmonitor.py -h|--help
    processmonitor.py -v|--version

Options:
    <process_name> Process name argument.
    <overall_duration> Overall duration of the monitoring in seconds.
    <sampling_interval> Sampling interval in seconds (optional, default 5).
    -h --help  Show this screen.
    -v --version  Show version.
"""

from docopt import docopt
from process import Process
from threading import Event, Thread
from datetime import datetime
import os
import sys
import csv
import time

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        iteration = 1
        while not stopped.wait(interval - time.time() % interval):
            func(*args, iteration)
            iteration = iteration + 1
    Thread(target=loop).start()    
    return stopped.set

def print_average():
    cpu_avg, mem_avg, files_avg = Process.metrics_average()
    if cpu_avg != None and mem_avg != None and files_avg != None:
        print(f"Metrics Avg.: %CPU: {cpu_avg}, MEMORY(B): {mem_avg}, OPEN FILES: {files_avg}")
        return True
    return False

def generate_report(name, duration, interval):
    if len(Process.metrics) == 0:
        return False
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{ts}_process-metrics-report_{name}_{duration}_{interval}.csv"
    with open(f"{filename}", mode='w') as report:
        writer = csv.writer(report, delimiter=',')
        writer.writerow(['ITERATION', '%CPU', 'MEMORY(B)', 'OPEN FILES'])
        iteration = 1
        for metric in Process.metrics:
            writer.writerow([
                iteration,
                metric.cpu,
                metric.mem,
                metric.files])
            iteration = iteration + 1
    reportpath = f"./{filename}"
    print(f"Metrics report: {reportpath}")
    return True

def raise_memory_leak_warning(name):
    if (Process.has_memory_leaks(name)):
        print(f"WARNING: possible memory leaks detected for process \'{name}\'")
        return True
    return False
        
def main():
    args = docopt(__doc__, version='Process Monitor 1.0')
    if not args['<sampling_interval>']:
        args['<sampling_interval>'] = 5

    name = args['<process_name>']
    duration = int(args['<overall_duration>'])
    interval = int(args['<sampling_interval>'])

    print("---------------------------------------------")
    print("              Process Monitor")
    print("---------------------------------------------")
    print(f"Monitoring process \'{name}\' every {interval} sec for {duration} sec")

    cancel_future_calls = call_repeatedly(interval, Process.monitor, name)
    time.sleep(duration)
    cancel_future_calls()
    print_average()
    generate_report(name, duration, interval)
    raise_memory_leak_warning(name)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    sys.exit(main())
