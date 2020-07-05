import pytest
import utils

def test_mem_to_octet_T():
    test_input = "1T"
    expected_output = utils.mem_to_octet(test_input)
    assert 1099511627776 == expected_output

def test_mem_to_octet_G():
    test_input = "1G"
    expected_output = utils.mem_to_octet(test_input)
    assert 1073741824 == expected_output

def test_mem_to_octet_M():
    test_input = "1M"
    expected_output = utils.mem_to_octet(test_input)
    assert 1048576 == expected_output

def test_mem_to_octet_K():
    test_input = "1K"
    expected_output = utils.mem_to_octet(test_input)
    assert 1024 == expected_output

def test_mem_to_octet_O():
    test_input = "1"
    expected_output = utils.mem_to_octet(test_input)
    assert 1 == expected_output

def test_mem_to_octet_empty():
    test_input = ""
    expected_output = utils.mem_to_octet(test_input)
    assert None == expected_output

def test_mem_to_octet_negative():
    test_input = "-1"
    expected_output = utils.mem_to_octet(test_input)
    assert None == expected_output

def test_mem_to_octet_alphanum():
    test_input = "123pipo"
    expected_output = utils.mem_to_octet(test_input)
    assert None == expected_output