from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from django.utils import timezone
from .forms import CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def list(request):
    """
    product(game)목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    game_list = Game.objects.order_by('posted_date')

    # 페이징 처리
    paginator = Paginator(game_list, 20)  # 페이지당 n개
    page_obj = paginator.get_page(page)

    context = {'game_list': page_obj}
    return render(request, 'product/game_list.html', context)


def detail(request, game_id):
    """
    product(game) 내용 출력
    """
    game = get_object_or_404(Game, pk=game_id)
    context = {'game': game}
    return render(request, 'product/game_detail.html', context)


@login_required(login_url='users:login')
def comment_create(request, game_id):
    """
    product(game) 댓글 등록
    """
    game = get_object_or_404(Game, pk=game_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.posted_date = timezone.now()
            comment.game = game
            comment.save()
            return redirect('product:detail', game_id=game.id)
    else:
        form = CommentForm()

    context = {'game': game, 'form': form}
    return render(request, 'product/game_detail.html', context)
