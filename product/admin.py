from django.contrib import admin
from .models import Game, Tag


# Tag 클래스를 inline 으로 나타냄
class TagInline(admin.TabularInline):
    model = Tag


class GameAdmin(admin.ModelAdmin):
    search_fields = ['title']
    # Game 클래스는 해당하는 Image 객체를 리스트로 관리함
    inlines = [TagInline, ]
    list_display = ['title', 'price']


admin.site.register(Game, GameAdmin)
