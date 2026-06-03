from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Check:
    id: str
    severity: str
    passed: bool
    message: str
    evidence: str = ""
