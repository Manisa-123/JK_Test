import logging 
import requests
import asyncio

async def download_wikipedia_article(title):

    print(f"Download of Wiki Started for {title}")
   
    endpoint="https://en.wikipedia.org/w/api.php" # wikipedia endpoint to download the content
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "titles": title
    }

    # Make the API request
    try:
        response = requests.get(endpoint, params=params)
        data = response.json()
    except:
        print(f"Error while downloadging the Wiki Page {title}")
        return
        # raise HttpException("Error while downloadging the Wiki Page")

    # Extract the page content
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))
    content = page.get("extract", "No content found")
    if not content:
        print(f"No content found for {title}")
        return
    print("Download Completed")
    return content

async def count_words(content):
    words = content.split()  # splitting the words into a list to find the length
    return len(words)

async def write_title_and_word_count_to_file(title, word_count):
    filename='result.txt'
    with open(filename, 'a') as file:
        file.write(f"{title}:{word_count}\n") # writes the title and the count of the words to results.txt file
        
    print(f"Count of words of wiki page for {title} written to results.txt")



article_python = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# title= article_python.split('/')
# title=title[-1]
# print(title)
# content =download_wikipedia_article(title)
# content_word_count = count_words(content) 
# write_title_and_word_count_to_file(title, content_word_count)
# # print(content)


# async def main():
#     await asyncio.gather(download_wikipedia_article("India"), download_wikipedia_article("Tanilnadu"))

async def get_word_count_of_wiki_page(title):
    if '/' in title:
        title=title.split('/')
        title=title[-1]
    
    content =await download_wikipedia_article(title)
    content_word_count = await count_words(content) 
    await write_title_and_word_count_to_file(title, content_word_count)



async def main():
    await asyncio.gather(get_word_count_of_wiki_page("https://en.wikipedia.org/wiki/Python_(programming_language)"), get_word_count_of_wiki_page("India"))



asyncio.run(main())
