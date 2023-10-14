import shutil
from datetime import datetime
import logging
import asyncio

from . import config


async def timered_maker(timer: config.Timer):
    while True:
        await asyncio.sleep(timer.seconds)
        logging.info(f"Run with timer {timer.seconds}")

        archname = "archive_" + str(datetime.today())[:-7].replace(" ", "_") \
                .replace(":", "").replace("-", "") + ".zip"
        logging.info(f"Make an archive with name {timer.filename}")

        shutil.make_archive(archname, "zip", timer.filename)

        logging.info(f"Done with timer {timer.seconds}")

