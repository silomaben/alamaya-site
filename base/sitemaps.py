from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home','blog','view_destinations','view_destinations','booking','about-us','contact-us','gallery','blog','package_1_maasaimara','package_2_hidden_gems','package_3_magical_kenya']
    
    def location(self,item):
        return reverse(item)
    

class BlogPostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()