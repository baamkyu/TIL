from django.shortcuts import render, redirect

from todos.models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def new(request):
    if request.method == 'POST':
        todoform = TodoForm(request.POST)
        if todoform.is_valid():
            todo = todoform.save(commit=False)      # todo안에 author는 포함X
            todo.author = request.user              # 포함 시켜주고
            todo.save()                             # 같이 저장
            return redirect('todos:index')
        
    else:
        todoform = TodoForm()
    context = {             # POST가 아니거나 유효성 검사 통과 못하면 여기로 옴
        'todoform': todoform
    }
    return render(request, 'todos/new.html', context)
