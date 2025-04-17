#!/usr/bin/env python
import os
import sys

import django
from django.test.runner import DiscoverRunner

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
    django.setup()
    failures = DiscoverRunner().run_tests(["tests"])
    sys.exit(bool(failures))
