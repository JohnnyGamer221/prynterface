import re
from .helpers import Match


class Detector:
    """@todo Implement Detector class
    - Gets some data from SerialIO --> main --> Parser --> Detector
    - Stores it in a buffer, must be complete lines.
    - Runs regex on buffer according to config
    - matches get extracted to free space from buffer
    - Parser gets data via output buffer
    """

    def __init__(self, detector_config: dict) -> None:
        self.config = detector_config
        self.data = ""
        self.line_type_expressions = {}
        for key in detector_config:
            if detector_config[key]["type"] != "line":
                continue
            self.line_type_expressions[str(key)] = detector_config[key]["expression"]

    def set_data(self, data: str) -> None:
        self.data = data

    def get_matches(self) -> list[Match]:
        matches = []
        for key in self.line_type_expressions:
            match = re.finditer(self.line_type_expressions[key], self.data)
            for m in match:
                matches.append(
                    Match(
                        matched_string=m.group(0),
                        start_index=m.start(),
                        end_index=m.end(),
                        key_name=key,
                    )
                )
        return matches


class Extractor:
    """@todo Implement Extractor class
    - Gets data from Parser --> Detector --> Extractor
    - Extracts match groups according to config
    - Returns data to Parser
    """

    def __init__(self, extractor_config: dict) -> None:
        pass
