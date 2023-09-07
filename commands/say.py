import helper


def command(data: helper.GlobalData, output: str | None, *args):
    if output not in data.modules and output is not None:
        raise Exception(f"Brother! You're putting it in the wrong place! You can't put it in {output}, you fool!")
    match output:
        case "brunette":
            print(" ".join(args))
        case _:
            raise Exception(f"Brother! You're putting it in the wrong place! You can't put it in {output}, you fool!")
    return data
