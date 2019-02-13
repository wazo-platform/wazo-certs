# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import subprocess

from hamcrest import (
    assert_that,
    equal_to,
)


def test_certificate_needs_subjectaltname_true():
    return_code = subprocess.call(['../bin/certificate-needs-subjectaltname', 'assets/certificate-without-subjectaltname.crt'])
    assert_that(return_code, equal_to(0))
    return_code = subprocess.call(['../bin/certificate-needs-subjectaltname', 'assets/certificate-not-generated-by-wazo.crt'])
    assert_that(return_code, equal_to(1))
    return_code = subprocess.call(['../bin/certificate-needs-subjectaltname', 'assets/certificate-with-subjectaltname.crt'])
    assert_that(return_code, equal_to(1))
