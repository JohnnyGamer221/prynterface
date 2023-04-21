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


# @todo SerialIO class [tests]
# Implement tests for SerialIO class


class SerialIO:
    def __init__(self):
        self.printer = None
        self.linenumber = 0

    def apply_settings(self, sps: SerialPortSettings):
        self.printer = sps

    async def connect(self):
        if self.printer is None:
            raise Exception("No printer set to connect to.")
        try:
            self.reader, self.writer = await serial_asyncio.open_serial_connection(
                url=self.printer.port,
                baudrate=self.printer.baudrate,
                bytesize=self.printer.bytesize,
                parity=self.printer.parity,
                stopbits=self.printer.stopbits,
                timeout=self.printer.timeout,
                xonxoff=self.printer.xonxoff,
                rtscts=self.printer.rtscts,
                write_timeout=self.printer.write_timeout,
                dsrdtr=self.printer.dsrdtr,
                inter_byte_timeout=self.printer.inter_byte_timeout,
            )
        except Exception as e:
            raise e

    async def write(self, data: bytes):
        try:
            self.writer.write(data)
            await self.writer.drain()
        except Exception as e:
            raise e

    async def readline(self):
        try:
            self.linenumber += 1
            return await self.reader.readline(), self.linenumber
        except Exception as e:
            self.linenumber -= 1
            raise e
