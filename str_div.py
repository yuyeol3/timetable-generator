def str_divider(content: str, len_limit: int):

    counter = 0
    index = 0

    div_container = ["" for i in range(floatrounder(len(content) / len_limit))]


    for i in content:
        div_container[index] += i

        counter += 1

        if counter == len_limit:
            counter = 0
            index += 1

    return div_container


def floatrounder(x: float):
    """실수형 변수를 입력받아, 소수점 뒤의 값이 0이면 입력값을 그대로 정수화해 반환하고, 그렇지 않으면 소수점을 자르고 1을 더해 정수화하는 함수"""
    if x == int(x):
        return int(x)
    
    elif x > int(x) or x < int(x):
        return int(x) + 1


if __name__ == "__main__":
    divided = str_divider("동해물과백두산이마르고닳도록하느님이보우하사우리나라만세무궁화삼천리화려강산대한사람대한으로길이보전하세남산위에저소나무철갑을", len_limit=10)
    
    for i in divided:
        print(i)
