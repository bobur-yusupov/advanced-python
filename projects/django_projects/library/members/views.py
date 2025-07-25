from django.http import StreamingHttpResponse
import asyncio

async def generate_data():
    for i in range(10):
        await asyncio.sleep(0.5)
        yield f"Data chunk {i}\n"

async def main(request):
    response = StreamingHttpResponse(generate_data())

    return response