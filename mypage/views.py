from django.http import HttpResponse

def index(request):
    return HttpResponse("마이 페이지 작업중입니다.")