import re
import sys

def validate_title(title):
    prefix_pattern = r'^(build|chore|ci|docs|feat|fix|perf|refactor|style|test|sample)[:\s].+$'
    max_length = 50
    
    print("The prefix match is:", re.match(prefix_pattern, title, re.IGNORECASE))

    if not re.match(prefix_pattern, title, re.IGNORECASE):
        print("PR title must start with one of the following prefixes: build, chore, ci, docs, feat, fix, perf, refactor, style, test, sample", file=sys.stderr)
        sys.exit(1)

    print("Length of the title:", len(title))

    if len(title) > max_length:
        print(f"PR title must not exceed {max_length} characters", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    title = sys.argv[1]
    validate_title(title)