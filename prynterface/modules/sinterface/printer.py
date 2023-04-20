from dataclasses import dataclass


@dataclass
class Printer:
    port: str
    baudrate: int
    bytesize: int
    parity: str
    stopbits: float
    timeout: float
    xonxoff: bool
    rtscts: bool
    write_timeout: float
    dsrdtr: bool
    inter_byte_timeout: float
