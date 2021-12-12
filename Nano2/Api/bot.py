from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot5')

text = [
    "How do add a boarding pass? I see no passes tab.",
"Hi Len. Could you try the steps in this guide and see if that helps: https://goo.gle/2MxU28H? If you still face issues, we're happy to help you directly here: https://goo.gle/2r2DZrR. Thanks for reaching out.",
"Keeps disappearing from home page. Very disappointing as my covid certificate is attached!!!!!",
"Hi Penny. We're sorry about that. Let's connect you to a specialist for further assistance. Visit: https://goo.gle/2r2DZrR. Thanks for reaching out.",
"App is now working for me as expected. Google Pay for smart watches is now (finally) available in New Zealand, so my Ticwatch Pro works for payments. On my phone I use it for contactless payments, but also accessing loyalty cards etc. Recently also been able to store my Covid vaccine certificate, which is coming into use in new Zealand shortly.",
"Hi Robin. Support for Google Pay on Wear OS watches is available in US, UK, Italy, Spain, Australia, Canada, Poland, Russia, or Germany. We are working to expand and bring it to more countries in the future. More info: https://goo.gl/k3nyZd. Thanks for reaching out.",
"whether it works is a matter of luck. detect very poorly. this week it simply clashed and had false messages of complete transactions while transactions actually failed. Can't believe this happens to a payment app and Google. please fix it ASAP.",
"Hi Nadia. We're sorry to hear that. Let's connect you to a specialist for further assistance. Visit: https://goo.gle/2r2DZrR. Hope it gets resolved soon.",
"Why cant I press and hold power to bring up the payment, only does that on OnePlus. Why",
"Hi Harry. Have a look at this guide to help you use cards & passes on Google Pixel: http://goo.gle/3rUJenz. Also, you can send us feedback regarding this directly from the Google Pay app by opening its menu and selecting Send feedback. Thanks.",
"I've been using Google Pay on my Samsung Galaxy Watch 4 since it was released, and Google Pay is only working half the time. The NFC terminal usually comes with an error message saying Check your phone or Enter an unlock code. No messages are shown on my watch, other than a red error symbol. If I use my phone, it works without a hitch every time. I bought the GW4 because of Google Pay, so I wouldn't have to drag my phone or CC with me where ever I went.",
"That is not the experience we want you to have, Oystein. Have a look at this article to pay with your smartwatch: https://goo.gle/39ffZmL. If all sounds good and the issue persists, visit: https://goo.gle/2r2DZrR. Thanks for reaching out.",
"There is a dating app called Kismia that is bogus. I want you to get me off that app.",
"Hi Keith. You can manage subscriptions at https://pay.google.com. From the menu on the left, select the active subscriptions tab, find the one you want to manage/update, click Account Details and select Cancel Subscription. If you still experience problems, visit: https://goo.gle/2r2DZrR. Thanks for reaching out.",
"Adding a credit/debit card fails on galaxy fold 3. It just flashes through a few screens real quick when you click to add a new card, then returns where it started.",
"Useless garbage keeps giving me error when trying to add my card, googling the error gives 0 results that help",
"Hi Ayaka. You can add a debit card, credit card, bank account, and other payment methods in the Google Pay app to help you make payments and get insights about your money. Have a look at this article to fix the issues: https://goo.gle/2SAQQwG. If everything looks good but you still experience problems, visit: https://goo.gle/2r2DZrR. Thanks!",
"No matter what the problem is, Google is always there to fix it. And they make the best products web apps hybrids and OS. Honestly any issue you have they will resolve, I just posted a bad review and I just got something fixed I've been stressed about for months. They replied in 2 seconds flat and pushed me in the right direction, Google I can never stay mad at you 😘🙏🏻",
"That's not the experience we want you to have, James. Let's connect you to a specialist for assistance. Visit: https://goo.gle/2r2DZrR. Thanks!",
"Keep deleting review",
"Hi David! Sorry to hear you’re having trouble paying. Have a look at this guide if you have trouble using Google Pay in stores: https://goo.gle/2SwLouL. If everything looks good but you still experience problems, visit: https://goo.gle/2r2DZrR. Thanks!"
]




trainer = ListTrainer(bot)
trainer.train(text)

def query(msg):
    response = bot.get_response(msg)
    return response