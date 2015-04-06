# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Todo
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json


def index(request):
    return render_to_response('mytodo/index.html', {})


'''
public
@desc 控制创建和读取方法的一个跳转
@param
@return
'''


def control_cr(request):
    if request.method == 'POST':
        return create(request)
    elif request.method == 'GET':
        return get_all(request)
    else:
        return HttpResponse('<h1>access deny</h1>')


'''
public
@desc 控制更新和删除方法的一个跳转
@param  url中的todo对象id
@return
'''


def control_ud(request, todo_id):
    if request.method == 'PUT':
        return update(request, todo_id)
    elif request.method == 'DELETE':
        return delete(request, todo_id)
    else:
        return HttpResponse('<h1>access deny</h1>')


'''
protect
@desc  获取所有的todo对象，并转为json格式，返回
@param
@return  json格式的todo列表
'''


def get_all(request):
    todos = Todo.objects.all()
    todo_dict = []
    flag_dict = {'Y': True, 'N': False}
    for todo in todos:
        todo_dict.append({'id': todo.id, 'title': todo.title, 'done': flag_dict[todo.done], 'order': todo.order})
    return HttpResponse(json.dumps(todo_dict), content_type='application/json')


'''
protect
@desc  创建一个todo记录
@param  POST中的json格式todo对象
@return  json格式{'success':True/False}
'''


def create(request):
    req = json.loads(request.body)
    title = req['title']
    content = req['content']
    order = req['order']

    if not title:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.order = order
    todo.save()
    return HttpResponse(json.dumps({'success': True}), content_type='application/json')


'''
protect
@desc  更新一条todo记录
@param  POST中的json格式todo对象
@return  json格式{'success':True/False}
'''


def update(request, todo_id):
    req = json.loads(request.body)
    title = req['title']
    done = req['done']
    order = req['order']
    flag_dict = {True: 'Y', False: 'N'}
    todo = Todo.objects.get(id=todo_id)
    todo.title = title
    todo.done = flag_dict[done]
    todo.order = order
    todo.save()
    return HttpResponse(json.dumps({'success': True}), content_type='application/json')


'''
protect
@desc  删除一条todo记录
@param  url中的todo对象id
@return  json格式{'success':True/False}
'''


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponse(json.dumps({'success': True}), content_type='application/json')
