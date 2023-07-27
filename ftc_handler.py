import base64
import json #Needed to create the Authorization token
import requests #The library to access APIs that are based on REST

"""
NOTE To know the response schema for any API call refer to the FTC API documentation.
NOTE any manipulation of the JSON to extract more specific information from the response schema
should be done in this file.
"""

#NOTE there are information about Alliance Selection, Awards, and Leagues which we can explore.

"""
Contains the constants that all or almost all requests require.
"""
class Constents:
    
    token_file = open('ftc_token.txt', 'r')

    #The steps needed to be taken to frist create the authorization token
    __STRING = token_file.readline()
    __TOKEN = base64.b64encode(__STRING.encode('ascii')).decode('ascii')

    #The header for Authorization needed in all requests
    HEADERS = {
        'Authorization': 'Basic ' + __TOKEN
    }

"""
All infromation about the season.
"""
class FTCSeasonData():
    
    """
    Returns a high level glance of a particular season. Uses the GET Season Summmary.

    season: int  Numeric year of the event and must be four digits.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def season_summary(season: int):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}'

        response = requests.get(url, headers=Constents.HEADERS)
        return json.loads(response.text)

"""
All information about events.
""" 
class EventData():

    #NOTE can have a method to return the event schedule of the entire day and of a specific team

    #NOTE can add eventCode query parameter to pull information on a specific event not all of them
    #NOTE can be used to pull the address of the competition and the livestream url through knowing the specific eventCode or teamNumber.
    """
    Returns all events listed in a particular FTC season. Uses the GET Event Listings.

    season: int  Numeric year of the event and must be four digits.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def all_event_listings(season: int):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/events'

        response = requests.get(url, headers=Constents.HEADERS)
        return json.loads(response.text)
    
    """
    Returns information about all events a specific team has attended.

    season: int  Numeric year of the event and must be four digits.
    teamnumber: int Nemeric team number of a team which attending event listings are requested.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def team_at_event(season: int, teamnumber: int):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/events'
        parameters = {
            'teamNumber': teamnumber
        }

        response = requests.get(url, headers=Constents.HEADERS, params=parameters)
        #print(json.dumps(response.json(), sort_keys=False, indent=4)) uncomment this to locate at the potential useful data
        return json.loads(response.text)
    
    """
    Returns the entire ranking list at an event in a particular season.

    season: int  Numeric year of the event and must be four digits.
    eventCode: str Case insensitive alphanumeric eventCode of the event and must be at least 3 characters.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def event_rankings(season: int, eventCode: str):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/rankings/{eventCode}'

        response = requests.get(url, headers=Constents.HEADERS)
        return json.loads(response.text)

"""
Obtains information reqarding a specific team or multiple teams.
"""
class TeamData():
    
    #NOTE can use eventCode or province name to get information about all teams at an event
    """
    Returns all information regarding about all teams in a particular season.

    season: int  Numeric year of the event and must be four digits.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def all_team_info(season: int):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/teams'

        response = requests.get(url, headers=Constents.HEADERS)
        return json.loads(response.text)
    
    """
    Returns all information on a specific team.

    season: int  Numeric year of the event and must be four digits.
    teamnumber: int Nemeric team number who you want data on.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def team_info(season: int, teamNumber: int):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/teams'
        parameters = {
            'teamNumber': teamNumber
        }

        response = requests.get(url, headers=Constents.HEADERS, params=parameters)
        #print(json.dumps(response.json(), sort_keys=False, indent=4))
        return json.loads(response.text)
    
    """
    Returns the ranking information about a specific team at a specific event in a particular season.

    season: int  Numeric year of the event and must be four digits.
    eventCode: str Case insensitive alphanumeric eventCode of the event and must be at least 3 characters.
    teamnumber: int Nemeric team number who you want data on.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def team_event_ranking(season: int, eventCode: str, teamNumber: int):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/rankings/{eventCode}'
        parameters = {
            'teamNumber': teamNumber
        }

        response = requests.get(url, headers=Constents.HEADERS, params=parameters)
        return json.loads(response.text)

"""
To get the results of a match and score either for the entire event or a specific team.
"""
class MatchData():
    
    """
    The match results for all matches of a particular event and season.

    season: int  Numeric year of the event and must be four digits.
    eventCode: str Case insensitive alphanumeric eventCode of the event and must be at least 3 characters.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def all_event_match_results(season: int, eventCode: str):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/matches/{eventCode}'

        response = requests.get(url, headers=Constents.HEADERS)
        return json.loads(response.text)
    
    """
    The match results for a specific team in a particular event and seaosn.

    season: int  Numeric year of the event and must be four digits.
    eventCode: str Case insensitive alphanumeric eventCode of the event and must be at least 3 characters.
    teamnumber: int Nemeric team number who you want data on.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def team_match_results(season: int, eventCode: str, teamNumber: int):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/matches/{eventCode}'
        parameters = {
            'teamNumber': teamNumber
        }

        response = requests.get(url, headers=Constents.HEADERS, params=parameters)
        return json.loads(response.text)
    
    """
    The match results of a specific match in a particular event and season.

    season: int  Numeric year of the event and must be four digits.
    eventCode: str Case insensitive alphanumeric eventCode of the event and must be at least 3 characters.
    matchNumber: int specific single matchNumber of result.
    Returns -> a dicitonary representation of the JSON repsonse schema.
    """
    @staticmethod
    def match_results(season: int, eventCode: str, matchNumber: int):
        url = f'http://ftc-api.firstinspires.org/v2.0/{season}/matches/{eventCode}'
        parameters = {
            'teamNumber': matchNumber
        }

        response = requests.get(url, headers=Constents.HEADERS, params=parameters)
        return json.loads(response.text)