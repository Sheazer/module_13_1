# import asyncio
# import time
#
# async def notification():
#     print('test1')
#     await asyncio.sleep(5)
#     print('5 seconds later')
#
# async def notification2():
#     print('test2')
#     await asyncio.sleep(3)
#     print('3 seconds later')
#
# async def main():
#     test = asyncio.create_task(notification())
#     test2 = asyncio.create_task(notification2())
#     await test
#     await test2
#     print('End program')
#
# asyncio.run(main())

import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(10 / power)
        print(f'Силач {name} поднял {i}й шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    man1 = asyncio.create_task(start_strongman('Pasha', 3))
    man2 = asyncio.create_task(start_strongman('Denis', 4))
    man3 = asyncio.create_task(start_strongman('Apollon', 5))
    await man1
    await man2
    await man3

asyncio.run(start_tournament())
