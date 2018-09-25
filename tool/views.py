from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

test_data = [['他', '代词', '3', '定中关系'], ['的', '助词', '1', '右附加关系'], ['精神', '名词', '4', '主谓关系'],
             ['值得', '动词', '0', '核心关系'], ['我们', '代词', '7', '主谓关系'], ['好好', '副词', '7', '状中结构'],
             ['学习', '动词', '4', '动宾关系']]


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def initialize(request):
    data_dic = dict()
    temp_dic = dict()
    data_list = list()
    item_dic = dict()
    index = 0

    for index in range(len(test_data)):
        if test_data[index][2] not in data_dic.keys():
            data_dic[test_data[index][2]] = list()
            data_dic[test_data[index][2]].append(test_data[index])
        else:
            data_dic[test_data[index][2]].append(test_data[index])

    for index in range(len(test_data)):
        temp_dic['name'] = test_data[index]
        temp_dic['children'] = list()
        if str(index + 1) in data_dic.keys():
            for item in data_dic[str(index + 1)]:
                item_dic['name'] = item
                temp_dic['children'].append(item_dic.copy())
                item_dic.clear()
        data_list.append(temp_dic.copy())
        temp_dic.clear()

    for i in range(len(data_list)):
        if data_list[i]['name'][2] == '0':
            index = i

    for data in data_list:
        data['name'] = data['name'][0] + "(" + data['name'][3] + ")"
        for children in data['children']:
            children['name'] = children['name'][0] + "(" + children['name'][3] + ")"

    for i in range(len(data_list)):
        data_name = data_list[i]['name']
        for j in range(len(data_list)):
            data_children = data_list[j]['children']
            for k in range(len(data_children)):
                if data_name == data_children[k]['name']:
                    data_list[j]['children'][k] = data_list[i]

    return_data = data_list[index]
    print(return_data)



initialize('123')
