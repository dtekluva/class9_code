from datetime import datetime, timezone
import pytz

tz = pytz.timezone('Africa/Lagos')
lagos = datetime.now(tz)
print(str(lagos)[0:26])
formatedDate = lagos.strftime("%Y-%m-%d %H:%M:%S")
print(formatedDate)