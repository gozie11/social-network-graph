###
# This  is a very rough draft.
###

from imessage_reader import fetch_data
import pprint
import json

DB_PATH = "/Users/gozieonyia/Library/Messages/chat.db"

# Create a FetchData instance
fd = fetch_data.FetchData(DB_PATH)

# Store messages in my_data
# This is a list of tuples containing user id, message and service (iMessage or SMS).
my_data = fd.get_messages()
#print(my_data)

#print(my_data[0][1], '\n', my_data[0][2],'\n', my_data[0][0],'\n')

# lets make a dictionary of the messages. The keys will be the user id and the values will be a list of the messages.

# Create a dictionary to store the messages
message_dict = {}
message_count ={}
for message in my_data:
    if message[0] not in message_dict:
        message_dict[message[0]] = [message[1]]
        message_count[message[0]] = 1
    else:
        message_dict[message[0]].append(message[1])
        message_count[message[0]] += 1
# prints out the dictionary
#pprint.pprint(message_dict)

#prints out the message count for each contact
pprint.pprint(message_count)

# can you print a pretty version of the dictionary?  
# I'm not sure what you mean by pretty version.  
# Do you mean print the dictionary in a more readable format?  
# If so, you can use the pprint module.  
# Here is an example:  import pprint  pprint.pprint(message_dict)  This will print the dictionary in a more readable format. 
# You can also use the json module to print the dictionary in a more readable format.  
# Here is an example:  import json  print(json.dumps(message_dict, indent=4))  This will print the dictionary in a more readable format.  
# I hope this helps.  Let me know if you have any questions.  Thanks.
