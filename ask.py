"""
Ask a question on the CLI
"""

import sys
from app.agent import ask

if len(sys.argv) != 2 or not sys.argv[1]:
    raise RuntimeError("Ask a question!")

ask(sys.argv[1])
