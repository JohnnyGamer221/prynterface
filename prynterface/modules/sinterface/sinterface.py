import serial_asyncio
from .printer import Printer

# @todo SerialIO class [tests]
# Implement tests for SerialIO class


class SerialIO:
    def __init__(self):
        self.printer = None

    def set_printer(self, printer: Printer):
        self.printer = printer

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
            return await self.reader.readline()
        except Exception as e:
            raise e
