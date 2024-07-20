from random import randint
import re

def convert_time(time: str):
    """시간표에 맞게 시간을 변환해주는 함수"""
    temp = time.split(":")
    return((int(temp[0]) - 8) * 60 + int(temp[1]))

class Lecture:
    dayName = ("월", "화", "수", "목", "금", "토", "일")

    def __init__(self, day : int, start_h : str, period : str, classroom : str) -> None:
        self.day = day
        self.start_h = start_h
        self.period = period
        self.classroom = classroom

    def toList(self) -> list[str]:
        res = [
            self.dayName[self.day],
            self.start_h,
            self.period,
            self.classroom
        ]
        return res;

    def toTimeTuple(self) -> tuple[int, int]:
        res = ((
            convert_time(self.start_h),
            convert_time(self.start_h) + int(self.period)
        ))

        return res



class Subject:
    def __init__(self, subject_name: str, subject_code: str, lectures : list[Lecture]):
        global yo_il
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.lectures = [i.toList() for i in lectures]
        self.times = [i.toTimeTuple() for i in lectures]
        self.color = (randint(160, 210),
                     randint(160, 210),
                     randint(160, 210))