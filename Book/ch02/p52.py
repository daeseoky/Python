# 특정 글자 수 반환
oneline = 'this is one line string'
print('t 글자수 : ', oneline.count('t'))

# 접두어 문자 비교 판단
print(oneline.startswith('this'))
print(oneline.startswith('that'))

# 문자열 교체
print(oneline.replace('this', 'that'))

# 문자열 분리 : 문단 -> 문장
multiline = '''this is
multi line
string'''
sent = multiline.split(('\n'))
print('문장: ', sent)
# 문자열 분리2 : 문장 -> 단어
words =oneline.split(' ')  #split(sep = ' ') : default

# 문자열 결합 : 단어 -> 문장
sent2 = ','.join(words)
print(sent2)