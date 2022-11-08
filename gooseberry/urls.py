from django.conf.urls import *

import gooseberry.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'gooseberry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', gooseberry.views.home),
        url(r'^md/$', gooseberry.views.render_md_blog),
	url(r'^blog/$', gooseberry.views.blog_base), 
	url(r'^base/$', gooseberry.views.simple_page('base.html')), 
	url(r'^resume/$', gooseberry.views.simple_page('resume.html')), 
	url(r'^portfolio/$', gooseberry.views.simple_page('portfolio.html')), 
	url(r'^address/$', gooseberry.views.simple_page('address.html')), 
	url(r'^blog/(.*)$', gooseberry.views.blog), 
	url(r'^test/$', gooseberry.views.test), 
	url(r'^jammer/$', gooseberry.views.jammer), 
	url(r'^.well-known/acme-challenge/p_LTkY9QHhcECb6Lv1UZWYQ6rawjuQLnUAdBdZZE9kk', gooseberry.views.file_a),
	url(r'^.well-known/acme-challenge/v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA', gooseberry.views.file_b),


	url(r'^messages/whatyouwant$', gooseberry.views.simple_page('messages/isthiswhatyouwant.html')), 




]
