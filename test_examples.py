import runpy
from pathlib import Path

import pytest

snippets = sorted(
    str(path) for path in Path(".").glob("*.py") if not path.name.startswith("test_")
)


@pytest.mark.parametrize("snippet", snippets)
def test_snippet(snippet):
    runpy.run_path(snippet)
