import pkg_resources
from .contexts import cd
from .prompting import error, prompt, status, success
from .unix import cp, ln_s

__version__ = pkg_resources.get_distribution("py-scripting").version
__all__ = ["prompt", "status", "success", "error", "cp", "cd", "ln_s"]
