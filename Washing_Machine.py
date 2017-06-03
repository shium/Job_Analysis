#-*- coding:utf-8 -*-

import re

def wash_attribute():
    pass

def wash_description():
    f = open('description.txt', 'r')
    content = f.read()
    f.close()
    wash = re.sub(r'\d\.|\d、|-|邮   箱：.*|公司网站：.*|(|)|（|）|HR 电话：.*', '', content)
    duty1 = re.findall(r'岗位职责：(.*?)任职要求', wash, re.S)
    duty2 = re.findall(r'职位描述：(.*?)[要求\n]+',wash, re.S)
    duty3 = re.findall(r'职位描述：(.*?)希望你',wash, re.S)
    duty4 = duty1 + duty2 + duty3
    duty = []
    for i in duty4:
        i = re.sub(r'熟悉|负责|经验|优先|工作|公司|精通|熟练|业务|客户|岗位职责|岗位要求', '', i)
        duty.append(i)
    f = open('index_des.txt', 'w')
    for i in duty:
        f.write(i)
    f.close()

    
def wash_city():
    f = open('city_money.txt', 'r')
    content = f.read()
    f.close()
    wash1 = re.sub(r'-(.*)\t', '\t', content)
    wash2 = re.sub(r'(.*)\t面议\n', '', wash1)
    f = open('wash_city_money.txt', 'w')
    f.write(wash2)
    f.close()

if __name__ == '__main__':
    wash_description()