from django.conf.urls import url

from blog.views import post_list

urlpatterns = [
    # url의 첫번째 인자: 매치될 url 정규표현식
    # url의 두번째 인자: view function
    #     view function
    #         -> request를받아서 response를 돌려준다
    #
    # blog.view에 있는 post_list함수를
    # 아래 url함수의 두번째 인자로 전달(함수 호출아님)
    url(r'^$', post_list),
]
