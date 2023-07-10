import requests
import pandas as pd
import sqlalchemy as db


class AutoDoc():

##Elias's code goes here
    def readFile(self, fileName):
     fileToRead = open(fileName)
     text = ""
     line = fileToRead.readline()
     text = text + "\n" + line

     while line:
         line = fileToRead.readline()
         text = text + "\n" + line 
     fileToRead.close()

     return text

##Xavier's Code below:
    def call_api(self, input_text):
        # API Key (replace "INSERTAPIKEYHERE" with your actual OpenAI API key)
        api_key = "INSERTAPIKEYHERE"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Generate prompt
        prompt = f"{input_text}"

        # API URL
        api_url = "https://api.openai.com/v1/chat/completions"

        data = {
            "model": "gpt-3.5-turbo",  # Specify the GPT model here
            "messages": [
                {"role": "system", "content": "You are AutoDoc, a helpful programming tool that automatically adds documentation to undocumented code. The user will provide you with code copied from a file. AutoDoc adds inline comments, function headers, etc to explain the code to its best understanding. Then it only returns the code unchanged with the added documentation. AutoDoc's output is directly written to the file, so the entire AutoDoc response must be formatted as comments if it is a note."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"OpenAI API request failed with status code {response.status_code}.")
    
    def writeFile(self,content,fileName):
        fileToWrite = open(fileName,'w')
        fileToWrite.write(content)
        fileToWrite.close()
        print("content succesfully written to the file")
    

## To make everything run
if __name__ == "__main__":
    #make instance
    autodoc = AutoDoc()
    
    #say howdy to the user & tell them what's up
    print("Welcome to AutoDoc!\n\t- I'm here to make undocumented code easier to understand.\n\t- I might not get things right, but I'll try my best.\n\t- I'm using a generative pretrained transformer to understand and contribute to you code's notes.")
    responseText=""
    fileNameToWrite = ""
    #use try and except catch blocks to succesfully retrieve a valid file from the user
    try:
        #prompt them for a file name, read that file, then call the api with the text string
        fileName = input("Type the file name you want documented:")
        testFileName = open(fileName)
        fileNameToWrite = fileName
        inputText = autodoc.readFile(fileName)
        responseText = autodoc.call_api(inputText)
    except FileNotFoundError:
        print("File not found. Please check the file name and try again")
    except IOError:
        print("Error while reading the file. Please ensure the file is accessible and try again")
    except Exception as e:
        print("An error occurred:", str(e))
    
    ##content = api_response.json()["choices"][0]["message"]["content"]

     # write the file
    autodoc.writeFile(responseText, fileNameToWrite)
    #store in Database
    my_dict = {'fileName': fileName, 'inputText': inputText, 'outputText': responseText}
    data = pd.DataFrame.from_dict([my_dict])
    engine = db.create_engine('sqlite:///autodoc.db')
    data.to_sql('autodocHistory', con=engine, if_exists='replace', index=False)
    
    responseFromUserOnSeeingDatabaseEntry = input("would you like to see your database? Enter only yes or no: ")
    responseFromUserOnSeeingDatabaseEntry.lower()
    if (responseFromUserOnSeeingDatabaseEntry == "yes"): 
        with engine.connect() as connection:
            query_result = connection.execute(db.text("SELECT * FROM autodocHistory;")).fetchall()
            print(pd.DataFrame(query_result))


   
