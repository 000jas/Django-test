import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import utils
from django.shortcuts import render
def home(request):
    return render(request, 'signer/index.html')
class SignMessageView(APIView):
    def post(self, request):
        message = request.data.get('message')
        if not message:
            return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)

        signature = utils.sign_message(message.encode())
        return Response({'signature': base64.b64encode(signature).decode()})

class VerifyMessageView(APIView):
    def post(self, request):
        message = request.data.get('message')
        signature_b64 = request.data.get('signature')

        if not message or not signature_b64:
            return Response({'error': 'Message and signature are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            signature = base64.b64decode(signature_b64)
        except Exception:
            return Response({'error': 'Invalid signature format'}, status=status.HTTP_400_BAD_REQUEST)

        valid = utils.verify_signature(message.encode(), signature)
        return Response({'valid': valid})
