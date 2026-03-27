import importlib.util
import sys
import types


if importlib.util.find_spec("pandas") is None:
    pandas_stub = types.ModuleType("pandas")

    def _missing_read_excel(*args, **kwargs):
        raise RuntimeError("pandas is not installed in this test environment")

    pandas_stub.read_excel = _missing_read_excel
    sys.modules["pandas"] = pandas_stub
