from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from snippets.models import Snippet, Comment
from snippets.forms import SnippetForm, CommentForm
from django.contrib.auth.decorators import login_required


def top(request):
    snippets = Snippet.objects.all() #Snippetの一覧を取得
    context = {"snippets": snippets} #テンプレートへ与えるオブジェクト
    return render(request, "snippets/top.html", context)



@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, "snippets/snippet_new.html", {'form': form})





@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpRespnseForbidden("このスニペットの編集は許可されていません")

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippet_detail', snippet_id=snippet_id)

    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})





@login_required
def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    comment_list = Comment.objects.filter(commented_to=snippet_id).all()
    comment_form = CommentForm()
    return render(request, 'snippets/snippet_detail.html', {
        'snippet': snippet,
        'comment_list': comment_list,
        'comment_form': comment_form,
        })


@login_required
def comment_new(request, snippet_id):
    if request.method == 'POST':
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commented_to = snippet
            comment.commented_by = request.user
            comment.save()
            messages.add_message(request, messages.SUCCESS, "コメントの投稿に成功しました。")
    else:
        messages.add_message(request, messages.ERROR, "コメントの投稿に失敗しました。")
    return redirect("snippet_detail", snippet_id=snippet_id)


