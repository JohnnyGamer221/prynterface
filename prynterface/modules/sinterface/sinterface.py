import serial_asyncio

from serialport import scan_ports, SerialPort
from exceptions import NoPortSetException, NoConnectionException


# Old SerialIO class didn't use generators as IO, this one will.
class SerialIO:
    """Provides an asynchronous Generator for reading from a serial port and accepts an asynchronous Generator for writing to a serial port.
    output_generator is an asynchronous Generator that yields bytes objects.
    input_generator is an asynchronous Generator that yields bytes objects.
    """
