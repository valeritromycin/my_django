from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from likes_app.services import is_fan
from tags_app.api.serializers.tag import TagSerializer
from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['user', ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )
    tags = TagSerializer(many=True, read_only=True)

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return is_fan(obj, user)

    @extend_schema_field(int)
    def get_likes_count(self, instance) -> int:
        instance.likes.count()