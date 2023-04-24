import pytest
from .context import sinterface

# @todo Finish tests for sinterface module.
# Needs a mocked serial connection to test connect/write/readline methods.
# See coverage report for more info.

NoPortSetExc = sinterface.NoPortSetException
NoConnExc = sinterface.NoConnectionException

test_settings = sinterface.SerialPortSettings(
    port="COM3",
    baudrate=115200,
    bytesize=8,
    parity="N",
    stopbits=1,
    timeout=1,
    xonxoff=False,
    rtscts=False,
    write_timeout=0,
    dsrdtr=False,
    inter_byte_timeout=0,
)


def test_init():
    """Test the init method."""
    sio = sinterface.SerialIO()
    assert sio.portsettings is None
    assert sio.linenumber == 0


def test_apply_settings():
    """Test the apply_settings method."""
    sio = sinterface.SerialIO()
    sio.apply_settings(test_settings)
    assert sio.portsettings == test_settings


@pytest.mark.asyncio
async def test_connect():
    """Test the connect method."""
    sio = sinterface.SerialIO()
    with pytest.raises(NoPortSetExc):
        await sio.connect()


@pytest.mark.asyncio
async def test_err_write():
    """Test the write method."""
    sio = sinterface.SerialIO()
    with pytest.raises(NoConnExc):
        await sio.write(b"test")


@pytest.mark.asyncio
async def test_err_readline():
    """Test the readline method."""
    sio = sinterface.SerialIO()
    with pytest.raises(NoConnExc):
        await sio.readline()
