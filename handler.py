import os
import runpy
from helper import GlobalData


def handle(global_state: GlobalData, command: str, *args: list[str]) -> GlobalData:
    if os.path.exists(p := f"commands\\{command.lower()}.py"):
        return runpy.run_path(p).get("command")(global_state, *args)
    else:
        raise Exception(f"Brother! You're putting it in the wrong place! You can't put it in {command}, you fool!")
