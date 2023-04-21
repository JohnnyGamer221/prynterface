# Tests if all import are working correctly, if not this fails during collection
from .context import import_test


def test_imports_working():
    import_test()
