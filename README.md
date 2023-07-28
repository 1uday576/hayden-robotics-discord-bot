# hayden-robotics-discord-bot
Repository for Hayden Robotics' Discord server bot done with Andrew Jiang.

This is code that is used to create a Discord server bot that allows users to interact with the **Google Classroom API** and the **FTC API** through a discord server. Thus, making it easy for users to not only get information from FTC but also get updates from Google Classroom in a server to communicate with your fellow teammates.

## Google Classroom API 

Able to retrieve the announcement posts made on the Google Classroom either through a call or from retrieving any new posts.

## FTC API

The FTC (First Tech Challenge) API is a REST API which specifically exposes various GET endpoints where we can query for different information which includes team info, event results, rankings, and schedules. The specific ftc_handler.py primary job is to make those GET requests passing in the path and query parameters and then return python objects of the JSON results. There are methods that pull more specific information than just a JSON scheme like the address and livestream Url.
