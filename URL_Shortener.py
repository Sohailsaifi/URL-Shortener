import pyshorteners

#input for the link

link = input("Enter the link : ")

shortener = pyshorteners.Shortener()

#calling the function

short_link = shortener.tinyurl.short(link)

#printing the short url
print(short_link)
