from Subject import Subject, Lecture
import PIL
from PIL import ImageDraw, ImageFont
from str_div import str_divider

class SubjectOverlapException(Exception):
    def __init__(self, message=None):
        super().__init__()
        self.message = message

    def __str__(self):
        if (self.message != None):
            return self.message
        
        return "There are subjects that have overlapping schedules."

class TimeTableGenerator:
    def __init__(self, subjects : list[Subject] = None):
        self.subjects = []
        if (subjects != None): self.subjects = subjects
        
    def generate(self, path : str):
        classes_by_day = {
                          "월": [],
                          "화": [],
                          "수": [],
                          "목": [],
                          "금": [],
                          "토": [],
                          "일": []
                          }
        
        for subject in self.subjects:
            for idx, lecture in enumerate(subject.lectures):
                classes_by_day[lecture[0]].append({subject : subject.times[idx]})

        if self.__overlap_check(classes_by_day):
            raise SubjectOverlapException

        self.__draw_time_table(classes_by_day, path)

    def addSubject(self, target : Subject):
        self.subjects.append(target)

    def removeSubject(self, index : int):
        self.subjects.remove(index)
    
    def clearSubjects(self):
        self.subjects.clear()

    def __overlap_check(self, classes_by_day : dict[str, list]):
        for an_yoil in list(classes_by_day.values())[:5]:

            if len(an_yoil) >= 2:

                for idx, x in enumerate(an_yoil):
                    x_values = tuple(x.values())[0]
                    if x_values != "사이버수업":

                        for y in an_yoil[idx + 1:]:
                            y_values = tuple(y.values())[0]
                            if (y_values[0] <= x_values[0] <= y_values[1] or y_values[0] <= x_values[1] <= y_values[1]) or (x_values[0] <= y_values[0] <= x_values[1] or x_values[0] <= y_values[1] <= x_values[1]):  # {"이름": (0, 1)}
                                return True

        return False

    def __convert_px(self, height, x):
        return (height / 60) * x

    def __draw_time_table(self, dictionary : dict[str, list], path : str):
        """시간표 그리기"""
        max_time = 0

        # dictionary = dictionary[:5]

        for an_yoil in list(dictionary.values())[:5]:  # 금요일까지만 

            for subject in an_yoil:
                subject_time = tuple(subject.values())[0]

                if type(subject_time) is tuple:  # "사이버수업" 을 비교하는 것을 방지
                
                    if subject_time[1] > max_time:
                        max_time = subject_time[1]
        
        nrow = (round(max_time / 60)) + 1

        header_img = PIL.Image.open("images/header.png")
        row_frame_img = PIL.Image.open("images/rowFrame.png")

        width = 959; total_height = 39 + (row_frame_img.size[1] * nrow)

        result_img = PIL.Image.new("RGB", (width, total_height), (255, 255, 255))
        y_offset = 0; x_offset = 0

        result_img.paste(header_img, (0, y_offset))
        y_offset += header_img.size[1]

        for i in range(nrow):  # 시간표 프레임 형성하기
            result_img.paste(row_frame_img, (0, y_offset))
            y_offset += row_frame_img.size[1]

        draw = PIL.ImageDraw.Draw(result_img)

        font = PIL.ImageFont.truetype(r".\\fonts\\NanumSquare_acR.ttf", size=15)
        font_bold = PIL.ImageFont.truetype(r".\\fonts\\NanumSquareB.ttf", size=17)
        color_black = "rgb(0, 0, 0)"
        color_white = "rgb(255, 255, 255)"

        y_offset = 39; x_offset = 0

        for i in range(nrow):  # 시간표의 시간 열에 시간 적어주기
            content = str(i + 8) + " 시"
            f_size = font.getsize(content)
            y_pos = ((row_frame_img.size[1] - 1) / 2) - (f_size[1] / 2)
            x_pos = (58 / 2) - (f_size[0] / 2)
            draw.text((x_pos, y_offset + y_pos), content, font=font, fill=color_black)

            y_offset += row_frame_img.size[1]

        y_offset = 39; x_offset = 59

        for an_yoil in list(dictionary.values())[:5]:  # 금요일까지만 

            for subject in an_yoil:
                subject_time = tuple(subject.values())[0]
                subject_info = tuple(subject.keys())[0]

                if type(subject_time) is tuple:
                    pix_loc = (self.__convert_px(row_frame_img.size[1], subject_time[0]), self.__convert_px(row_frame_img.size[1], subject_time[1]))
                    class_img = PIL.Image.new("RGB", (179, int(pix_loc[1] - pix_loc[0])), subject_info.color)  # 픽셀 위치는 정수로 줘야 함
                    result_img.paste(class_img, (x_offset, y_offset + int(pix_loc[0])))

                    row_limit = 10  # 한 칸에 적힐 수 있는 글자 수 제한

                    divided = str_divider(subject_info.subject_name, row_limit)

                    str_divided = ""

                    for i in divided:
                        str_divided += f"{i}\n"

                    str_divided += f"{subject_info.lectures[0][-1]}"

                    draw.text((x_offset + 10, int(pix_loc[0]) + 50), str_divided, font=font_bold, fill=color_white)

            
            x_offset += 180

        result_img.save(path)  # 생성한 이미지를 렌더링해 저장

if __name__ == "__main__":
    ttgen = TimeTableGenerator()
    ttgen.addSubject(
        Subject("이산수학", "1234", [Lecture(0, "10:00", 240, "1234"),Lecture(2, "10:00", 240, "1234")])
    )
    ttgen.generate("./res.png")
