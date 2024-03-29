import re
from .helpers import Match


class Detector:
    """@todo Matching of block types, docs, flags, tests"""

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

    # @todo block matches and flags
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
    """@todo docs, tests, flags"""

    def __init__(self, extractor_config: dict) -> None:
        self.config = extractor_config

    def extract(self, data: str, key: str) -> dict:
        buffer = []
        expressions = self.config[key]["expressions"]
        for key, value in expressions.items():
            expression = value["expression"]
            flags = value["flags"]
            match = re.finditer(expression, data)
            for m in match:
                buffer.append({key: m.group(1)})
        merged = {}
        for match in buffer:
            for key, value in match.items():
                if key in merged:
                    if isinstance(merged[key], list):
                        merged[key].append(value)
                    else:
                        merged[key] = [merged[key], value]
                else:
                    merged[key] = value
        return merged
