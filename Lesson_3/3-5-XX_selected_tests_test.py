#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-
import time
import pytest
from selenium import webdriver

import pytest
#@pytest.mark.xfail
#@pytest.mark.smoke
#@pytest.mark.regression
#@pytest.mark.skip(reason="not implemented yet")
#@pytest.mark.beta_users


class TestMainPage():

    @pytest.mark.smoke
    def test_guest_can_login(self):
        assert True

    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self):
        assert True

    @pytest.mark.regression
    def test_guest_should_see_login_link(self):
        #browser.get(link)
        #browser.find_element_by_css_selector("#login_link")
        assert True

    @pytest.mark.smoke
    def test_guest_should_see_basket_link_on_the_main_page(self):
        #browser.get(link)
        #browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        assert True

class TestBasket():

    @pytest.mark.regression
    def test_guest_can_go_to_payment_page(self):
        assert True

    @pytest.mark.regression
    def test_guest_can_see_total_price(self):
        assert True

class TestBookPage():
    @pytest.mark.regression
    def test_guest_can_add_book_to_basket(self):
        assert True

    @pytest.mark.regression
    def test_guest_can_see_book_price(self):
        assert True

