import aiohttp
import asyncio


class IndexNotFoundException(Exception):
    """Exception raised when an index is not found."""
    def __init__(self, message=""):
        super().__init__(message)
        self.message = message

async def get_index_value(number):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.example.com/index/{number}") as response:
            if response.status == 200:
                result = await response.json()
                if "data" in result and "message" in result["data"] :
                    raise IndexNotFoundException(result["data"]["message"])
                else:
                    return result["data"]
            else:
                return "Error retrieving value"