# Try pyee, a Python Event Emitter

import time

from pyee.base import EventEmitter

ee = EventEmitter()

@ee.on("event")
def event_handler(*args, **kwargs):
    print("Event fired!")

for _ in range(10):
    ee.emit("event")
    time.sleep(1)
