import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    """
    Asynchronously fetches content from URL
    """

    start_time = time.time()
    try:
        async with session.get(url) as response:
            content = await response.read()
            end_time = time.time()

            print(f"Fetched {url} in {end_time - start_time:.4f} seconds")
            return content

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


async def main():
    """
    Main function to fetch multiple URLs concurrently
    """

    urls = [
        "https://google.com",
        "https://microsoft.com",
        "https://amazon.com",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    start_time = time.time()
    results = asyncio.run(main())
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.4f} seconds")
