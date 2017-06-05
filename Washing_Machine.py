#-*- coding:utf-8 -*-

import re
import csv

def wash_attribute():
    '''
    提取工作经验、学历
    '''
    with open('attribute.txt', 'r') as f:
        content = f.read()
    exp = re.findall(r'经验：(.*)', content)
    formal = re.findall(r'学历：(.*)', content)
    with open('attribute_exp.txt', 'w') as f:
        for i in exp:
            f.write(i+'\n')
    
    with open('attribute_for.txt', 'w') as f:
        for i in formal:
            f.write(i+'\n')

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
        i = re.sub(r'熟悉|负责|经验|优先|工作|公司|精通|熟练|业务|客户|岗位职责|岗位要求|以上|平台', '', i)
        i = re.sub(r'[pP]ython', '', i)
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
    citylist1 = wash2.split('\n')
    citylist2 = []
    for i in citylist1:
        citylist2.append(i.split('\t'))
    print citylist2[0]
    '''
    with open('city_money.csv', 'w') as f:
        w = csv.writer(f)
        for row in citylist2:
            w.writerow([item for item in row])
    '''
def technology():
    f = open('description.txt', 'r')
    content = f.read()
    f.close()
    f = open('technology.txt', 'r')
    tech_str = f.read()
    f.close()
    tech_list = tech_str.split()
    b = {}
    for i in tech_list:
        n = re.findall(i, content, re.I)
        b[i] = len(n)
    f = open('tech_need.txt', 'w')
    for i in b:
        f.write(i+'\t'+str(b[i])+'\n')
    f.close()

if __name__ == '__main__':
    wash_attribute()
    #wash_city()
    #technology()