# Goal is to add AI for recommendations and storage of favorites

from functions import *

# Main
def main():

	name = input("What would you like to hear today?\n")
	link_grabber(name)

	play()

	# video_info(link)
	# download(link)


if __name__ == "__main__":
	main()
