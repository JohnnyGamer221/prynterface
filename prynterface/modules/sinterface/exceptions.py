class NoPortSetException(Exception):
    """Raised by SerialIO.connect() if no port is set."""

    pass


class NoConnectionException(Exception):
    """Raised by SerialIO. write() or read() if no connection is established."""

    pass
