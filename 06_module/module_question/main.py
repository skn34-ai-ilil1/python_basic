# main.py

import team_module
import attendance_module    
import task_module
import math
import datetime
import calculator

print("안녕하세요, 주식회사 SQUIRREL입니다.")

print(team_module.introduce_manager())
print(team_module.introduce_developer())

print(attendance_module.record_attendance("카피바라", "9:00"))
print(attendance_module.record_leave("카피바라", "18:00"))

print(task_module.start_task("코드 리뷰"))
print(task_module.complete_task("코드 리뷰"))

업무량 = [10, 12, 8, 15, 9]
평균_업무량 = math.fsum(업무량) / len(업무량)
print(f"평균 업무량: {평균_업무량}")

count = 0
for i in 업무량:
    if i > 평균_업무량:
        count +=1

print(count)


print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 카피바라님이 작업 '코드 리뷰'을(를) 완료했습니다.")