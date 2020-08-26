import os


if __name__ == "__main__":
    print("1", os.getenv("PAT_TOKEN"))
    print("2", os.getenv("TRAVIS_COMMIT"))
    print("3", os.getenv("TRAVIS_PULL_REQUEST_SHA"))
