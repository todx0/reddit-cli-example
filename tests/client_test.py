import pytest
import asyncpraw
from client import Client
from config import Config

@pytest.mark.asyncio
@pytest.mark.parametrize("input_str,expected", [
    ("xbiking", 10)
])
async def test_fetch_latest_posts(input_str, expected):
  config = Config()
  client = Client(config)
  result = await client.fetch_latest_posts(input_str, expected)
  assert isinstance(result, list)
  for item in result:
    assert isinstance(item, asyncpraw.models.Submission)
  assert len(result) == expected, f"Failed for '{input_str}': expected '{expected}', got '{result}'"
  await client.close()