# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import sys
import pytest

from envjson import EnvJSON

# set os env
os.environ["TEST_ENV"] = "test-env"


def test_it_should_return_default_value():
    env = EnvJSON(
        json_file="tests/test.json", strict=True
    )
    print(env)
    # assert env["simple_d"] is None
    # assert env["simple_e"] == ""
    # assert env["config.complex"] == "xxxXyyy"
    # assert env["config.with_default"] == "DEFAULT"

