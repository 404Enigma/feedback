import pandas as pd

data = pd.read_csv('C:\\Users\\agarw\\Downloads\\GooglePayIndia.csv')

selected_rows = data[~data['replyContent'].isna()] 

rows = selected_rows[['content','replyContent']].values
#print(rows)
text = [
    "How do add a boarding pass? I see no passes tab."
"Hi Len. Could you try the steps in this guide and see if that helps: https://goo.gle/2MxU28H? If you still face issues, we're happy to help you directly here: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Keeps disappearing from home page. Very disappointing as my covid certificate is attached!!!!!"
"Hi Penny. We're sorry about that. Let's connect you to a specialist for further assistance. Visit: https://goo.gle/2r2DZrR. Thanks for reaching out."
"App is now working for me as expected. Google Pay for smart watches is now (finally) available in New Zealand, so my Ticwatch Pro works for payments. On my phone I use it for contactless payments, but also accessing loyalty cards etc. Recently also been able to store my Covid vaccine certificate, which is coming into use in new Zealand shortly."
"Hi Robin. Support for Google Pay on Wear OS watches is available in US, UK, Italy, Spain, Australia, Canada, Poland, Russia, or Germany. We are working to expand and bring it to more countries in the future. More info: https://goo.gl/k3nyZd. Thanks for reaching out."
"whether it works is a matter of luck. detect very poorly. this week it simply clashed and had false messages of complete transactions while transactions actually failed. Can't believe this happens to a payment app and Google. please fix it ASAP."
"Hi Nadia. We're sorry to hear that. Let's connect you to a specialist for further assistance. Visit: https://goo.gle/2r2DZrR. Hope it gets resolved soon."
"Why cant I press and hold power to bring up the payment, only does that on OnePlus. Why"
"Hi Harry. Have a look at this guide to help you use cards & passes on Google Pixel: http://goo.gle/3rUJenz. Also, you can send us feedback regarding this directly from the Google Pay app by opening its menu and selecting "Send feedback". Thanks."
"I've been using Google Pay on my Samsung Galaxy Watch 4 since it was released, and Google Pay is only working half the time. The NFC terminal usually comes with an error message saying "Check your phone" or "Enter an unlock code". No messages are shown on my watch, other than a red error symbol. If I use my phone, it works without a hitch every time. I bought the GW4 because of Google Pay, so I wouldn't have to drag my phone or CC with me where ever I went."
"That is not the experience we want you to have, Oystein. Have a look at this article to pay with your smartwatch: https://goo.gle/39ffZmL. If all sounds good and the issue persists, visit: https://goo.gle/2r2DZrR. Thanks for reaching out."
"There is a dating app called Kismia that is bogus. I want you to get me off that app."
"Hi Keith. You can manage subscriptions at https://pay.google.com. From the menu on the left, select the active subscriptions tab, find the one you want to manage/update, click Account Details and select Cancel Subscription. If you still experience problems, visit: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Adding a credit/debit card fails on galaxy fold 3. It just flashes through a few screens real quick when you click to add a new card, then returns where it started."
"Sorry to hear that, Scott. You can find the steps for adding cards here: https://g.co/help/n866n. If the issue still persists, you can contact us directly if you have further questions: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"Won't let me use it in a location as it says it's not here yet but I works fine on my phone"
"We hear you, James. Our Google Pay support team would be the best to help you with this. Let's connect you to them for further assistance: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"Useless garbage keeps giving me error when trying to add my card, googling the error gives 0 results that help"
"Hi Ayaka. You can add a debit card, credit card, bank account, and other payment methods in the Google Pay app to help you make payments and get insights about your money. Have a look at this article to fix the issues: https://goo.gle/2SAQQwG. If everything looks good but you still experience problems, visit: https://goo.gle/2r2DZrR. Thanks!"
"No matter what the problem is, Google is always there to fix it. And they make the best products web apps hybrids and OS. Honestly any issue you have they will resolve, I just posted a bad review and I just got something fixed I've been stressed about for months. They replied in 2 seconds flat and pushed me in the right direction, Google I can never stay mad at you 😘🙏🏻"
"That's not the experience we want you to have, James. Let's connect you to a specialist for assistance. Visit: https://goo.gle/2r2DZrR. Thanks!"
"Keep deleting review"
"Hi Emanuelijus. Let's connect you to a specialist for assistance. Visit: https://goo.gle/2r2DZrR. Thanks!"
"It won't update my balance from in app purchase."
"Hi there. Let's connect you to a customer support specialist: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Terrible I've had to download this app so I can create a wallet for football tickets and it won't let me download the information from the football club keeps saying there's been an error try again"
"Hi Trevor. We're sorry about that. Could you try the steps in this guide and see if that helps: https://goo.gle/2MxU28H? If you still face issues, we're happy to help you directly here: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"Horrendous glitches. Sometimes works, sometimes not!!! Very user unfriendly!!!"
"Hi Izeizei. Let's connect you to a specialist for assistance. Visit: https://goo.gle/2r2DZrR. Thanks!"
"Doesn't work with TD Bank cards, needs to be fixed to allow all cards on the app"
"Hi Aiden. We're always excited to support more cards. You can find a list of supported banks and cards at https://goo.gl/fEBx5D. If your's isn't supported, we recommend you contact your card issuer regarding their support of Google Pay. Thank you."
"Pathetic, been dowloading football tickets all season now just stopped working, back to iphone for me absolute joke of a app"        
"Hi Gary. We're sorry about that. Could you try the steps in this guide and see if that helps: https://goo.gle/2MxU28H? If you still face issues, we're happy to help you directly here: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"This app never worked. Developer doesn't give a s&@* about it!"
"We hear you, Vitalie. Our Google Pay support team would be the best to help you with this. Let's connect you to them for further assistance: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"Does not work with ANDROID 12 after device has been used for ANDROID 12 beta testing"
"Sorry to hear that, Mike. Could you try clearing the Google Pay app's cache, data and restart your phone to see if it works fine? If the issue still persists, you can contact us directly if you have further questions: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Stopped working. Used to work fine and app is good. But randomly all my 3 payment cards are being refused. When I hold against reader it just says payment didn't work. Plenty money on cards."
"Sorry to hear that, Black. Our Google Pay support team would be the best to help you with this. Let's connect you to them for further assistance: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"Buggy, cannot connect most of my card, despite advertised ability to do it."
"Sorry to hear that, Ilia. Could you try clearing the Google Pay app's cache, data and restart your phone to see if it works fine? If the issue still persists, you can contact us directly if you have further questions: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"Update to my previous feedback about not being able to add cards in pixel 6. I have cards already added but it won't let me Enable contactless. Get an error saying can't verify details. I can't even add the same cards again. I have the same cards on my Asus Rog phone 3 and I can add/use cards with no issues. So it must be a pixel 6 specific issue? I have been using Google pay on other phones for years without any issues"
"Sorry to hear that, Mohammed. You can find the steps for adding cards here: https://g.co/help/n866n. If the issue still persists, you can contact us directly if you have further questions: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Your phone doesn't meet security requirements on samsung s21 android 12 update. Are you aware of this"
"We're sorry to hear that, Graham. Have a look at this article to check if the phone can make in-store payments: https://goo.gle/2sXlEgv. If the issue persists, we can help you directly here: https://goo.gle/2r2DZrR. Thanks for reaching out."
"I cannot turn it off. I want to use another app and pay takes over and it won't uninstall"
"Hi Doug. If you installed the Google Pay app on your device, you can uninstall it. In some cases, if the Google Pay app came preinstalled on your device, you can’t uninstall it, but you can disable it. To do so, follow these steps: https://goo.gle/33D0y5h. If all sounds good and the issue persists, visit: https://goo.gle/2r2DZrR. Thanks!"
"Doesn't even work"
"Sorry for the delayed response, Luisa. Our Google Pay support team would be the best to help you with this. Let's connect you to them for further assistance: https://goo.gle/2r2DZrR. Thanks for reaching out."
"I have been trying to call someone all day yesterday and today,buy nothing,can you please give me a contact number in the UK that I can speak with someone, today would be very helpful,thanks Andrew"
"Hi Andy. Let's connect you to a specialist for assistance. Visit: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Every time I try to pay in store with the phone (I have a Revolut card enrolled) I get the message phone moved too fast" 🙁"        
"Hi Adrian. Sorry to hear you’re having trouble paying. Here are some steps to resolve the problem: https://goo.gle/2SwLouL. If the issue persists, we can help you directly here: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Why am I still being asked to install Google pay when there is a newer version available? Everytime I open this app it takes me to 
"the new app, why do I need both installed on my phone!? Totally convenient...just waiting to see how secure it is for that 5th star." 
"Hi Erik. You can still use the older Google Pay app for now, but soon you can no longer send or receive money unless you download the new Google Pay app. To learn more: g.co/help/pxgaz5. If everything looks good but you still experience problems, visit: https://goo.gle/3c9Ojlv. Thanks for reaching out."
"Your device doesn't meet security requirements"
"We're sorry to hear that, Matthew. Have a look at this article to check if the phone can make in-store payments: https://goo.gle/2sXlEgv. If the issue persists, we can help you directly here: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Not able to use this app to pay. Has been embarrassing when this is your only means to pay."
"Sorry to hear that, Alison. Our Google Pay support team would be the best to help you with this. Let's connect you to them for further assistance: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Trying to add my banks debit card to the app, keeps telling me to contact bank. Have deleted this app as we as the banks app a number of times and get the same result. Bank can see the phone as registered on their system but the app still won't accept the card. Has even raised a token to force the registration but waited 12 hours as requested by the bank , still not working. Worked fine on my samsung s10+ but won't on my new samsung Fold3. Phone software is current version."
"Sorry to hear that, Brian You can find the steps for adding cards here: https://g.co/help/n866n. If the issue still persists, you can contact us directly if you have further questions: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"This app was working fine then it stopped yesterday. Im in Australia and I went to edit my details and a lady in Tennessee is on my address details but Im the primary user. Now Im unable to enter my card details. So frustrating"
"That's not the experience we want you to have, Brian. Let's connect you to a specialist for further assistance. Visit: https://goo.gle/2r2DZrR. Thanks!
"
"there is nothing simple and easy about it Google pay app!!!!! This is an update y'all give me this whack email address to get to IT specialist and they still give me the same running around shame on you developer)(I don't know what happened to Google I used to be able to use the pay app now I'm not able to use it so if anybody go outside to download I will advise you not to find out Google has done something with their account online and be able to use the internet do not understand Google Play"
"Hi there. We understand your concern. Let's connect you to a specialist for further assistance. Visit: https://goo.gle/2r2DZrR. Thanks!"
"NFC completely stopped working after the last Android update! Tried contacting customer service for help and all they can give me is 
"turn your phone off and then back on. It might be time to switch to Apple."
"Sorry to hear that, Kelly. Our Google Pay support team would be the best to help you with this. Let's connect you to them for further assistance: https://goo.gle/2r2DZrR. Thanks for reaching out."
"TWICE THIS APP HAS DELETED MY CARD WITHOUT WARNING AND NOW WON'T AUTHENTICATE OR VERIFY WITH MY BANK-MAKING THE APP ABSOLUTELY USELESS AND VERY EMBARRASSING WHEN I WENT TO PAY FOR THINGS IN A STORE-!! 😡 AND YES I HAVE SCREENLOCK ENABLED LIKE MOST PEOPLE & THEIR MOBILES-!! (N LOOK AT THEIR REPLY-!!! 🤔 😑 🙄 😂😂😂)"
"That doesn't sound good, Amy. Did you have screen lock enabled? This is required to use the app and prevent card deletion. If you did, can you get in touch so we can help you directly: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Not able to use on finally release of androind 12 Samsung UI 4. Not in beta anymore, how is it still not supported"
"Hi there! You can find the device requirements and settings here: https://goo.gle/3aBwk5U. If everything looks good but you still experience problems, visit: https://goo.gle/2rva9fU. Thanks for reaching out to us."
"Doesn't? work in other regions"
"Hi Sam. Google pay is available in selected countries. Have a look at this guide for the list of countries, participating banks and cards that are supported on Google Pay: https://goo.gle/2tWDroH. Hope this info helps."
"Not working in Oneplus 9 pro"
"Hi Vinoth. You can find the device requirements and settings here: https://goo.gle/2EVaDPx. If everything looks good but you still experience problems, visit: https://goo.gle/2r2DZrR. Thanks for reaching out.
"
"I can even download the app.. tried multiple times but just keeps spinning"
"Hi Denise. Could you try clearing the Google Pay app's cache, data and restart your phone to see if it works fine? If the issue still persists, you can contact us directly if you have further questions: https://goo.gle/2rva9fU. Thanks for reaching out."
"Google Pay unsupported on device (Galaxy watch 4) since recent device software update."
"Hi Jeffrey! Have a look at this article to pay with your smartwatch: https://goo.gle/39ffZmL. If you need help, we're happy to assist: https://goo.gle/2rva9fU. Thanks for reaching out to us."
"I expected more from Google, you need to give the option to manually add categories or the option to manually add cards under an existing category... This should be a "Google wallet" where you can add cards to pay, loyalty cards(any card) and pretty much everything we need in one place.... For example i would like to add the card that i use to get the bus,to store my wifi password as a barcode and 
"many more things like gym memberships card and local shop loyalty cards...."
"Thanks for the feedback, Christos! Feel free to send us feedback directly from the app by opening Google Pay > tap menu icon > Send feedback."
"Terrible, suddenly stopped working on TFL bus services and ticket barriers on my nearly two year old phone. Luckily I had one of the 
"cards on me. Despite it still working fine in shops and restaurants I no longer trust it. Judging by reviews here and elsewhere it seems this is a common problem. Edited to add: yes I have done as suggested, as I said in my review it has worked for nearly two years with no problem. It also does not work at all on TFL buses anymore."
"Hi Sophie. Sorry to hear you're having trouble using Google Pay with Transport for London. Next time you're there, try keeping your device up against the terminal until the gate opens. If the issue persists, we'd appreciate it if you open Google Pay app > Tap menu icon > Help > Send feedback > check "include system logs." Thanks!"
"App is immediately crashing now... :("
"Hi Andy. We're sorry about that. Could you try clearing the Google Pay app's cache, data and restart your phone to see if it works fine? If the issue still persists, you can contact us directly if you have further questions: https://goo.gle/2rva9fU. Thanks for reaching out."
"Why it isn't working on redmi note 10..not supported apps.so disappointed."
"Hi Marilou! We understand your concern. You can find the device requirements and settings here: https://goo.gle/3aBwk5U. If everything looks good but you still experience problems, visit: https://goo.gle/2rva9fU. Thanks for reaching out to us."
"I don't need this or want this and there is no reason I should be stuck with this application on my phone."
"Hi Shawn. If Google Pay came pre- installed on your device, you can’t uninstall it but you can disable it. More info: https://goo.gle/33D0y5h. If everything looks good but you still experience problems, visit: https://goo.gle/2rva9fU. Thanks!"
"Good"
"Hi Palmer! Thanks for your review! We'd like our users to have the best possible experience with Google Pay. Please let us know what 
"we can improve. If you experience issues with the app, you can connect to a specialist for further assistance. Visit: http://goo.gle/3bmogJa."
"No longer auto fills my information which is literally the only thing I use it for"
"Hi there. Have a look at this article for more info on auto-fill: https://goo.gle/34FXVAV. We can also help directly here if you have questions: https://goo.gle/2r2DZrR. Thanks for reaching out."
"Unsafe. When you lose or misplace your phone it's dangerous."
"Hi there! To help protect your information in case your phone gets lost or stolen, the Google Pay app requires a screen lock. If your device is locked, the Google Pay app can’t be opened: g.co/help/3xjh9. Learn more here: https://goo.gle/3hJTUTX. If you need help, visit: goo.gle/2r2DZrR. Thanks."
"Worked perfectly for months then stopped working saying my device didn't meet security criteria. Hadn't made any updates to Android ... Literally stopped working overnight"
"Hi Stephen. We're sorry about that. Have a look at this article to make sure your phone meets software standards for Google Pay: https://goo.gle/2sXlEgv. If everything looks good but you still experience problems, visit: https://goo.gle/2rva9fU. Thanks for reaching out to us."
"All store stopped working with gpay in canada since I got my pixel 6 pro."
"Hi David! Sorry to hear you’re having trouble paying. Have a look at this guide if you have trouble using Google Pay in stores: https://goo.gle/2SwLouL. If everything looks good but you still experience problems, visit: https://goo.gle/2r2DZrR. Thanks!"
]

for row in rows[:50]:
    #print(row)
    
    text.append(row[0])
    text.append(row[1])
    print('"{}"'.format(row[0]))
    print('"{}"'.format(row[1]))

#print(text)