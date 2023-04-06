#!/usr/bin/env python

"""Tests for `get_html_from_safari` package."""

import pytest,time
from get_html_from_safari import get_html_from_safari
from get_html_from_safari.get_html_from_safari import get_html, run_as

def test_safari_running():
    run_as('safari_activate')
    time.sleep(1)
    running = run_as('safari_is_running')
    assert running == 'true'

def test_safari_running_without_url():
    out = get_html()
    assert '<head>' in out, "Expected '<head>' to be in output"

def test_without_safari_running():
    run_as('safari_quit')
    time.sleep(1)
    with pytest.raises(get_html_from_safari.SafariIsNotRunning):
        get_html()

def test_safari_not_running_with_url():
    time.sleep(1)
    out = get_html('https://www.google.com')
    assert '<head>' in out, "Expected '<head>' to be in output"

