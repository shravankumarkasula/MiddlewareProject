class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        print("init() is executed only once..!!")
        self.get_response = get_response

    def __call__(self, request):
        print('This line added at pre-processing of request')
        response = self.get_response(request)
        print('This line added at post-processing of request')
        return response


from django.http import HttpResponse


class AppMaintananceMiddleware(object):
    def __init__(self, get_response):
        print("init() method is called...");
        self.get_response = get_response

    def __call__(self, request):
        return HttpResponse('<h1>IAM UNDER REBOOT8am KI RA RA PUKA ..!!</h1><hr />')


from django.http import HttpResponse


class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        print("init() is called for error-app");
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        print("Server is printing exception")
        return HttpResponse(
            '<h1> CHUSUKONI TYPE CHAYARA PUKA!!!</h1><hr />')


class FirstMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('This line printed by FirstMiddleware at pre-processing of request');
        response = self.get_response(request)
        print('This line printed by FirstMiddleware at post-processing of request')
        return response;


class SecondMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('This line printed by SecondMiddleware at pre-processing of request')
        response = self.get_response(request)
        print('This line printed by SecondMiddleware at post-processing of request')
        return response
