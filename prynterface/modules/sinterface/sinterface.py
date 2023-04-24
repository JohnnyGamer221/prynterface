import serial_asyncio
from dataclasses import dataclass


@dataclass
class SerialPortSettings:
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


class NoPortSetException(Exception):
    """Raised by SerialIO.connect() if no port is set."""

    pass


class NoConnectionException(Exception):
    """Raised by SerialIO. write() or read() if no connection is established."""

    pass


class SerialIO:
    """SerialIO class
    Sets up an asynchronous serial connection to a serial port.
    """

    def __init__(self):
        """Does almost nothing."""
        self.portsettings = None
        self.linenumber = 0
        self.is_connected = False

    def apply_settings(self, sps: SerialPortSettings):
        """Applys a SerialPortSettings object.

        Args:
            sps (SerialPortSettings): Settings object containing all neded info.
        """
        self.portsettings = sps

    async def connect(self):
        """Try to connect to the port specified in the settings.

        Raises:
            Exception: If not port is set.
            e: something goes very wrong.
        """
        if self.portsettings is None:
            raise NoPortSetException("No port set to connect to.")
        try:
            self.reader, self.writer = await serial_asyncio.open_serial_connection(
                url=self.portsettings.port,
                baudrate=self.portsettings.baudrate,
                bytesize=self.portsettings.bytesize,
                parity=self.portsettings.parity,
                stopbits=self.portsettings.stopbits,
                timeout=self.portsettings.timeout,
                xonxoff=self.portsettings.xonxoff,
                rtscts=self.portsettings.rtscts,
                write_timeout=self.portsettings.write_timeout,
                dsrdtr=self.portsettings.dsrdtr,
                inter_byte_timeout=self.portsettings.inter_byte_timeout,
            )
            self.is_connected = True
        except Exception as e:
            raise e

    async def write(self, data: bytes):
        """Writes some data to the existing connection.

        Args:
            data (bytes): data to be written.

        Raises:
            e: something goes very wrong.
        """
        if not self.is_connected:
            raise NoConnectionException("No connection established.")
        try:
            self.writer.write(data)
            await self.writer.drain()
        except Exception as e:
            raise e

    async def readline(self) -> tuple:
        """Reads a line of data from an initialized connection.

        Raises:
            e: something goes very wrong.

        Returns:
            tuple: line, linenumber
        """
        if not self.is_connected:
            raise NoConnectionException("No connection established.")
        try:
            self.linenumber += 1
            return await self.reader.readline(), self.linenumber
        except Exception as e:
            self.linenumber -= 1
            raise e
