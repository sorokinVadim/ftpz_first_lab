from dataclasses import dataclass, field
from typing import Iterable
import os
import logging


@dataclass
class Timer:
    seconds: int 
    filename: str

def new_timer(timer_line: str) -> Timer:
    filename, seconds = timer_line.split(" ")
    seconds = int(seconds)
    return Timer(seconds=seconds, filename=filename)
        

@dataclass
class Config:
    timers: Iterable[Timer] = field(default_factory= lambda: [])

class ReadConfigException(Exception): ...
class ConfigNotExist(Exception): ...

def open_config(config_file = "timers.txt"):
    if config_file not in os.listdir():
        raise ConfigNotExist

    with open(config_file, 'r') as file:
        lines = file.read().split("\n")
        lines = [line for line in lines if line != ""]
    logging.debug(f"Lines: {lines}")

    try:
        config = Config(timers=[new_timer(line) for line in lines])
    except Exception as ext:
        raise ReadConfigException(ext)

    return config 

