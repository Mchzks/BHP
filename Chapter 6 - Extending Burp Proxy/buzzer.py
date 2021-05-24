from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator

from java.util import List, ArrayList

import random

class BurpExtender():
    def registerExtenderCallbacks(IBurpExtender, IIntruderPayloadGeneratorFactory):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        callbacks.registerIntruderPayloadGeneratorFactory(self)

        return
    
    def getGeneratorName(self):
        return "BHP Payload Genrator"

    def createNewInstance(self, attack):
        return BHPFuzzer(self, attack)

class BHPFuzzer(IIntruderPayloadGenerator):
    def __init__(self, extender, attack):
        self._extender = extender
        self._helpers = extender._helpers
        self._attack = attack
        self.max_payloads = 10
        self.num_iterations = 0

        return

    def hasMorePayloads(self):
        if self.num_iterations == self.max_payloads:
            return False
        else:
            return True

    def getNextPayload(self, current_payload):
        # Convert into a string
        payload = "".join(chr(x) for x in current_payload)

        # Call our simple mutator to fuzz the POST
        payload = self.mutate_payload(payload)

        # Increse the number of fuzzing attempts
        self.num_iterations += 1

        return payload

    def reset(self):
        self.num_iterations = 0
        return

    def mutate_payload(self, original_payload):
        # Pick a simple mutator or even call an external script
        picker = random.randint(1,3)

        # Select a random offset in the payload to mutate
        offset = random.randint(0, len(original_payload)-1)

        front, back = original_payload[:offset], original_payload[offset:]

        # Random offset insert a SQL injection attempt
        if picker == 1:
            front += "'"
        elif picker == 2:
            front += "<script>alert('BHP');</script>"
        elif picker == 3:
            chunk_length = random.randint(0, len(back)-1)
            repeater = random.randint(1, 10)
            for _ in range(repeater):
                front += original_payload[:offset + chunk_length]
        
        return front + back