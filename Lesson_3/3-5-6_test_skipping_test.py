#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-
import time, unittest
from selenium import webdriver
import pytest


@pytest.mark.xfail(strict=False)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False