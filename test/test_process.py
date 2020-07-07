import pytest
from process import Process

def test_process_metrics_average_empty(empty_process_metrics):
    empty_process_metrics
    assert Process.metrics_average() == (None, None, None)

def test_process_metrics_average_filled(fill_process_metrics):
    fill_process_metrics
    cpu_avg, mem_avg, files_avg = Process.metrics_average()
    assert cpu_avg == 0.2 and mem_avg == 2048 and files_avg == 2

def test_process_monitor_ok(running_process_name):
    assert Process.monitor(running_process_name, 0) == True

def test_process_monitor_nok(unknown_process_name):
    assert Process.monitor(unknown_process_name, 0) == False

def test_process_exists_ok(running_process_name):
    assert Process.exists(running_process_name) == True

def test_process_exists_nok(unknown_process_name):
    assert Process.exists(unknown_process_name) == False

def test_process_get_cpu_usage_ok(running_process_name, is_positive_or_0_float):
    val = Process.get_cpu_usage(running_process_name)
    assert is_positive_or_0_float(val) == True

def test_process_get_cpu_usage_nok(unknown_process_name):
    assert Process.get_cpu_usage(unknown_process_name) == None

def test_process_get_private_memory_usage_ok(running_process_name, is_positive_integer):
    val = Process.get_private_memory_usage(running_process_name)
    assert is_positive_integer(val) == True

def test_process_get_private_memory_usage_nok(unknown_process_name):
    assert Process.get_private_memory_usage(unknown_process_name) == None

def test_process_get_number_of_open_files_ok(running_process_name, is_positive_integer):
    val = Process.get_number_of_open_files(running_process_name)
    assert is_positive_integer(val) == True

def test_process_get_number_of_open_files_nok(unknown_process_name):
    assert Process.get_number_of_open_files(unknown_process_name) == 0

def test_process_get_pids_ok(running_process_name):
    pids = Process.get_pids(running_process_name)
    assert len(pids) > 0

def test_process_get_pids_nok(unknown_process_name):
    assert Process.get_pids(unknown_process_name) == []

def test_leaky_process_has_memory_leaks(leaky_process_name):
    assert Process.has_memory_leaks(leaky_process_name) == True

def test_memorytight_process_has_no_memory_leaks(memorytight_process_name):
    assert Process.has_memory_leaks(memorytight_process_name) == False

def test_unknown_process_has_no_memory_leaks(unknown_process_name):
    assert Process.has_memory_leaks(unknown_process_name) == False
