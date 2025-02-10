import argparse
import asyncio
from index import IndexService, IndexNotFoundException, IndexProtocolException


def check_number_range(value):
    number = int(value)
    if number < 0 or number > 1000000:
        raise argparse.ArgumentTypeError(f"{value} is not in the range [0-1000000]")
    return number


async def fetch_index_value(service, number):
    try:
        value = await service.get_index_value(number)
        print(f"Index value for {number}: {value}")
    except IndexNotFoundException as e:
        print(f"Index not found for {number}: {e.message}")
    except IndexProtocolException as e:
        print(f"Protocol error for {number}: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred for {number}: {str(e)}")


async def main():
    parser = argparse.ArgumentParser(description="Index client sample application using Python")
    parser.add_argument('numbers', type=check_number_range, nargs='+',
                        metavar="[0-1000000]",
                        help='A list of numbers ranging from 0 till 1000000')
    parser.add_argument('--url', type=str, default="http://localhost:8000",
                        help='The API URL to fetch index values from')
    args = parser.parse_args()

    service = IndexService(args.url)

    tasks = [fetch_index_value(service, number) for number in args.numbers]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())