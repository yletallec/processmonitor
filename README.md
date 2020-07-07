# Process Monitor

[![Build Status](https://travis-ci.com/yletallec/processmonitor.svg?branch=master)](https://travis-ci.com/github/yletallec/processmonitor)

Process Monitor is a Python console application collecting metrics for a process and its children.
  - % of CPU used
  - Virtual private memory used
  - Number of open files

From the gathered process metrics, Process Monitor:
  - Outputs the average for each metric
  - Creates a CSV report

Process Monitor also raises a warning in case of memory leaks detection.

## Usage
```
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
```

## Installation

Process Monitor requires macOS 10.14.3+ with command line developer tools.
It requires elevated privileges, leaks utility and docopt library to run.
It requires elevated privileges, pytest, mock, pytest-cov and codecov libraries to test.
```sh
git
```
If missing, typing 'git' in a Terminal will launch command line developer tools installation.
leaks, python3 and pip3 are bundled with command line developer tools.

```sh
➜ which leaks
/usr/bin/leaks
➜ which git
/usr/bin/git
➜ which python3
/usr/bin/python3
➜ which pip3
/usr/bin/pip3
```

```sh
➜ pip3 install -U pip
➜ pip3 install -U pytest
➜ pip3 install mock
➜ pip3 install pytest-cov
➜ pip3 install codecov
➜ pip3 install docopt
➜ mkdir ~/src
➜ cd ~/src
➜ git clone https://github.com/yletallec/processmonitor.git
➜ cd processmonitor
```

## Run tests
```sh
➜ sudo python3 -m pytest --cov=./
```

## Run application
```sh
➜ sudo python3 processmonitor.py Google 15
---------------------------------------------
              Process Monitor
---------------------------------------------
Monitoring process 'Google' every 5 sec for 15 sec
Metrics #1: %CPU: 1.6, MEMORY(B): 435159040, OPEN FILES: 419
Metrics #2: %CPU: 1.3, MEMORY(B): 435159040, OPEN FILES: 421
Metrics #3: %CPU: 1.0, MEMORY(B): 427819008, OPEN FILES: 416
Metrics Avg.: %CPU: 1.3, MEMORY(B): 432712362, OPEN FILES: 418
Metrics report: ./2020-07-08_18-04-30_process-metrics-report_Google_15_5.csv
WARNING: possible memory leaks detected for process 'Google'
```
