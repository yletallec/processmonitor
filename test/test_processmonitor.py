import processmonitor
import pytest
import mock

def test_init():
  with mock.patch.object(processmonitor, "main", return_value=0):
    with mock.patch.object(processmonitor, "__name__", "__main__"):
      with mock.patch.object(processmonitor.sys, 'exit') as mock_exit:
         processmonitor.init()
         assert mock_exit.call_args[0][0] == 0

def test_main_ok(args_ok):
    with mock.patch.object(processmonitor.sys, 'argv', args_ok):
        res = processmonitor.main()
        assert res == processmonitor.ExitStatus.OK

def test_main_string_duration(args_string_duration):
    with mock.patch.object(processmonitor.sys, 'argv', args_string_duration):
        res = processmonitor.main()
        assert res == processmonitor.ExitStatus.BAD_DURATION

def test_main_float_duration(args_float_duration):
    with mock.patch.object(processmonitor.sys, 'argv', args_float_duration):
        res = processmonitor.main()
        assert res == processmonitor.ExitStatus.BAD_DURATION

def test_main_string_interval(args_string_interval):
    with mock.patch.object(processmonitor.sys, 'argv', args_string_interval):
        res = processmonitor.main()
        assert res == processmonitor.ExitStatus.BAD_INTERVAL

def test_main_float_interval(args_float_interval):
    with mock.patch.object(processmonitor.sys, 'argv', args_float_interval):
        res = processmonitor.main()
        assert res == processmonitor.ExitStatus.BAD_INTERVAL

def test_main_interval_gt_duration(args_interval_gt_duration):
    with mock.patch.object(processmonitor.sys, 'argv', args_interval_gt_duration):
        res = processmonitor.main()
        assert res == processmonitor.ExitStatus.INTERVAL_GT_DURATION

def test_processmonitor_print_average_ok(fill_process_metrics):
    fill_process_metrics
    assert processmonitor.print_average() == True

def test_processmonitor_print_average_nok(empty_process_metrics):
    empty_process_metrics
    assert processmonitor.print_average() == False

def test_processmonitor_generate_report_ok(fill_process_metrics, running_process_name):
    fill_process_metrics
    assert processmonitor.generate_report(running_process_name, 2, 1) == True

def test_processmonitor_generate_report_nok(empty_process_metrics, running_process_name):
    empty_process_metrics
    assert processmonitor.generate_report(running_process_name, 2, 1) == False

def test_processmonitor_raise_memory_leak_warning_ok(leaky_process_name):
    assert processmonitor.raise_memory_leak_warning(leaky_process_name) == True

def test_processmonitor_raise_memory_leak_warning_nok(memorytight_process_name):
    assert processmonitor.raise_memory_leak_warning(memorytight_process_name) == False
