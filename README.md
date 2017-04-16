# py3utils: Useful Python 3 utils
 
Some useful Python 3 utils.
 
## Getting Started
 
### Prerequisites
 
* pip install python-dateutil
 
### Installing
1. pip install py3utils

## Docs
* datetimeutil
```
from py3utils.datetimeutil import TimeUtils

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
```

* urlutil
```
from py3utils.urlutil import Url


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
```

## License
MIT
 
