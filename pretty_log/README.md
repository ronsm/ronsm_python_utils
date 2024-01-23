# Usage

```
LOG_CONFIG = {
     'package_name': 'Your Package Name',
     'package_git': 'N/A',
     'author_name': 'Your Name',
     'author_git': 'yourgithandle',
     'author_email': 'your.email@domain.com'
}

self.sl = SimpleLog(LOG_CONFIG)
self.sl.welcome()
self.log_state(1) # wait

...

self.log_state(0) # ready
```
