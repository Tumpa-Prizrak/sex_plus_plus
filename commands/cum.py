from helper import GlobalData


def command(data: GlobalData, loundness: str = "loud"):
    match loundness:
        case "loud":
            data.output_end = True
        case "silently":
            data.output_end = False
        case _:
            raise Exception("Oni-chan! You didn't cum!")
    data.is_done = True
    return data
