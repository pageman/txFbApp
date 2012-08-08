"""
Copyright (c) 2012 Enrique Samson Jr. <enriquejr at gmail dot com>

Distributed under the MIT License (See accompanying LICENSE.txt)


Application Root page.
"""

from twisted.web.resource import Resource, NoResource
import privacy, tos

class Facebook(Resource):

    def getChild(self, name, request):
        res = None
        if name == '':
            res = self
        elif name == 'tos':
            res = tos.Tos()
        elif name == 'privacy':
            res = privacy.Privacy()
        else:
            res = NoResource()
        return res

    def render_GET(self, request):
        return 'Welcome to My FB App!'
