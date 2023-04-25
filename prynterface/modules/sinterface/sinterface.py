import serial_asyncio

from serialport import scan_ports, SerialPort
from exceptions import NoPortSetException, NoConnectionException


class SerialIO:
    """Provides an asynchronous Generator for reading from a serial port and accepts an asynchronous Generator for writing to a serial port."""
