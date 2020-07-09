'''1.字符串创建用‘’或者“”；2.字符串的访问截取str[0:5]；3.转义符（）4.+ ：字符串的连接；*：重复输出；
r/R:所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符
5. print("Name %s Age %d"%('ZLY',10)) 6.str="""三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符"""
7.name='zhu liyuan' print(f'Hello{name}');x=2 print (f'{x+1}')
8.Python3中，所有的字符串都是Unicode字符串
9.字符串的内建函数capitalize()
'''
s='you are a good person'
print(dir(s))
print(s.capitalize())

name='zhu liyuan'
print(f'Hello {name}')
x=2
print (f'{x+1}')
print ('qweqw\
sadas\ni\'am a \"boy\"')
print ('s' not in  'start')
print(r'\n')
print(R'\n')
print("Name %s Age %d"%('ZLY',10))
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)



'''1.统计一句话中的单词数量'''
input_words='i amd a n, boys!'
def count_words(input_words):
    new_s=''
    for i in input_words:
        if (i>='a' and i<='z') or (i>'A'and i <'Z'):
            new_s+=i
        else:
            new_s+=' '
    return len(new_s.split())
'''2.字符串统计，判断字符串中字母的个数，以及某个字母的个数和位置'''
def get_letter_num(s,letter):
    num=0
    index=0
    for i in s:
        if i==letter:
            num=num+1
            print('字母位置', index)
        index=index+1
    return num
s='I am a  good boy!'
print('一共有多少单词：%d'%count_words(s))
num=get_letter_num(s,'o')
print(f'一共有字母o个数{num}')

'''3.字符串的反转,数字反转'''
def reverse(number):
    if isinstance(number,int)==False:
        return None
    if number>=0:
        s=str(number)
        reverse_str=s[::-1]
    else:
        s=str(abs(number))
        reverse_str='-'+s[::-1]
    # news=''.join(reverse_list)
    return int(reverse_str)
s='1'
ss='1213'
print('字符反转',ss[::-1])
print('数字反转',reverse(s))
'''python中shell脚本的调用以及执行'''
'''4.二维数组中查找指定数字
5.一个只出现一次的字符，并返回'''

