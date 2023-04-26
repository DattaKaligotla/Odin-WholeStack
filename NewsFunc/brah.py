article = """Sundar Pichai is facing what may likely be Google’s biggest competitive challenge in the 25 years since it was founded.

His company's dominance in ad-rich search engine queries is under acute threat by Microsoft’s A.I.-enabled Bing just as heavy investments in Google Cloud mean the business continues to bleed red ink in an industry where profits seem to grow on trees for other hyperscalers.

Google CEO Pichai, who is now in the process of rushing out his own chatbot dubbed Bard to respond, is having to cut back elsewhere. Last month he received immediate pushback on a new policy that forces staff at his loss-making Cloud operations to share their desks with a partner.

In comments recorded on tape and obtained by CNBC, Pichai urged employees affected by his Cloud Office Evolution (CLOE) plan to remember that prime office real estate doesn’t come cheap in its five largest locations, including San Francisco and New York.

“There are people, by the way, who routinely complain that they come in and there are big swaths of empty desks,” he said last week. “It feels like a ghost town—it’s just not a nice experience.”

There’s a simple motivation behind this penny-pinching: Parent company Alphabet is under pressure.

That is because once you take Google’s search engine revenue away, more than half of the group’s $282 billion in annual revenue disappears. Subtract YouTube from the remainder and what's left is essentially a mishmash of loss-making activities.

Google's hardware business—including its Pixel mobile phone, Nest home products, and Fitbit wearable devices—doesn’t move the needle, and annual revenue pulled in by its Google Play app store actually decreased, according to its latest 10-K filing.

In September, the company said it would begin shutting down its Stadia video game streaming division, and, to add insult to injury, veteran YouTube boss Susan Wojcicki is stepping down just when TikTok is rapidly growing its audience through a laser-like focus on viral short-form videos.

Google did not immediately respond to Fortune's request for comment.

Growing Google Cloud has been a strategic priority for Pichai
But Google’s cloud business has promise thanks to the rapidly growing need for remote data processing. Rival hyperscalers Amazon Web Services and Microsoft Azure rake in profits by the truckload, renting out their data centers’ excess computing power to corporate customers looking to avoid the fixed costs of maintaining their own.

Growing Google Cloud has consequently been a major priority for Pichai ever since he took over running the company in 2015.

While the division’s top line soared 37% last year to over 26 billion euros, its operating loss stayed virtually flat at $3 billion. Alphabet finance chief Ruth Porat, who guided for a "meaningful" decrease in office-related capex this year, merely said last month she remained "very focused on the path to profitability" at Google Cloud.

That’s why Pichai sought to conserve cash by consolidating office space, even as he apologized to staff for trying to sugarcoat the news last month.

“We should be good stewards of financial resources,” Pichai said, according to CNBC. “We have expensive real estate. And if they’re only utilized 30% of the time, we have to be careful in how we think about it.”

Search engine subsidies
The constant cross-subsidization of Alphabet’s sundry loss-making businesses using search engine profits has Cathie Wood’s ARK Invest believing that tripping up Google's cloud ambitions could be a secondary aim of Microsoft's A.I. push.

Her analysts argue CEO Satya Nadella aims to exert enough pressure on Google with its new A.I.-enabled Bing that investors force Pichai to dial back his investments in Cloud to protect margins.

This could then cede valuable market share to Azure. Microsoft’s rival hyperscaler earns a 40%-plus return on sales, translating into $8.9 billion in operating profits during just the past fiscal second-quarter alone.

With 6% of Google's global workforce slated to lose their jobs, conserving desk space should therefore be the least of Googlers' concerns right now.   """ 

import os
import openai as ai
import wandb
import user
userInfo = ["NFL", "Cologne", "Jalen Hurts", "Philadelphia Eagles"]
import secrets
thing = secrets.choice(userInfo)
userMood = "funny"
readingLevel = "Normal"
userArticleGen = f"Here is the input article:{article}, rewrite the article in a way that connects key concepts to the following user interest: {thing}, also write in the following way: {userMood}, also write it in this reading level for the user: {readingLevel}"
ai.api_key = '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'
completions = ai.Completion.create(
            engine='text-davinci-003',  # Determines the quality, speed, and cost.
            temperature=0.75,            # Level of creativity in the response
            prompt=userArticleGen,           # What the user typed in
            max_tokens=500,             # Maximum tokens in the prompt AND response
            n=1,                        # The number of completions to generate
            stop=None,                  # An optional setting to control response generation
        )
outputArticle = completions.choices[0].text
userTitleGen = "Just Give me an Article title based on the following article:" + outputArticle + "and connect it to" + thing+ "in some way"  + "user reading level: " + readingLevel
completions = ai.Completion.create(
                engine='text-davinci-003',  # Determines the quality, speed, and cost.
                temperature=0.75,            # Level of creativity in the response
                prompt=userTitleGen,           # What the user typed in
                max_tokens=500,             # Maximum tokens in the prompt AND response
                n=1,                        # The number of completions to generate
                stop=None,                  # An optional setting to control response generation
            )
outputTitle = completions.choices[0].text
print(outputTitle)

print(outputArticle)
print(thing)