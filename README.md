# SW Club Chatbot
I worked on a chatbot project aimed at improving the club's website at the Software Entrepreneurship Club. After studying software fundamentals and acquiring basic backend knowledge, I began the project. Although it was my first time using HTML and web server tools, I approached the project with great interest.

The main goal of the project was to add a chatbot function to the website, allowing users to address any questions they had about the club. While the implementation and integration of the chatbot were successfully completed, I wasn't able to develop the functionality for the model to learn and respond based on the website's content. This aspect was left as a future development task.

Through this project, I was able to acquire important skills in web development and chatbot integration, and it remains a project with significant potential for further development.

## Skills

- **Flask**: Used to build a web server that processes questions input by users in the chatbot search box and returns appropriate responses, based on the Python-based micro web framework.
- **flask-sock**: Supports real-time communication through WebSockets, allowing user queries entered in the search box to be immediately sent to the server for quick chatbot responses.
- **OpenAI API**: Calls OpenAI's natural language processing model to generate answers to user-input questions, creating appropriate responses based on the content entered in the search box and returning them to the client.
- **JavaScript**: Implements actions such as handling button click events and resetting user input fields, providing functionality to clear the chatbot's conversation history or remove input content when the reset button is clicked.

## Creating a requirements.txt File

### Install Required Packages
- Flask
- flask-sock
- openai

### Generate requirements.txt
```
pip freeze > requirements.txt
```

### For adding Your GitHub Repository
```
git add requirements.txt
git commit -m "Add requirements.txt"
git push
```

## Working
```
conda create -n joe python=3.9
```

```
git clone https://github.com/BinnieJoe/SW-Club-Chatbot.git
```

```
python app.py
```
