from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from . import serializers
from . import models


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Posts to be viewed """
    queryset = models.BoastsRoastsModel.objects.all()
    serializer_class = serializers.PostSerializer

    @action(detail=False)
    def boasts(self,request,pk=None):
        all_boasts = models.BoastsRoastsModel.objects.filter(isboast=True).order_by('-date_created') 
        serializer = self.get_serializer(all_boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self,request,pk=None):
        all_roasts = models.BoastsRoastsModel.objects.filter(isboast=False).order_by('-date_created') 
        print(all_roasts)
        serializer = self.get_serializer(all_roasts, many=True)
        return Response(serializer.data)

    @action(detail=True,methods=['put'])
    def upvote(self,request, pk=None):
        post = models.BoastsRoastsModel.objects.get(id=pk)          
        post.post_upvote = post.post_upvote + 1
        post.save()    
        return Response({'status': 'upvote increamented'})


    @action(detail=True,methods=['put'])
    def downvote(self,request ,pk=None):
        post = models.BoastsRoastsModel.objects.get(id=pk)              
        post.post_downvote = post.post_downvote - 1
        post.save()    
        return Response({'status': 'donvote increamented'})


  