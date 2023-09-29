import dataclasses
import datetime
import json
import logging
import os
import warnings
from typing import Dict, List

import license_utils
from license_utils import build_licenses
from license_utils.computation import compute_match_scores


def _load_licenses_from_file(cache_file: str):
    if not os.path.exists(cache_file):
        raise RuntimeError(f"License cache file {cache_file} does not exist")
    with open(cache_file, "r") as f:
        licenses_dict = json.load(f)
        if licenses_dict["version"] != license_utils.__version__:
            warnings.warn(
                f"License cache file {cache_file} was created with a different "
                + f"version of spdx-license-matcher (cache version: {licenses_dict['version']}, "
                + f"current version: {license_utils.__version__})."
                + "We thus re-download the licenses and replace the cache."
            )
            raise RuntimeError("Cache file version mismatch")
        return build_licenses.load_licenses_from_dict(licenses_dict["licenses"])


def _store_licenses_to_file(
    licenses: List[build_licenses.SpdxLicense], cache_file: str
):
    licenses_dict = {
        "version": license_utils.__version__,
        "timestamp": datetime.datetime.now().isoformat(),
        "licenses": [dataclasses.asdict(l) for l in licenses],
    }
    os.makedirs(os.path.dirname(cache_file), exist_ok=True)
    with open(cache_file, "w") as f:
        f.write(json.dumps(licenses_dict))


class SpdxLicenseUtils:
    licenses = None

    def __init__(self, cache_file: str | None = None):
        self.cache_file = cache_file
        if cache_file != None:
            try:
                self.licenses = _load_licenses_from_file(cache_file)
            except RuntimeError as e:
                warnings.warn(
                    f"Could not load licenses from cache file: {str(e)}. Will re-download licenses and replace cache."
                )
                pass  # We just re-download the licenses
        else:
            logging.info(
                "No cache file specified. We will re-download the licenses every time."
                "This takes a while and requires a internet connection."
            )

        if self.licenses == None:
            self.fetch_licenses()

    def fetch_licenses(self):
        self.licenses = build_licenses.fetch_spdx_licenses(load_text=True)
        if self.cache_file != None:
            _store_licenses_to_file(self.licenses, self.cache_file)

    def match_text_to_id(self, license_text: str) -> Dict[str, float]:
        return compute_match_scores(license_text, self.licenses)
