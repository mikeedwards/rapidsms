#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import time

class Router:
    def __init__(self):
        self.backends = []
        self.apps = []

    def add_app(self, app):
        self.apps.append(app)

    def add_backend(self, backend):
        self.backends.append(backend)

    def serve_forever(self):
        # dump some debug info for now
        print "BACKENDS: %r" % (self.backends)
        print "APPS: %r" % (self.apps)
        print "SERVING FOREVER..."

        # block forever! TODO: replace this
        # with a thread for each backend
        while(True):
            time.sleep(1)

    def dispatch_incoming(self, message):                            
        for app in self.apps:                                        
            try:
                print "DISPATCHED INCOMING %s to %s" % (message, app)
                app.incoming(message)                                
            except AttributeError:                                        
                pass                                                 
    
    def dispatch_outgoing(self, message):                                         
        try:
            print "DISPATCHED OUTGOING %s to %s" % (message, message.backend)
            message.backend.send(message)                                
        except AttributeError:                                        
            pass
        