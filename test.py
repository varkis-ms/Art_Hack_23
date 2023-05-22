import requests
from backend.database.enums.role import Role
import uuid
from datetime import date
# requests.get("https://oauth.vk.com/authorize?client_id=51651729&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.131&state=123456")

# a = "vk1.a.wZhyJqr9rnAqyaQIACILJir9q4JM_hJ1TkhoJDZSmXqBukD7PUEbYIE9zMXMO3vsjJEsmPhQJZuY-nsjF55Q3E1n5kxMMcoj0-iwrEb62Oqd2WRCHIsSvrmgoRRAFwMPQXavs9d8QkCl6y3b-iCykfyMrOD_evhhQ5j6-17Q5rCgJU6ToWR6RfsSU2zUvUJn"
# b = "vk1.a.7eW1xEHKhw_XaShhEqUGLGed3XuqUJRKmYUNKDgxQg66_l_gwMfCs63Ldm01DpH3ubi2SlRug4sH_E1EoTNsKij7tH0HOwI4bMECeGHVnA6NbfcDBAnOqQG88IJmEFGVLiKWUBZkRH-FZ27pWzbtdQY2gwafKIza8xPGjB5N2wmVxhrDh7u93_2_VNlUcwki"
#
# resp = requests.get(f"https://api.vk.com/method/users.get?access_token={a}&v=5.131")
# print(resp.json()["response"][0]["id"])

# print(Role.admin.value)

print(date.today())