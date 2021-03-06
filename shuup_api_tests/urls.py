# -*- coding: utf-8 -*-
# This file is part of Shuup API.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/', include('shuup_api.urls', namespace=settings.SHUUP_API_URLS_NAMESPACE)),
    url(r'^sa/', include('shuup.admin.urls', namespace="shuup_admin")),
]
