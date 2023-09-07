from dataclasses import dataclass, field


@dataclass
class GlobalData:
    modules: list[str] = field(default_factory=list)
    loop_stack: list[int] = field(default_factory=list)
    output_end: bool = True
    is_done: bool = False
