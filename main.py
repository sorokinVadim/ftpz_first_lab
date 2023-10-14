from archiver import config as cfg_setup, tools
import logging
import asyncio

logging.basicConfig(level=logging.DEBUG)

async def main():
    config = cfg_setup.Config() 
    try:
        config = cfg_setup.open_config()
    except cfg_setup.ReadConfigException as exp:
        logging.critical(f"Config file not valid, fix them.\nDetails: {exp}")
    except cfg_setup.ConfigNotExist:
        logging.critical("Config does not exist, \
but has been created by me, enter times here.")
    
    logging.info("Run timers")
    async with asyncio.TaskGroup() as tg:
        for timer in config.timers:
            tg.create_task(tools.timered_maker(timer))

        

if __name__ == '__main__':
    asyncio.run(main())
