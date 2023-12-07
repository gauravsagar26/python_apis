from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserPost

# Create your views here.


class UserInfoView(APIView):

    def post(self, request):

        data = request.data
        user_id = data["user_id"]
        UserPost.objects.create(user_id=user_id, content=data["content"])
        return Response({
            "status": "200",
            "message": "created the post",
            "data": "----"
        })



class UserGetCount(APIView):

    def get(self, request, id):
        # user_id = get_user_id(request.headers)
        user_info = UserPost.objects.filter(user_id=1, post_id=id)
        if user_info.exists():
            user_info = user_info.last()
            content = user_info.content
            word_count = 0
            letters_count = 0
            for c in content:
                if c == " ":
                    word_count += 1
                else:
                    letters_count += 1
            average_word_lenth = letters_count/word_count
        return Response({
            "status": "200",
            "message": "success",
            "data": {"word_count": word_count, "average_word_length": average_word_lenth},
        })
    



    # {
    #     "user_id": 10,
    #     "content": "My name is Gaurav . I am 10 years old"
    # }
