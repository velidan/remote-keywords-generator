"""
A middleware to adds a CORS header to each response
"""

class CORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        res = self.get_response(request)

        # avoiding the CORS problem
        res["Access-Control-Allow-Origin"] = "*"
        return res