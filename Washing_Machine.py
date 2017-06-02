#-*- coding:utf-8 -*-

import re

def wash_attribute():
    f = open('attribute.txt', 'r')
    content = f.read()
    f.close()
    content = re.sub(r'地点：|公司.*|经验：|学历：|职位月薪：', '', content)
    content = re.sub(r'\n\n','',content)
    f = open('wash_attr.txt','w')
    f.write(content)
    f.close()

def wash_description():
    f = open('description.txt', 'r')
    content = f.read()
    f.close()
    content = re.sub(r'岗位职责：|任职要求：|\d|\.|、|:|邮   箱：.*|公司网站：.*|(|)|（|）|HR 电话：.*','',content)
    #content = re.findall()

if __name__ == '__main__':
    wash_attribute()    
