import re


class Detector:
    """@todo Implement Detector class
    - Gets some data from SerialIO --> main --> Parser --> Detector
    - Stores it in a buffer, must be complete lines.
    - Runs regex on buffer according to config
    - matches get extracted to free space from buffer
    - Parser gets data via output buffer
    - block type should only be scanned when there is a safe stopping point (e.g. ok, wait, error)
    """

    def __init__(self, detector_config: dict) -> None:
        pass


class Extractor:
    """@todo Implement Extractor class
    - Gets data from Parser --> Detector --> Extractor
    - Extracts match groups according to config
    - Returns data to Parser
    """

    def __init__(self, extractor_config: dict) -> None:
        pass
