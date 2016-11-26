import urllib

def readText():
    text = open("C:\Udacity\PythonProjects\PythonLearning\sampleText.txt")
    contents = text.read()
    print(contents)
    text.close()
    checkProfanity(contents)


def checkProfanity(textToCheck):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+textToCheck)
    output = connection.read()
    print(output)
    connection.close()
    
readText()
