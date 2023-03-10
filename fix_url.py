import re
import codecs

standard_url = r"https://www\.random\.com/lol/\S+"

normalized_urls = []

with codecs.open("tt_urls.txt", "r", "utf-8") as f:
    for line in f:
        match = re.match(standard_url, line)
        if match:
            normalized_urls.append(match.group())

with codecs.open("cleaned_urls.txt", "w", "utf-8") as f:
    for url in normalized_urls:
        f.write(url + "\n")

        
# Summary: 
# First I have imported two modules regular expression and codecs. Then I have created standard_url variable to match the standard format of URL

# Second. Opened the file using codecs.open() function and encoding="utf-8". Then I have wrote a for loop for the tt_urls.txt file to go thru each line of the text and match standard url format. After that if staement for adding cleaned urls to the list if it maches the standard url format.

# Third create a new file for normalized urls and save it each url in new line. As well using codecs.open() and encoding="utf-8".