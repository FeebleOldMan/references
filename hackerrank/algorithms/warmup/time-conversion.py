#!/usr/bin/env python
import time

print time.strftime('%H:%M:%S', time.strptime(raw_input().strip(), '%I:%M:%S%p'))
