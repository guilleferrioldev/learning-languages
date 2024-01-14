import asyncio 
"""Synchronous programming"""
# In programming, we can simplify the definition of synchronous code as "a bunch of statements in sequence"; so each statement in your code is executed one after the other. This means each statement has to wait for the previous one to finish executing

"""Coroutines"""
# Coroutine are computer program components that generalize subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed. 


"""Async event-loop"""
# In computer science, the event loop is a programming construct or design pattern that waits for and dispatches events or messages in a program

### Async/Await
async def main():
    print("guille")
    await foo("text")
    print("Finish")

async def foo(text):
    print("Text")
    await asyncio.sleep(1)

#asyncio.run(main())

### Tasks
async def main_2():
    print("guille")
    task = asyncio.create_task(foo_2("text"))
    await asyncio.sleep(2)
    print("Finish")

async def foo_2(text):
    print("Text")
    await asyncio.sleep(1)

#asyncio.run(main_2())

### Example 
async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2.75)
    print("done fetching")
    return {"data": 1}

async def print_number():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task_1 = asyncio.create_task(fetch_data())
    task_2 = asyncio.create_task(print_number())
    await task_1
    await task_2

#asyncio.run(main())
