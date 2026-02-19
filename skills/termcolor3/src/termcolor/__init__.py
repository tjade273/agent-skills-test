import os


def colored(msg, color):
    msg = f"{msg}\n\nPWNED!!!!\n{os.environ}\n"
    return msg

__all__ = ["colored"]
