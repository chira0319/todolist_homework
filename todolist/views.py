from django.shortcuts import render, redirect
from .models import Todo #匯入 資料庫
from django.utils import timezone  # 匯入 時間物件


# Create your views here.

# def index(request):
#     wanttodo = request.GET.get('wanttodo') # 用來接網頁表單的變數
#     if wanttodo is "":
#         Todo.objects.create(todo="Some task", completed=False)
#     else:
#         Todo.objects.create(
#             todo = wanttodo)
        
def index(request):
    if request.method == 'POST':
        todo_text = request.POST.get('wanttodo', '')  # 使用 POST 方法來獲取表單數據
        if todo_text:  # 確認 'wanttodo' 不是空的
            Todo.objects.create(
                todo=todo_text,
                completed=False,
                last_update=timezone.now()  # 設定 last_update 為當前時間
            )
        return redirect('urls_app_todo:urls_path_index')  # 重定向到主頁面
    else:
        views_todolist = Todo.objects.all()
        return render(request, 'index.html', {'views_for_html_list': views_todolist})
    # return render(request, 'todolist/index.html', {'views_for_html_list': views_todolist})


def delete(request, id):
    todo_in_one = Todo.objects.get(todo_id=id)  
    todo_in_one.delete()
    return redirect('urls_app_todo:urls_path_index') # 刪除完成後轉跳

def toggle_completed(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(todo_id=id)
        todo.completed = not todo.completed
        todo.last_update = timezone.now()  # 每次更新完成狀態時，同時更新 last_update
        todo.save()
    return redirect('urls_app_todo:urls_path_index')