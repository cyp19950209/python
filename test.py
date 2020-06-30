from django.utils.deprecation import MiddlewareMixin
import json

class MyMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.POST:
            request.data=request.POST.copy()
            for k,v in request.FILES.items():
                request.data[k]=v

        elif request.body:
            json_byte=request.body
            json_data=json.loads(json_byte)
            request.data=json_data
        else:
            request.data={}
        print(request.data)
