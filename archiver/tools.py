import shutil
from datetime import datetime
import logging
import asyncio
from random import randint as rint

from . import config


async def timered_maker(timer: config.Timer):
    while True:
        await asyncio.sleep(timer.seconds)
        logging.info(f"Run with timer {timer.seconds}")
        now = datetime.today()
        archname = f"archive_{now.strftime('%Y%m%d%H%S')}{rint(1000, 9999)}"
        logging.info(f"Make an archive with name {timer.filename}")
        shutil.make_archive(archname, "zip", timer.filename)
        logging.info(f"Done with timer {timer.seconds}")

