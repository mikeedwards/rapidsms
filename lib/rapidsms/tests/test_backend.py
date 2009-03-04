#!/usr/bin/env python2.4
# vim: ai ts=4 sts=4 et sw=4

import unittest
import rapidsms.backends


class MockRouter(object):
    def __init__(self):
        self.messages = []
    
    def dispatch_incoming(self, message):   
        self.messages.append(message)
    
    def dispatch_outgoing(self, message):   
        pass

class TestBackend(unittest.TestCase):

    REQUIRED_METHODS = ("start", "stop", "send", "receive")

    def setUp(self):
        self.mock_router = MockRouter()
        self.backend = rapidsms.backends.Spomsky(self.mock_router)
    
    def tearDown(self):
        pass
    
    def test_api(self):
        for m in self.REQUIRED_METHODS:
            has_method = hasattr(self.backend, m)
            self.assertTrue(has_method, "Missing method: %s" % (m))

    def test_notifies_router(self):
        n = len(self.mock_router.messages)
        self.backend.receive("1234", "Test Message")
        self.assertTrue(len(self.mock_router.messages) > n,
            "The backend didn't notify its router of an incoming message")
        self.assertEqual(self.mock_router.messages[-1].text,"Test Message",
            "The incoming message received is incorrect")
    
    # things to test:
    #   sending messages (without *really* doing it)
    #   arity of api methods (use inspect.getargspec)
    #   individual tests for required API methods


if __name__ == "__main__":
    unittest.main()
