from google import google
import texttospeech
import randomresponse

def search(query):
	page=1
	searchResult=google.search(query,page)
	searchList=list(searchResult)
	if(len(searchList)>=2):
		texttospeech.convert(str(searchList[1].description))
	else:
		randomresponse.generateResponse('searchfail')	
	return


