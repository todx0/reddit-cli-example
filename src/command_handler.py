class CommandHandler:
    def __init__(self, client):
        self.client = client
        self.commands = {
            'fetch_latest_posts': self._fetch_latest_posts
        }

    async def execute(self, args) -> None:
        if args.command not in self.commands:
            raise ValueError(f"Unknown command: {args.command}")
        await self.commands[args.command](args)

    async def _fetch_latest_posts(self, args) -> None:
        posts = await self.client.fetch_latest_posts(args.subreddit, args.limit)
        if not posts:
            print(f"No posts found in subreddit '{args.subreddit}' or it may be private/invalid.")
        else:
            for post in posts:
                print(f"Title: {post.title}")
                print(f"Author: {post.author.name}")
                print(f"Upvotes: {post.score}")
                print("---")
        await self.client.close()
