import json
import time
import datetime
from SOAPpy.Types import structType


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return time.mktime(obj.timetuple())
        if isinstance(obj, structType):
            obj = obj._asdict()
            return obj
        return json.JSONEncoder.default(self, obj)


def emit(payload, ok):
    return json.dumps({
        "data": payload,
        "ok": ok
    }, sort_keys=True, indent=4, cls=JSONEncoder)
