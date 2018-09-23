import time
import requests

print("Coder: Mostafa M. Mead")
print("Python Version : 3")
print("Facebook Likes With React Script\n")

def CheckToken(accessToken):
	checkUrl = 'https://graph.facebook.com/me/?access_token={}'.format(accessToken)
	if 'first_name' in str(requests.get(checkUrl).content):
		return True
	else:
		return False

def FBReaction(reAction , tokensTxt , postsTxt):
	with open(tokensTxt) as f:
		lines = f.read().split("\n")
	with open(postsTxt) as g:
		posts = g.read().split("\n")
	for postId in posts:
		for accessToken in lines:
			if CheckToken(accessToken):
				reactLink = 'https://graph.facebook.com/{}/reactions'.format(postId)
				reactData = {
					'type':reAction,
					'access_token':accessToken
				}
				try:
					reactReq = requests.post(reactLink , data=reactData)
				except Exception as e:
					print(e)
				else:
					print("Reaction Done Succesfully On")
			else:
				print('Invalid Access Token')

def main():
	userReact = input('Enter Reaction [ LIKE , HAHA , WOW , ANGRY , LOVE , SAD ]: ')
	userTokensTxt = input('Enter Access Tokens Text: ')
	userPostsTxt = input("Enter Your Posts Ids Text: ")
	FBReaction(userReact , userTokensTxt , userPostsTxt)

if __name__ == '__main__':
	try:
		main()
	except Exception as Ex:
		print(Ex)
		time.sleep(1000)
	else:
		print("Process Done Succesfully")
		time.sleep(1000)