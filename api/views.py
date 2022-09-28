

from rest_framework.response import Response

from .models import Agent
from .serializers import  AgentSerializer

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class AgentView(APIView):

    @api_view(['GET','POST'])

    def agent_list(request):
        if request.method == "GET":
            agents = Agent.objects.all()
            serializer = AgentSerializer(agents,many=True)
            return Response(serializer.data)
        
        if request.method == "POST":
            serializer = AgentSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['GET','PUT','DELETE'])

    def edit_agent(request,id):
            try:
                agent = Agent.objects.get(pk = id)
            except Agent.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND,template_name="<html>hello</html>",data="The Data you are looking for its not present.")


            if request.method =="GET":
                serializer = AgentSerializer(agent)
                return Response(serializer.data)

            if request.method == "DELETE":
                if request.user.is_staff:
                    agent.delete()
                    return Response(status=status.HTTP_200_OK,data="Deleted!")
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST,data="Permission denied!")

            if request.method == "PUT":
                serializer = AgentSerializer(agent,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                    
class AgentList(ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["mobile"]

