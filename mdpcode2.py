from ncclient import manager
import re
nexus=manager.connect(
    host="",
    username= "admin",
    password= "Admin_1234"

)

for capability in nexus.server_capabilities:
    print(capability)