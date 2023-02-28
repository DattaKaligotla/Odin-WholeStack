import os
import openai as ai
import wandb
import user
class GPTDriver:
    def __init__ (self,userInfo,userId,userMood,article,prompt):
        self.APIkey = "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"
        self.userInfo = userInfo
        self.userId = userId
        self.article = article 
        self.prompt = prompt
        self.userMood = userMood
        self.outputArticle = None
        self.outputTitle = None
        self.userArticleGen = "Generate me just an article based on the following input article: " + article 
        + "make it interesting and connect to the topics this user likes, if it is relevant enough to those:" + str(userInfo) 
        + "write it in the tone the user wants the article:" + userMood
    def generateOutputArticle(self):
        ai.api_key = 'sk-somekeygoeshere'
        completions = ai.Completion.create(
            engine='text-davinci-003',  # Determines the quality, speed, and cost.
            temperature=0.5,            # Level of creativity in the response
            prompt=self.userArticleGen,           # What the user typed in
            max_tokens=500,             # Maximum tokens in the prompt AND response
            n=1,                        # The number of completions to generate
            stop=None,                  # An optional setting to control response generation
        )
        self.outputArticle = completions.choices[0].text
    def getOutputArticle(self):
        if(self.outputArticle != None):
            return self.outputArticle
        else:
            return "Article is Empty"
    def generateOutputTitle(self):
        if(self.outputArticle != None):
            ai.api_key = 'sk-somekeygoeshere'
            userTitleGen = "Just Give me an Article Name based on the following article:" + self.outputArticle
            completions = ai.Completion.create(
                engine='text-davinci-003',  # Determines the quality, speed, and cost.
                temperature=0.5,            # Level of creativity in the response
                prompt=userTitleGen,           # What the user typed in
                max_tokens=50,             # Maximum tokens in the prompt AND response
                n=1,                        # The number of completions to generate
                stop=None,                  # An optional setting to control response generation
            )
            self.outputTitle = completions.choices[0].text
        else:
            return "Article is Empty"
    def getOutputTitle(self):
        if(self.outputTitle != None):
            return self.outputTitle
        else:
            return "Title is Empty"
        
        
        
        