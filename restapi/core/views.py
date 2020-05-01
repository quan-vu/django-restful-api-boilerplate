from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PingView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'pong': datetime.now()}
        return Response(content)