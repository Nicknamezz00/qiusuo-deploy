from rest_framework import serializers

from subjects.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(
        required=False,
        queryset=Subject.objects.all(),
        slug_field='cate_name',
        error_messages={"blank": "请输入父学科名", "required": "请输入父学科名"},
        help_text="父学科名")

    childs = serializers.SerializerMethodField()

    def get_childs(self, obj):
        all_childs = Subject.objects.filter(parent__cate_name=obj.cate_name)
        childs_ser = SubjectSerializer(all_childs, many=True)
        return childs_ser.data

    def validate(self, attrs):
        cate_name = attrs.get('cate_name')
        level = attrs.get('level')

        if level == 0:
            return attrs

        if not cate_name:
            raise serializers.ValidationError("类别不能为空!")

        # 只有最高层级学科不存在父学科
        parent = attrs.get('parent')
        if not parent:
            raise serializers.ValidationError("父学科不存在!")

        # 当前学科的层级只能比父学科低一级
        if not level == parent.level + 1:
            raise serializers.ValidationError("层级不合法!")

        return attrs

    class Meta:
        model = Subject
        depth = 3
        fields = ['id', 'level', 'cate_name', 'parent', 'childs']

