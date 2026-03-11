from typing import Any, Dict

import pytest


@pytest.fixture
def browser_context_args(browser_context_args: Dict, playwright) -> Dict[str, Any]:
    context = {
        **browser_context_args,
        "locale": "en-US",
        "ignore_https_errors": True,
        "viewport": {"width": 1920, "height": 1080},
    }
    return context
