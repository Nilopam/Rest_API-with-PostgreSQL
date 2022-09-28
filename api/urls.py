from django.urls import path
from .views import  AgentList, AgentView 



urlpatterns = [
    path('agents',AgentView.agent_list,name="agent_list"),
    path('agents/<int:id>',AgentView.edit_agent,name="agent_list"),
    path('agents/', AgentList.as_view(), name='agent_list'),

    
]