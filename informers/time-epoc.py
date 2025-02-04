from datetime import datetime

import time

current_ms = int(time.time() * 1000)
print(f"Current milliseconds since epoch: {current_ms}")

# Method 1: From current timestamp
current_ms = int(time.time() * 1000)

specific_timestamp = 0 +1000 * 60 *60 * 24* 3
date_from_timestamp = datetime.fromtimestamp(specific_timestamp/1000)
print(f"Date from specific timestamp: {date_from_timestamp}")


from datetime import datetime

date = datetime(1970, 1, 1)
epoch_milliseconds = int(date.timestamp() * 1000)
print(f"Milliseconds since epoch for June 4, 1980: {epoch_milliseconds}")