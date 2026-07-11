"""Convenient repository-root entry point for the weekly workspace generator."""

from __future__ import annotations

import runpy
from pathlib import Path


SCRIPT = Path(__file__).parent / "School" / "Computer-Science" / "scripts" / "new_week.py"
runpy.run_path(str(SCRIPT), run_name="__main__")
