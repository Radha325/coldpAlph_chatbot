import random
Responses={
"hello":["Hyee","Hello","Greetings"],
"how are you?":["I'm fine and you?","I'm doing well,thankyou"],
"good bye":["Good bye!","See you later!","Bye!"]
}
while True:
 user_input=input("you:  ")
 if user_input.lower()in Responses:
    bot_reply=random.choice(Responses[user_input.lower()])
    print("Bot:",bot_reply)
else:
     print("Bot: I'm sorry,I didn't understand what you said." )
     