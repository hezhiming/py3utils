# py3utils: Useful Python 3 utils

Some useful Python 3 utils.

## Getting Started

### Prerequisites

* pip install python-dateutil

### Installing
1. pip install py3utils

## Docs
* datetimeutil
```python
from py3utils import TimeUtils

if __name__ == '__main__':
    print(TimeUtils.current_timestamp())
    print(TimeUtils.current_timestamp_ms())
    print(TimeUtils.current_utc_datetime())
    print(TimeUtils.current_local_datetime())

    now_timestamp = TimeUtils.current_timestamp()
    print(TimeUtils.timestamp2str(now_timestamp, timezone=tz.tzlocal()))  # from dateutil import tz
    print(TimeUtils.timestamp2datetime(now_timestamp, timezone=tz.tzutc()))

    now_local_dt = TimeUtils.current_local_datetime()
    print(TimeUtils.datetime2str(now_local_dt))

    utc_dt = TimeUtils.current_utc_datetime()
    print(TimeUtils.convert_datetime(utc_dt, timezone=tz.tzlocal(), offset_seconds=8 * 3600)) # UTC --> China


    # 1492352448
    # 1492352448964
    # 2017-04-16 14:20:48.964633+00:00
    # 2017-04-16 22:20:48.965634+08:00
    # 2017/04/16 22:20:48
    # 2017-04-16 14:20:48+00:00
    # 2017/04/16 22:20:48
    # 2017-04-16 22:20:48.965634+08:00
```

* urlutil
```python
from py3utils import Url


if __name__ == '__main__':
    url = Url('https://www.baidu.com/path/to/here?q1=v1&q2=v2#frag')
    print(url.scheme)
    print(url.netloc)
    print(url.path)
    print(url.query)
    print(url.fragment)

    print(Url.decode_query(url.query))  # decode query to Python object
    print(Url.encode_query({'q1': 'v1', 'q2': 'v2'}))
    print(Url.quote_str('unsafe str {};;; **&&'))


    # https
    # www.baidu.com
    # /path/to/here
    # q1=v1&q2=v2
    # frag
    # [('q1', 'v1'), ('q2', 'v2')]
    # q1=v1&q2=v2
    # unsafe%20str%20%7B%7D%3B%3B%3B%20%2A%2A%26%26
```

## License
MIT

