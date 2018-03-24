#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sillysort` package."""

import pytest

from click.testing import CliRunner

from sillysort import sillysort
from sillysort import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'sillysort.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_Silly_sort(capsys):
    """We use the capsys argument to capture printing to stdout."""
    # The silly_sort function sort a list, but returns nothing.
    assert sillysort.silly_sort([1,2,3,4]) == None

    # Capture the result of the sillysort.silly_sort function call.
    captured = capsys.readouterr()

    # If we check captured, we can see that the the silly string has been planted.
    assert "Silly!" in captured.out
    assert "Silly!" in captured.out   
    assert "Silly!" in captured.out
    assert "Silly!" in captured.out
