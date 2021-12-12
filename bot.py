
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd

data = pd.read_csv('C:\\Users\\agarw\\Downloads\\GooglePayIndia.csv')

selected_rows = data[~data['replyContent'].isna()] 

rows = selected_rows[['content','replyContent']].values


bot = ChatBot('Bot5')

# Create a new trainer for the chatbot
trainer = ListTrainer(bot)



text = []

for row in rows[:5]:
    #print(row)
    
    text.append(row[0])
    text.append(row[1])

print(text)

trainer.train(text)


  
# response = bot.get_response('How do add a boarding pass?')
# print('How do add a boarding pass?')
# print(response)



while True:
    request=input('you :')
    if request == 'OK' or request == 'ok':
        print('Bot: bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:', response)
