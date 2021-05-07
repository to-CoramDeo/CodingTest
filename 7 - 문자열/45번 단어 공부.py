# 문제: 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력: 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력: 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

words = input().upper()
unique_words = list(set(words))

unique_words_count_list = []
for i in range(len(unique_words)): # 추출한 알파벳 단어의 개수만큼 반복
    unique_words_count = words.count(unique_words[i])
    unique_words_count_list.append(unique_words_count)

if unique_words_count_list.count(max(unique_words_count_list)) > 1:
    print("?")
else:
    print(unique_words[unique_words_count_list.index(max(unique_words_count_list))])

# 알고리즘 순서
# 1) 단어(알파벳 대소문자)를 입력 받는다.
# - 자료 이름: words     # var, 'str'
# - 입력받는 방법: words = input()

# 2) 입력 받은 알파벳 단어를 대문자로 바꿔준다. # 출력 값이 알파벳 대문자
# - 대문자로 바꿔주는 방법: words = input().upper()      # var, 'str'
# -- type(input()): 'str' == type(upper()): 'str'

# 3) 단어에 있는 알파벳을 추출한다. = 중복된 알파벳을 제거한다. 
# - 자료 이름: unique_words     # list
# - 중복된 문자를 제거하는 방법: set(words)

# 4) 입력 받은 알파벳 단어에 있는 추출한 알파벳의 개수를 구한다.   
# - 자료 이름: unique_words_count     # var, int
# - 문자열 안에 포함된 특정한 문자의 개수를 세는 방법: words.count('str')   
# - 자료 구조: unique_words_count_list     # list

# 5) 개수의 최대값이 2 : 1 = "?" :  "추출한 알파벳"을 출력한다.
# - 최대값 구하는 방법: max()