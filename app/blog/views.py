import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from blog.models import Post


def post_list(request):
    """
        first/
            first_file.txt
            second/
                second_file.txt
                third/
                    module.py
                    fourth/
                        fourth_file.txt
        module.py에서
        0. 현재 경로
            os.path.abspath(__file__)
        1. third/ 폴더의 경로
            os.path.dirname(<현재경로>)
        1-1. second/ 폴더의 경로
            os.path.dirname(<third폴더의 경로>)
        2. second/second_file.txt의 경로
            os.path.join(<second폴더의 경로>, 'second_file.txt')
        3. fourth/ 폴더의 경로
            os.path.join(<현재경로>, 'fourth')
        4. fourth/fourth_file.txt의 경로
            os.path.join(<현재경로>, 'fourth', 'fourth_file.txt')
        :param request:
        :return:
        """
    # cur_file_path = os.path.abspath(__file__)
    # blog_dir_path = os.path.dirname(cur_file_path)
    # app_dir_path = os.path.dirname(blog_dir_path)
    # templates_dir_path = os.path.join(app_dir_path, 'templates')
    # blog_template_file_path = os.path.join(templates_dir_path, 'blog', 'post_list.html')
    # print(blog_template_file_path)
    # html = open(blog_template_file_path, 'rt').read()

    # html = render_to_string('blog/post_list.html')
    # return HttpResponse(html)
    posts1 = Post.objects.all()
    context = {
        'posts': posts1,
    }
    return render(request, 'blog/post_list.html', context)
    #
    # result = '글 목록<br>'
    # for post in Post.objects.all():
    #     result += '{}<br>'.format(post.title)
    # return HttpResponse(result)
    # posts = Post.objects.all()
    # print(posts)
