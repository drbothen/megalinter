# !/usr/bin/env python3
"""
Unit tests for REPOSITORY linter semgrep
This class has been automatically @generated by .automation/build.py, please do not update it manually
"""

from unittest import TestCase

from megalinter.tests.test_megalinter.LinterTestRoot import LinterTestRoot


class repository_semgrep_test(TestCase, LinterTestRoot):
    descriptor_id = "REPOSITORY"
    linter_name = "semgrep"
