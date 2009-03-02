#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import rapidsms
import gettext
import locale
gettext.bindtextdomain("betarsms", None)
locale.setlocale(locale.LC_ALL, None)
gettext.textdomain("betarsms")
_ = gettext.gettext

# another pointless app
class App(rapidsms.app.Base):

    def incoming(self, message):
        message.respond(_("Beta!"))
        #added the following line to test that this fired
        self.status = "responded"
