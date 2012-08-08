"""
Copyright (c) 2012 Enrique Samson Jr. <enriquejr at gmail dot com>

Distributed under the MIT License (See accompanying LICENSE.txt)


Application Terms of Service page.
"""

from twisted.web.resource import Resource

class Tos(Resource):
    isLeaf = True

    def render_GET(self, request):
        return "Coming soon..."
