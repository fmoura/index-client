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

class InvalidArgumentException(Exception):
    """Exception raised when an invalid argument is provided."""
    def __init__(self, message=""):
        super().__init__(message)
        self.message = message

class IndexService:
    def __init__(self, api_url):
        self.api_url = api_url

    async def get_index_value(self,number):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}/index/{number}") as response:
                match response.status:
                    case 200:
                        result = await response.json()
                        if "data" in result and "error message" in result["data"] :
                            raise IndexNotFoundException(result["data"]["error message"])
                        else:
                            if "data" in result:
                                return {"index":result["data"]["index"],"value":result["data"]["value"]}
                            else :
                                raise IndexProtocolException("'data' key not found in response")
                    case 400:
                        result = await response.json()
                        if "error" in result and "message" in result["error"]:
                            raise InvalidArgumentException(result["error"]["message"])
                        else:
                            raise IndexProtocolException("'error' or 'error:message' key not found in response")
                    case 500:
                        result = await response.json()
                        if "error" in result and "message" in result["error"]:
                            raise Exception(result["error"]["message"])
                        else:
                            raise IndexProtocolException("'error' or 'error:message' key not found in response")
                    case _:
                        raise IndexProtocolException(f"Unexpected response status: {response.status}")