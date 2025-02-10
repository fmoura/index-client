import pytest
from aioresponses import aioresponses
from index import IndexService, IndexNotFoundException, IndexProtocolException, InvalidArgumentException

@pytest.mark.asyncio
async def test_get_index_value_success():
    api_url = "http://localhost:8000"
    service = IndexService(api_url)
    number = 123

    with aioresponses() as mocked:
        mocked.get(f"{api_url}/index/{number}", payload={"data": {"index": number, "value": 456}})

        result = await service.get_index_value(number)
        assert result == {"index": number, "value": 456}

@pytest.mark.asyncio
async def test_get_index_value_not_found():
    api_url = "http://localhost:8000"
    service = IndexService(api_url)
    number = 123

    with aioresponses() as mocked:
        mocked.get(f"{api_url}/index/{number}", status=200, payload={"data": {"error message": "Index not found"}})

        with pytest.raises(IndexNotFoundException):
            await service.get_index_value(number)

@pytest.mark.asyncio
async def test_get_index_value_protocol_error():
    api_url = "http://localhost:8000"
    service = IndexService(api_url)
    number = 123

    with aioresponses() as mocked:
        mocked.get(f"{api_url}/index/{number}", status=200, payload={})

        with pytest.raises(IndexProtocolException):
            await service.get_index_value(number)

@pytest.mark.asyncio
async def test_get_index_value_invalid_argument():
    api_url = "http://localhost:8000"
    service = IndexService(api_url)
    number = 123

    with aioresponses() as mocked:
        mocked.get(f"{api_url}/index/{number}", status=400, payload={"error": {"message": "Invalid argument"}})

        with pytest.raises(InvalidArgumentException):
            await service.get_index_value(number)

@pytest.mark.asyncio
async def test_get_index_value_unexpected_error():
    api_url = "http://localhost:8000"
    service = IndexService(api_url)
    number = 123

    with aioresponses() as mocked:
        mocked.get(f"{api_url}/index/{number}", status=500, payload={"error": {"message": "Unexpected error"}})

        with pytest.raises(Exception):
            await service.get_index_value(number)