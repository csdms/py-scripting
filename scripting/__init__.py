from importlib.metadata import version
from .contexts import cd
from .prompting import error, prompt, status, success
from .unix import cp, ln_s

__version__ = version("py-scripting")
__all__ = ["prompt", "status", "success", "error", "cp", "cd", "ln_s"]
