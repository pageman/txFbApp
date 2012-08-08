"""
Copyright (c) 2012 Enrique Samson Jr. <enriquejr at gmail dot com>

Distributed under the MIT License (See accompanying LICENSE.txt)


Application Privacy page.
"""

from twisted.web.resource import Resource

class Privacy(Resource):
    isLeaf = True

    def render_GET(self, request):
        return "Coming soon..."
