import pytest

from spdx_license_matcher import matcher



def test_matcher():
    license_utils = matcher.SpdxLicenseUtils()
    license_text = [l for l in license_utils.licenses if l.spdx_id == "MIT"][0].text
    license_text = license_text.replace(" <year> <copyright holders>", " 2021 Jon Doe")

    matching= license_utils.match_text_to_id(license_text)
    print(matching)