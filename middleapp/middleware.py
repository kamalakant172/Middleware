# from django.shortcuts import HttpResponse
from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse as render


class my_middleware:
    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):
        response= self.get_response(request)   
    
        # print(request.method)
        # print(request.META)

        # return HttpResponse(response1)
        # print(request.headers)
        
        return response
    def process_template_response(self, request, response):
        response.context_data['Meta']= request.META
        response.context_data['Headers']= request.headers
        response.context_data['Method']= request.method
        return response

        

# def my_middleware(get_response):
#     # print("middleware")



#     def my_function(request):
#         # print("before viewcall")
#         # print(request.headers)
        
 


#         response = get_response(request)
#         # print("after viewcall")
#         # print(response.headers)
#         print(request.META)
        
        
        
#         return response
#     return my_function