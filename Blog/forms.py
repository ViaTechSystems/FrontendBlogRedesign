from django import forms

from Blog.models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    # this is the form used to create a blog post.
    # it is a model form so there are no fields declared
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
        ]


class CommentForm(forms.ModelForm):
    # this is the form used to create a comment.
    # it is a model form so there are no fields declared
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
