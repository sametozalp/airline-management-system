from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(ex, context):
    response = exception_handler(exc=ex, context=context)
    if response is not None:
        return Response({
            "success": False,
            "message": response.data.message if 'detail' in response.data else response.data,
        }, status=response.status_code)
    
    return Response({
            "success": False,
            "message": "An error occured",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)