import asyncio
import httpx
from httpx import HTTPError


async def request_task(client: httpx.AsyncClient, url):
    try:
        request = await client.get(url)
        content = request.text
    except HTTPError as error:
        content = str(error)
    with open('content_output.txt', 'a+') as file:
        file.write(f"--{url}--\n{content}\n")


async def main(urls: list):
    client = httpx.AsyncClient()
    requests_tasks = [asyncio.create_task(request_task(client, url)) for url in
                      urls]
    await asyncio.gather(*requests_tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        main(['https://www.google.com', 'https://mail.ru']))
    loop.close()
