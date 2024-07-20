from TimeTableGenerator import TimeTableGenerator
from Subject import Subject, Lecture

if __name__ == "__main__":
    # 강의 생성
    lecture1 = Lecture(day=0, start_h="10:00", period="120", classroom="A101")
    lecture2 = Lecture(day=2, start_h="13:00", period="90", classroom="B202")

    # 과목 생성
    subject1 = Subject(subject_name="수학", subject_code="MATH101", lectures=[lecture1])
    subject2 = Subject(subject_name="물리학", subject_code="PHY101", lectures=[lecture2])

    # 시간표 생성기 초기화
    ttgen = TimeTableGenerator(subjects=[subject1, subject2])

    # 시간표 생성
    ttgen.generate(path="./res.png")