# Asyncio Baking Simulation

## Overview
จากโค๊ดนี้แสดงให้เห็นวิธีใช้ไลบรารี asyncio ของ Python เพื่อรันงานแบบ Asynchronous หลายงานพร้อมกัน โดยในโค๊ดเป็นตัวอย่างการทำงานของการอบขนมปังโดยแต่ละก้อนต้องใช้เวลาทั้งหมด 
7 วินาที มีอุ่นเตา 2 วินาที และอบอีก 5 วินาที ซึ่งเราจะใช้ asyncio กระบวนการอบทั้งหมดจะทำงานพร้อมกัน ช่วยลดระยะเวลาในการทำงานเมื่อเทียบกับการรันแบบเรียงลำดับ
## How It Works
-ฟังก์ชัน bake เป็น coroutine แบบ asynchronous ที่จำลองกระบวนการอบขนมปัง
-ฟังก์ชัน main จะสร้างและจัดการงานอบขนมปัง 50 ก้อนโดยใช้ asyncio.create_task()

-asyncio.wait(tasks) ใช้เพื่อรอให้ทุกงานเสร็จสิ้นก่อนดำเนินการต่อ

-สคริปต์จะวัดเวลาการทำงานทั้งหมดโดยใช้ time.time()

-หากรันแบบเรียงลำดับ สคริปต์จะใช้เวลาประมาณ 7 × 50 = 350 วินาที แต่ด้วย asyncio จะใช้เวลาเพียง ประมาณ 7 วินาที เนื่องจากสามารถรันงานพร้อมกันได้

## Prerequisites

- Python 3.7+

## How to Run
1. git clone https://github.com/chetod/python_simple_asyncio.git
2. Run the script using:
   ```bash
   python async_baking.py
   ```


## Example expected Output
![image](https://github.com/user-attachments/assets/43daf73e-8eee-420d-a230-0510fe796cf0)
![image](https://github.com/user-attachments/assets/9d5a5108-b0bc-4c6f-893d-2ac5d669af71)
![image](https://github.com/user-attachments/assets/3dc9e83e-ca8a-4c67-86d0-e510bb463502)

สรุปการทำงานโค๊ด ถ้าเป็นปกติจะทำงานเรียงตามลำดับ แต่ถ้าเป็น asyncio จะทำงานพร้อมกัน และเสร็จเร็วกว่า
เช่น ถ้าเป็นปกติจะใช้เวลาประมาณ 7*50 วินาที(50 loop loopละ 7 วิ) แต่ถ้าเป็น asyncio จะใช้เวลาประมาณ 7 วิ 
มันเร็วกว่าเพราะไม่ต้องรอให้ loop ทำงานเสร็จก่อนถึงทำงาน loop ถัดไป และมันยังกลับมาทำ callback ต่อไปได้ทันที





