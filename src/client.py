import certifi
import ssl
import aiohttp
import asyncpraw
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception
from typing import List, Callable
from config import Config

class Client:
    def __init__(self, config: Config):
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context))
        self.reddit = asyncpraw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            username=config.username,
            password=config.password,
            user_agent=config.user_agent,
            requestor_kwargs={"session": self.session}
        )

    @staticmethod
    def with_retry(func: Callable) -> Callable:
        retry_decorator = retry(
            stop=stop_after_attempt(3),
            wait=wait_exponential(multiplier=1, min=4, max=10),
            retry=retry_if_exception(lambda e: not isinstance(e, (
                asyncpraw.exceptions.ClientException, 
                asyncpraw.exceptions.RedditAPIException
            ))),
            reraise=True
        )
        return retry_decorator(func)
				
    @with_retry
    async def fetch_latest_posts(self, subreddit_name: str, limit: int) -> List[asyncpraw.models.Submission]:
        subreddit = await self.reddit.subreddit(subreddit_name)
        posts = []
        async for post in subreddit.new(limit=limit):
            posts.append(post)
        return posts

    async def close(self) -> None:
        await self.reddit.close()
        await self.session.close()