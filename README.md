
# 시간표 생성기

이 레포지토리는 시간표를 생성하는 Python 프로젝트입니다. 이 프로젝트는 시간표를 이미지로 생성하기 위한 모듈을 포함하고 있습니다.

## 특징

- **과목 및 강의 관리**: 과목과 해당 강의를 정의할 수 있습니다.
- **시간표 생성**: 주어진 과목과 강의로부터 시간표를 이미지로 생성합니다.
- **충돌 감지**: 겹치는 강의 시간을 확인하고 적절히 처리합니다.
- **문자열 분할**: 문자열을 작은 세그먼트로 나누는 유틸리티 함수.

## 설치 방법

1. 저장소를 클론합니다:

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. 필요한 의존성을 설치합니다:

   ```bash
   pip install -r requirements.txt
   ```

## 사용법

### 모듈 개요

1. **`__init__.py`**
   - 시간표 생성기와 과목 모듈을 초기화합니다.

2. **`str_div.py`**
   - 문자열을 지정된 길이의 세그먼트로 나누는 `str_divider` 함수를 포함하고 있습니다.
   - 사용 예:
     ```python
     divided = str_divider("분할할 문자열", len_limit=10)
     for segment in divided:
         print(segment)
     ```

3. **`Subject.py`**
   - `Lecture` 및 `Subject` 클래스를 정의합니다.
   - 사용 예:
     ```python
     from Subject import Subject, Lecture

     lecture1 = Lecture(day=0, start_h="10:00", period="120", classroom="A101")
     subject = Subject(subject_name="수학", subject_code="MATH101", lectures=[lecture1])
     ```

4. **`TimeTableGenerator.py`**
   - 시간표 생성을 담당하는 `TimeTableGenerator` 클래스를 포함하고 있습니다.
   - 사용 예:
     ```python
     from TimeTableGenerator import TimeTableGenerator, Subject, Lecture

     lecture1 = Lecture(day=0, start_h="10:00", period="120", classroom="A101")
     subject = Subject(subject_name="수학", subject_code="MATH101", lectures=[lecture1])

     ttgen = TimeTableGenerator(subjects=[subject])
     ttgen.generate(path="./timetable.png")
     ```

### 예제

다음은 시간표를 생성하는 전체 예제입니다:

```python
from TimeTableGenerator import TimeTableGenerator, Subject, Lecture

# 강의 생성
lecture1 = Lecture(day=0, start_h="10:00", period="120", classroom="A101")
lecture2 = Lecture(day=2, start_h="13:00", period="90", classroom="B202")

# 과목 생성
subject1 = Subject(subject_name="수학", subject_code="MATH101", lectures=[lecture1])
subject2 = Subject(subject_name="물리학", subject_code="PHY101", lectures=[lecture2])

# 시간표 생성기 초기화
ttgen = TimeTableGenerator(subjects=[subject1, subject2])

# 시간표 생성
ttgen.generate(path="./timetable.png")
```

## 기여

기여는 언제나 환영합니다! 개선 사항이나 버그 수정을 위해 이슈를 열거나 풀 리퀘스트를 제출해 주세요.
