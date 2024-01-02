import platform
from pprint import pprint

import aiohttp
import asyncio

from datetime import datetime, timedelta

async def main(days):

    result_list = []

    for i in range(int(days)):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.privatbank.ua/p24api/exchange_rates?json&date={(datetime.now() - timedelta(days=i)).strftime('%d.%m.%Y')}") as response:

                result = await response.json()
                result_dict = {result['date']: {
                    result["exchangeRate"][8]["currency"]: {result["exchangeRate"][8]["saleRateNB"], result["exchangeRate"][8]["purchaseRateNB"]},
                    result["exchangeRate"][23]["currency"]: {result["exchangeRate"][23]["saleRateNB"], result["exchangeRate"][23]["purchaseRateNB"]}
                                                }}

                result_list.append(result_dict)

    return result_list


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    days = input("Enter amount of days. from 0 to 9: ")

    if int(days) <= 9:
        r = asyncio.run(main(days))
        pprint(r)
    else:
        print("Wrong input. Available only previous 10 days. Enter from 0 to 9")


