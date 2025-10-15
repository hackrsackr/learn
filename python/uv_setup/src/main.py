import os
from dotenv import load_dotenv

load_dotenv()
id = os.getenv("GCP_PROJECT_ID")
my_key = os.getenv("MY_KEY")
key = os.getenv("KEY")


def main() -> None:
    print(id)
    print(my_key)
    print(key)


if __name__ == "__main__":
    main()
