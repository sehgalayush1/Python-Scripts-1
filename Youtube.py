import pafy

url= raw_input("Enter your url: ")
video=pafy.new(url)
print "Do you Want to Download it or want to extract information?"
choice = raw_input("Input 'download' to Download or 'extract' to Extract Information: ")

if choice == 'download':
	best=video.getbest()
	best.download(quiet=False)
elif choice == 'extract':
	print "Title : " +video.title
	print "Rating : " +str(video.rating) 
	print "View Count : " + str(video.viewcount) + "Author : " + video.author + "Length :" + str(video.length)
	print "Duration :" + str(video.duration) + "Likes : "+ str(video.likes) + "Dislikes : "+ str(video.dislikes)
	print "Description : "+ video.description
	print "Published on Date : " + str(video.published)
else:
	print "Oops wrong Choice !"
