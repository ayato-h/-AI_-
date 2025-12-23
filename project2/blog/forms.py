from django import forms
from .models import Post  # Postモデルをインポート

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # モデルとしてPostを使用
        fields = ['title', 'content']  # フォームで表示するフィールド
