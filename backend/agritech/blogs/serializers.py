# import serializer from rest_framework
from rest_framework import serializers
# import blog model from blogs app
from blogs.models import Blog
from blog_categories.models import BlogCategory

# create a serializer for blogs model
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['categories', 'slug', 'blog_image', 'title', 'blog_author', 'first_paragraph',
         'middle_paragragh', 'final_paragragh', 'country', 'reading_time', 'blog_date', 'updated_at',
          'is_published']

# create a serializer for blog categories model
class BlogCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['name', 'slug', 'blog_category_image', 'created_at', 'updated_at']