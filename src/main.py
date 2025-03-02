import asyncio
from config import Config
from input_parser import InputParser
from command_handler import CommandHandler
from client import Client

async def main():
		
    # Load and validate config
    config = Config()

    # Parse arguments from input
    args = InputParser.parse_arguments()

    # Initialize a Reddit client
    client = Client(config)

    # Initialize command handler
    handler = CommandHandler(client)

    # Execute command
    await handler.execute(args)


if __name__ == '__main__':
    asyncio.run(main())