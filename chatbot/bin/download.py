import requests
import loguru
import os
from dotenv import load_dotenv


def download(url, dist_path):
    res = requests.get(url)

    with open(dist_path, "wb") as dist:
        dist.write(res.content)


if __name__ == "__main__":
    load_dotenv()
    URL = os.getenv("DATASET_URL")
    DIST_PATH = os.getenv("DIST_PATH")

    loguru.logger.info("Downloading datasets...")
    download(URL, DIST_PATH)
    loguru.logger.info("Done!")
