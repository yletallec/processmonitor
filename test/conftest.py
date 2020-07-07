import pytest
from process import Process

@pytest.fixture
def args_ok(running_process_name):
    return ['', running_process_name, '2', '1']

@pytest.fixture
def args_string_duration(running_process_name):
    return ['', running_process_name, 'string']

@pytest.fixture
def args_float_duration(running_process_name):
    return ['', running_process_name, '2.2']

@pytest.fixture
def args_string_interval(running_process_name):
    return ['', running_process_name, '2', 'string']

@pytest.fixture
def args_float_interval(running_process_name):
    return ['', running_process_name, '2', '1.1']

@pytest.fixture
def args_interval_gt_duration(running_process_name):
    return ['', running_process_name, '1', '2']

@pytest.fixture
def running_process_name():
    return "distnoted"

@pytest.fixture
def unknown_process_name():
    return "unknown_process"

@pytest.fixture
def leaky_process_name():
    return "UserEventAgent"

@pytest.fixture
def memorytight_process_name():
    return "distnoted"

@pytest.fixture
def empty_process_metrics():
    Process.metrics = []

@pytest.fixture
def fill_process_metrics():
    Process.metrics = []
    Process.metrics.append(Process.Metric(0.1,1024,1))
    Process.metrics.append(Process.Metric(0.3,3072,3))

@pytest.fixture
def is_positive_or_0_float():
    def _is_positive_or_0_float(val):
        try:
            val = float(val)
            if val >= 0:
                return True
        except ValueError:
            return False
        return False

    return _is_positive_or_0_float

@pytest.fixture
def is_positive_integer():
    def _is_positive_integer(val):
        try:
            val = float(val)
            if val.is_integer() and val > 0:
                return True
        except ValueError:
            return False
        return False

    return _is_positive_integer
