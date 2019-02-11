from django.shortcuts import render

# Create your views here.

from main.models import JdFirstCate


def index(request):
    first_cates = JdFirstCate.objects.all()
    for first_cate in first_cates:
        second_cate_list = first_cate.jdsecondcate_set.all()
        first_cate.second_cates = second_cate_list
        for second_cate in first_cate.second_cates:
            third_cate_list = second_cate.jdthirdcate_set.all()
            second_cate.third_cates = third_cate_list

    context = {
        'first_cates': first_cates,
    }
    return render(request, 'index.html', context)