import asyncio
import logging

from core.bot import main

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        print("Starting Bakery Bot...")
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Exit')
