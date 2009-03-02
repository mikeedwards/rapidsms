#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import rapidsms

# a pointless app to demonstrate the structure
# of sms applications without magic decorators
class App(rapidsms.app.Base):

    def incoming(self, message):
        message.respond("Alpha!")
        #added the following line to test that this fired
        self.status = "responded"
