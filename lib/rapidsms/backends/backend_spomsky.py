#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from backend_base import Base
from rapidsms.message import Message
import spomsky


class Spomsky(Base):
    
    def __init__(self, router, host="localhost", port="8100"):
        self.client = spomsky.Client(host, port)
        self.router = router

    def start(self):
        #bare minimum to pass test
        pass

    def stop(self):
        #bare minimum to pass test
        pass

    def send(self,message):
        print "Spomsky Message \"%s\" sent to \"%s\"" % (message.text, message.caller)

    def receive(self, caller, text):
        # turn the caller/text into a message object
        msg = Message(self, caller, text)
        # and send it off to the router
        self.router.dispatch_incoming(msg)
