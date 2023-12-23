import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import pandas as pd
import subprocess
from imessage_reader import fetch_data
import pprint
import json
from openai import OpenAI
from config import api_key

client = OpenAI(api_key=api_key)


# # Define the command to execute the JavaScript script
# command = ['node', 'number_handler.js']
# # # Execute the command and capture the output
# output = subprocess.check_output(command, universal_newlines=True)
# print("output: ", output)

DB_PATH = "/Users/gozieonyia/Library/Messages/chat.db"
# Create a FetchData instance
fd = fetch_data.FetchData(DB_PATH)

# Store messages in my_data
# This is a list of tuples containing user id, message and service (iMessage or SMS).
my_data = fd.get_messages()


# Your OpenAI API key


# pprint.pprint(my_data)

# print(my_data[0][1], '\n', my_data[0][2],'\n', my_data[0][0],'\n')

# lets make a dictionary of the messages. The keys will be the user id and the values will be a list of the messages.
# the messages will be important to analyze the sentiment of the messages and other things.

# TODO: 
# 1. put the logic in a function named get_messages

# Create a dictionary to store the messages
def get_contact_count(message_dict):
    return len(message_dict.keys())

message_dict = {}
message_count ={}
for message in my_data:
    if len(message[0])<10:
        continue
    # the replace function is used to remove the leading +1 from the phone number credit to copilot
    # I need to make the replace more generic to handle other country codes
    phone_nubmer = message[0].replace('+1', '')
    # print("test x")


    if phone_nubmer not in message_dict:
        message_dict[phone_nubmer] = [message[1]]
        message_count[phone_nubmer] = 1
    else:
        message_dict[phone_nubmer].append(message[1])
        message_count[phone_nubmer] += 1
# prints out the dictionary
# partial_dict = dict(list(message_dict.items())[:3])
# pprint.pprint(partial_dict)
#TODO: subsitiute the hard coded conversation with the message_dict  of a specific contact
# Example conversation data
conversation = [
    "Hey Dean how’ve you been? This is Gozie",
    "Hey Gozie!! Long time! Oh nothing much, just uprooted my entire life and moved to North Carolina. Haha",
    # ... include other parts of the conversation
]

# Joining the conversation into a single string
conversation_text = "\n".join(conversation)

# Constructing the prompt for sentiment analysis
content = f"Analyze the sentiment of this conversation and provide aditional talking points/suggestions to extend the conversation. keep your response as concise as possible. give me bullet points:\n{conversation_text}"

# Sending the request to OpenAI API
response = client.completions.create(model="text-davinci-002", prompt=content,
        max_tokens=50,  # Extended for longer responses
        temperature=0.5,  # Adjust for creativity
        top_p=1,  # Control response diversity
        frequency_penalty=0,  # Fine-tune word frequency
        presence_penalty=0  # Fine-tune word presence
    )

# Extracting and printing the response
print("open_ai response :)",response.choices[0].text.strip())

print(get_contact_count(message_dict))
# pprint.pprint(message_dict)
# pprint.pprint(message_dict['gaylerivers39@icloud.com'])



#prints out the message count for each contact
# pprint.pprint(message_count)

# You can also use the json module to print the dictionary in a more readable format.  
# Here is an example:  import json  print(json.dumps(message_dict, indent=4))  This will print the dictionary in a more readable format.  
# I hope this helps.  Let me know if you have any questions.  Thanks.

#I wonder if the value being appended to contacts can be an object that contains the number of messages sent in order to make the node size correspond to the number of messages sent
contacts=[]
for key in message_count:
    contacts.append(key)

G2 = nx.Graph()
G2.add_nodes_from(contacts)

#I want node size to correspond to the number of messages sent
#how can I do that?:  
#I want the node color to correspond to the number of messages sent
#how can I do that?
#
# nx.draw(G, with_labels=True, node_color = "blue", font_size = 8, bbox=dict(facecolor='red', alpha=0.5), node_size = 100, edge_color = "green", width = 2.0, style = "dashed", alpha = 0.5)


nx.draw(G2, with_labels=True, node_color = "blue", font_size = 7, 
        node_size = 100, edge_color = "green", width = 2.0, alpha = 0.5)

plt.show(block=False)
wait = input("PRESS ENTER TO CONTINUE.\n")
# plt.close()
print("done")

# # Draw graph
# G = nx.Graph()
# G.add_edges_from(friends)
# nx.draw(G, with_labels=True, node_color = "blue", font_size = 10, 
#         node_size = 100, edge_color = "green", width = 2.0, alpha = 0.5)
# plt.show()


 
#print(nx.nodes(G))

# G = nx.Graph()
# friends = []

# G.add_edges_from(friends)
# nx.draw(G, with_labels=True, node_color = "blue", font_size = 8, bbox=dict(facecolor='red', alpha=0.5), 
#         node_size = 100, edge_color = "green", width = 2.0, style = "dashed", alpha = 0.5)
# plt.show()



