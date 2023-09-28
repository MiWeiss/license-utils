from typing import Dict
from spdx_license_matcher import build_licenses

from spdx_license_matcher.computation import compute_match_scores

import os


class SpdxLicenseUtils:
    def __init__(self):
        # TODO allow on file caching etc.
        self.licenses = build_licenses.fetch_spdx_licenses(load_text=True)



    def match_text_to_id(self, license_text: str) -> Dict[str, float]:
        return compute_match_scores(license_text, self.licenses)
    

