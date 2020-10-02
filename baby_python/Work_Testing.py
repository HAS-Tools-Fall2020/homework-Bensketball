# Attendance for class

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
filename = 'meeting_saved_chat #12(10-01-20).txt'
filepath = os.path.join('zoom_chats', filename)
print(os.getcwd())
print(filepath)

# %%
# creation of data frame
chat = pd.read_table(filepath, sep = '\t',
        names=['time', 'from + name + message']
        )
# chat
# print(chat)
# print(chat['from + name + message'])
# message = data['from + name + message'].str.split(":", n = 1)
chat['from + name'], chat['message'] = chat['from + name + message'].str.split(':', 1).str
chat['from'], chat['name'] = chat['from + name'].str.split('  ', 1).str
# print(chat['time'])
chat['message']
chat_org = pd.DataFrame(chat, columns = ['time', 'name', 'message'])
# print(chat)
print(chat_org)
# %%
chat_by_name= chat_org.sort_values(by=['name'])
# print(present.name[present.time.contains('16')])
present = chat_by_name[chat_by_name.time.str.contains('16')]
late = chat_by_name[chat_by_name.time.str.contains('17')]
late18 = chat_by_name[chat_by_name.time.str.contains('18')]
late = late.append(late18)
# %%
print(present)

# %%
print(late)

#%%
print(len(present))

#%%
print(len(late))

# %%
print(len(chat_org))

# %%
print(len(chat_by_name))
# %%
