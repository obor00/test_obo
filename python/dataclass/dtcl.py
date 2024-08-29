from dataclasses import dataclass

@dataclass
class TotoConfArgs:
    arg1: str
    arg2: int
    arg3: bool

args = TotoConfArgs(arg1="value1", arg2=123, arg3=True)
args_dict = dataclasses.asdict(args)
print(args_dict)
