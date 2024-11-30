import json

# Load FAQ and Resources data
with open('data/faq.json', 'r') as faq_file:
    faq_data = json.load(faq_file)

with open('data/resources.json', 'r') as resources_file:
    resources_data = json.load(resources_file)

def process_input(query):
    """ Process the text input to answer FAQs """
    # Check if the query matches any FAQ
    if query in faq_data:
        return faq_data[query]
    else:
        return "Sorry, I don't have an answer to that question. You can ask me about various subjects like Python, Data Science, etc."

def share_resources(topic):
    """ Share resources for a specific topic """
    if topic in resources_data:
        resource_list = "\n".join([f"{item['title']}: {item['url']}" for item in resources_data[topic]])
        return f"Here are some resources for {topic}:\n{resource_list}"
    else:
        return f"Sorry, I don't have resources for {topic} at the moment."
