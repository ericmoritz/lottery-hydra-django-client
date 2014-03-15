from django.conf.urls import patterns, url, include
from django.conf import settings
from lottery_hydra.views import resource
import os

urlpatterns = patterns(
    '',
    url(
        r'lottery/(.*)', resource,

        kwargs={'cfg_irl': os.environ['CONFIG_IRL']}
    )
)
