from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    posts = Post.objects.all()  # Получаем все посты

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)

        # Получаем комментарий из формы
        new_comment = request.POST.get('comments')

        if new_comment:
            # Добавляем комментарий в поле comments
            if post.comments:
                post.comments += f"\n{request.user.username}: {new_comment}"
            else:
                post.comments = f"{request.user.username}: {new_comment}"
            post.save()  # Сохраняем пост с новым комментарием

        return redirect('forum:index')  # Перенаправляем на ту же страницу после добавления комментария

    return render(request, 'forum/index.html', {'posts': posts})

def register(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            if request.POST["login"]:
                context = {'login': request.POST["login"]}
                return render(request, 'forum/register.html', context)
    return redirect('forum:index')

def auth(request):
    if request.method=="POST":
        if not request.user.is_authenticated and request.POST["login"] and request.POST["password"]:
            # Поиск пользователя по данным, введенным в форму
            print(request.POST["password"])
            user = authenticate(request, username=request.POST["login"], password=request.POST["password"])
            # если пользователь был найден, то
            if user is not None:
                # вызываем метод login с аргументами request и объектом пользователя
                login(request, user)
                # перенаправляем на страницу профиля
                return redirect('forum:profile')
            else:
                # если пользователь не был найден, но указанный логин существует в базе
                if User.objects.filter(username=request.POST["login"]).exists():
                    # формируем контекст с ошибкой
                    context = {'login': request.POST["login"], 'error_message': 'пароль неверный! попробуйте ещё раз'}
                    # рендерим страницу регистрации с новым контекстом
                    return render(request, 'forum/register.html', context)
                else:
                    # если пользователь не был найден и его профиля не существует, то
                    # создаем новый объект пользователя
                    user = User.objects.create_user(username=request.POST["login"], email='', password=request.POST["password"])
                    # сохраняем нвоый объект в базе
                    user.save()
                    # разрешаем пользователю войти в систему
                    login(request, user)
                    # перенаправляем на страницу профиля
                    return redirect('forum:profile')
        else:
            return redirect('forum:register')
    else:
        return redirect('forum:index')

def _logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('forum:index')

def profile(request):
    return render(request, 'forum/profile.html')