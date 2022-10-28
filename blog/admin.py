from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('author_name',)


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", 'get_image')
    list_filter = ('title', 'pub_date')
    search_fields = ('title',)
    inlines = [CommentInline]
    save_on_top = True
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="150" height="150">')

    get_image.short_description = 'Изображение'

    class Meta:
        model = Article


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('article', 'pub_date', 'author_name', 'comment_text')
    list_filter = ('article', 'author_name')
    search_fields = ('article', 'author_name')
    readonly_fields = ('article', 'author_name')


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
