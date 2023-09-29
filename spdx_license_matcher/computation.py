from typing import List
from spdx_license_matcher.build_licenses import SpdxLicense
from spdx_license_matcher.normalize import normalize
from spdx_license_matcher.sorensen_dice import get_dice_coefficient


def compute_match_scores(inputText, licenses: List[SpdxLicense]):
    """Normalizes the given license text and forms bigrams before comparing it
    with a database of known licenses.

    Arguments:
        text {string} -- text is the license text input by the user.

    Returns:
        dictionary -- dictionary with license name as key and dice coefficient as value.
    """
    matches = {}
    normalizedInputText = normalize(inputText)
    for license in licenses:
        matches[license.spdx_id] = get_dice_coefficient(
            normalizedInputText, license.normalized_text
        )
    return matches
