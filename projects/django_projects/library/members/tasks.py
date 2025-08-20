import asyncio

async def process_task(task_id):
    print(f"Processing task {task_id}...")

    await asyncio.sleep(2)

    print(f"Task {task_id} completed.")
    return f"Task {task_id} result"
