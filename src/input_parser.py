from urllib.parse import urlparse
import argparse
import sys
from typing import Optional

class InputParser:
    @staticmethod
    def extract_subreddit(input_str: str) -> Optional[str]:
        input_str = input_str.strip()

        if input_str.startswith(('https://', 'http://', 'www.', 'reddit.com')):
            if not input_str.startswith(('https://', 'http://')):
                input_str = 'https://' + input_str
            parsed = urlparse(input_str)
            if parsed.netloc != 'www.reddit.com' and parsed.netloc != 'reddit.com':
                return None
            path_parts = parsed.path.split('/')
            if len(path_parts) >= 3 and path_parts[1] == 'r' and path_parts[2]:
                return path_parts[2]
            return None

        elif input_str.startswith(('/r/', 'r/')):
            parts = input_str.split('/')
            valid_parts = [part for part in parts if part]
            if len(valid_parts) >= 2 and valid_parts[0] in ('r', 'r') and valid_parts[1]:
                return valid_parts[1]
            return None

        else:
            if input_str and all(c.isalnum() or c == '_' for c in input_str):
                return input_str
            return None
            
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument('subreddit')
        parser.add_argument('command')
        parser.add_argument('limit', nargs='?', type=int, default=5)
        
        try:
            args = parser.parse_args()
            subreddit = InputParser.extract_subreddit(args.subreddit)
            
            if not args.command:
                print(f"Invalid command: {str(args.command)}")
            if not subreddit:
                print(f"Invalid subreddit: {str(subreddit)}")
                sys.exit(1)

            args.subreddit = subreddit
            return args

        except Exception as e:
            print(f"Error parsing arguments: {str(e)}")
            sys.exit(1)