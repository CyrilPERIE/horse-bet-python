import os
from datetime import date, timedelta
from asyncio import run

from scripts.scraping.scraper import scrap_day


if __name__ == "__main__":
    year = 2020
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    data_folder = f"data/raw/{year}"
    os.makedirs(data_folder, exist_ok=True)

    current_date = start_date
    while current_date < end_date:
        print(f"Scraping {current_date}")
        try:
            run(scrap_day(current_date, data_folder))
        except BaseException as e:
            print(f"\033[91m{e}\033[0m")

        current_date += timedelta(days=1)
