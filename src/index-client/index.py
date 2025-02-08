import aiohttp


class IndexNotFoundException(Exception):
    """Exception raised when an index is not found."""
    def __init__(self, message=""):
        super().__init__(message)
        self.message = message

class IndexProtocolException(Exception):
    """Exception raised when protocol is not respected."""
    def __init__(self, message=""):
        super().__init__(message)
        self.message = message

class IndexService:
    def __init__(self, api_url):
        self.api_url = api_url

async def get_index_value(self,number):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{self.api_url}{number}") as response:
            if response.status == 200:
                result = await response.json()
                if "data" in result and "message" in result["data"] :
                    raise IndexNotFoundException(result["data"]["message"])
                else:
                    if "data" in result:
                        return result["data"]
                    else :
                        raise IndexProtocolException("'data' key not found in response")
            else:
                return "Error retrieving value"