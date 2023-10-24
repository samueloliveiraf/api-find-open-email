from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.email_find.models import EmailFind


@api_view(['POST'])
def update_open_email(request, email_id):
    if request.method != 'POST':
        return Response({'detail': 'Método não permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not email_id:
        return Response({'detail': 'ID não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        email_obj = EmailFind.objects.filter(id=email_id)

        if not email_obj.exists():
            return Response({'detail': 'E-mail não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        email_obj.update(open_email=True)

        return Response({'detail': 'E-mail atualizado com sucesso.'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
