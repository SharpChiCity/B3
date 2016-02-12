---ABOUT---
BingBucksBot (B3) is a simple python script that asks for your email and password in order to search Bing.com using Chrome and gather points for the rewards program. At no point will your personal data be sent back to the creator, nor anywhere else.

B3 was built using Python 3.4 and Selenium. It Will* compiled using cx_Freeze at some point. The source code can be located at https://github.com/MonteTribal under the name 'B3' (If it is not taken down). 

It was tested using Google Chrome (Version 48.0.2564.97 m)

**PLEASE NOTE**
	words.txt is basically an unedited dictionary. There are 'bad words' in this list. I take no responsibility if a search result happens to offend you, or if you get into any trouble for having any particular search term in your search history.

---HOW TO---
For the bot to work, you must feed it your account information. This can be done in credentials.XML. Simply change the contents of <email>xxx</email> and <password>xxx</password> to your personal data. Then run the .exe. Again, your information will only be used to log into your account, and nothing more.

If you do not have a Microsoft Account, you can create one at: https://login.live.com
The info used to create that account is what will go in credentials.

If you do not have Google Chome, it can be downloaded at https://www.google.com/chrome/browser/desktop/

If you are viewing the source, I assume you know what you are doing. It is <100 lines, you'll be fine.

---FILE DETAILS---
B3.exe
	this runs the search bot.
words.txt
	a very long list of words. I think I got it from:
		https://docs.oracle.com/javase/tutorial/collections/interfaces/examples/dictionary.txt
	but It has been a long time since I got it.
credentials.xml
	the home of your account information. must be edited before the bot will work for you.

---V1.0---
	Initial Commit
	Open new Chrome browser
	Log into Microsoft Account
	Search 30 times (15 points)
	Close Chrome browser
	
---Side Note---
B3 v1 was made by a fairly ill developer on his sick day. If you are viewing the source, be aware that OOP practices were fairly ignored, and that the dev simply passing the time. This may be rewritten at some point when the dev's head is less foggy from cold medicine.