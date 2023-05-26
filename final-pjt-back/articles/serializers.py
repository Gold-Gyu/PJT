from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    # author2 = serializers.CharField(source='author', read_only=True)
    class Meta:
        model = Article
        
        fields = ('id', 'title', 'content', 'user_id', 'user_username', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = ('id','content','user_id', 'user_username','created_at',)


# class ArticleSerializer(serializers.ModelSerializer):
#     comment_set = CommentSerializer(many=True, read_only=True) # read_only는 유효성검사에는 들어가지 않고 오직 읽을 때만 사용
#     comment_count = serializers.IntegerField(
#         source='comment_set.count', 
#         read_only=True
#     )
#     def getUsername(self, obj):
#         return obj.user.username
        
#     username = serializers.SerializerMethodField("getUsername")

#     class Meta:
#         model = Article
#         fields = ('id','title','username','content','comment_count','comment_set','created_at',)
#         depth = 1







