#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

def test_input_text(expected, actual):
    assert actual == expected, f"expected {expected}, got {actual}"

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected {substring} to be substring of {full_string}"
 

