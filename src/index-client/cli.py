import argparse
import asyncio

async def main():
    parser = argparse.ArgumentParser(description="Index client sample application using Python")
    parser.add_argument('number', required=True, type=int, choices=range(0,100),
                   metavar="[0-100]", 
                   help='A number ranging from 0 till 100')
    args = parser.parse_args()

    value = await get_index_value(args.number)



if __name__ == "__main__":
    asyncio.run(main())