import asyncio
import logging

from core.bot import main

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,  # Set the minimum severity level to log
        filename='app_log.txt',  # **Crucial: Specifies the output file**
        filemode='a',  # 'a' appends (adds to the end), 'w' overwrites
        format='%(asctime)s - %(levelname)s - %(message)s'  # Define the log message format
    )
    try:
        print("Starting Bakery Bot...")
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Exit')
