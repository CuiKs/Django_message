from django.shortcuts import render

from .models import UserMessage


# Create your views here.

def get_form(request):
    # 查找数据
    # all_messages = UserMessage.objects.all()
    # all_messages = UserMessage.objects.filter(name='张三', address='上海')
    # # 删除
    # # 删除去全部
    # all_messages.delete()
    # for message in all_messages:
    # 删除单条
    #     message.delete()
    #     print(message.name)

    # 前端输入添加数据
    # if request.method == 'POST':
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message', '')
    #     email = request.POST.get('email', '')
    #     address = request.POST.get('address', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.object_id = '1'
    #     user_message.message = message
    #     user_message.email = email
    #     user_message.address = address
    #     user_message.save()
    # return render(request, 'message_form.html')

    # 根据用户名展示数据
    if request.method == 'POST':
        request_name = request.POST.get('name')
        all_message = UserMessage.objects.filter(name=request_name)
        message = None
        if all_message:
            message = all_message[0]

        return render(request, 'message_form.html', {'return_message': message})

    return render(request, 'message_form.html')
