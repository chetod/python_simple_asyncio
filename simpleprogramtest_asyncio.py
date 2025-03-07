import asyncio
import time


async def bake(bread):
    print(f'Oven ({bread}): Preheating...')
    await asyncio.sleep(2)
    print(f'Oven ({bread}): Baking...')
    await asyncio.sleep(5) 
    print(f'Oven ({bread}): Finished baking!')
    return f'{bread} is ready'


async def main():
    tasks = []
    for i in range(1, 51):  
        tasks.append(asyncio.create_task(bake(f'Bread {i}'))) # สร้าง task 

    done, pending = await asyncio.wait(tasks)

    print(f'Completed tasks: {len(done)}')
    print(f'Uncompleted tasks: {len(pending)}')


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main()) # ใช้ asyncio.run() เพื่อเรียกใช้ main() และสร้าง event loop ใหม่
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')

#สรุปการทำงานโค๊ด ถ้าเป็นปกติจะทำงานเรียงตามลำดับ แต่ถ้าเป็น asyncio จะทำงานพร้อมกัน และเสร็จเร็วกว่า
#เช่น ถ้าเป็นปกติจะใช้เวลาประมาณ 7*50 วินาที(50 loop loopละ 7 วิ) แต่ถ้าเป็น asyncio จะใช้เวลาประมาณ 7 วิ 
# มันเร็วกว่าเพราะไม่ต้องรอให้ loop ทำงานเสร็จก่อนถึงทำงาน loop ถัดไป และมันยังกลับมาทำ callback ต่อไปได้ทันที