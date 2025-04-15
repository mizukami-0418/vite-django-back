from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CalculatorView(APIView):
    def post(self, request):
        try:
            num1 = int(request.data.get('num1'))
            num2 = int(request.data.get('num2'))
            operator = request.data.get('operator')
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return Response({"error": "0で割ることはできません"}, status=status.HTTP_400_BAD_REQUEST)
                result = round(num1 / num2, 2)
            else:
                return Response({"error": "無効な演算子"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"result": result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)