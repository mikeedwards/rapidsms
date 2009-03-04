#!/usr/bin/env python2.4
# vim: ai ts=4 sts=4 et sw=4

import unittest
import rapidsms
import sys, urllib2, time
sys.path.append("../..")
import apps.alpha.app,apps.beta.app

class TestApps(unittest.TestCase):
    
    def setUp(self):
        self.router = rapidsms.Router()
        self.spomsky_backend = rapidsms.backends.Spomsky(self.router)
        self.router.add_backend(self.spomsky_backend)
   
    def tearDown(self):
        pass
    
    def test_dispatches_messages_to_alpha(self):
        self.http_backend = rapidsms.backends.Http(self.router,"localhost",8000)
        self.router.add_backend(self.http_backend)

        app_alpha = apps.alpha.app.App()
        
        self.router.add_app(app_alpha)
        
        app_alpha.status = "idle"
        
        urllib2.urlopen("http://127.0.0.1:8000/567890/testMessage1")
        time.sleep(.01)
        
        self.assertEqual(app_alpha.status,"responded","Alpha app did not respond to HTTP")
        
        app_alpha.status = "idle"
        self.spomsky_backend.receive("1234", "Test Message2")
        self.assertEqual(app_alpha.status,"responded","Alpha app did not respond to Spomsky")
          
    def test_dispatches_messages_to_beta(self):
        self.http_backend = rapidsms.backends.Http(self.router,"localhost",8001)
        self.router.add_backend(self.http_backend)

        app_beta = apps.beta.app.App()

        self.router.add_app(app_beta)
        
        app_beta.status = "idle"

        urllib2.urlopen("http://127.0.0.1:8001/123456/testMessage3")
        time.sleep(.01)

        self.assertEqual(app_beta.status,"responded","Beta app did not respond to HTTP")
        
        app_beta.status = "idle"
        self.spomsky_backend.receive("1234", "Test Message4")
        self.assertEqual(app_beta.status,"responded","Beta app did not respond to Spomsky")

if __name__ == "__main__":
    unittest.main()
