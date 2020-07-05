# Process Monitor

[![Build Status](https://travis-ci.org/yletallec/processmonitor.svg?branch=master)](https://travis-ci.org/yletallec/processmonitor)

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

Process Monitor requires macOS with leaks utility, Python 3.7+ and docopt library to run.
```sh
git
```

![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRzAr6lzIqjmW0w9fs-udxLHuobDHAB1W7RiQ&usqp=CAU)

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
➜ sudo pip3 install docopt
➜ mkdir ~/src
➜ cd ~/src
➜ git clone https://github.com/yletallec/processmonitor.git
```