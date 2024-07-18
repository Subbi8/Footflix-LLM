import os
import pandas as pd
import requests
import json
import plotly.graph_objects as go

# Translation table for special characters
translation_table = {
    'à': 'a', 'á': 'a', 'â': 'a', 'ä': 'a', 'ǎ': 'a', 'æ': 'a', 'ã': 'a', 'å': 'a', 'ā': 'a', 'ă': 'a', 'ą': 'a',
    'À': 'A', 'Á': 'A', 'Â': 'A', 'Ä': 'A', 'Ǎ': 'A', 'Æ': 'A', 'Ã': 'A', 'Å': 'A', 'Ā': 'A', 'Ă': 'A', 'Ą': 'A',
    'Ë': 'e', 'é': 'e', 'è': 'e', 'ê': 'e', 'ě': 'e', 'ẽ': 'e', 'ē': 'e', 'ė': 'e', 'ę': 'e',
    'Ë': 'E', 'É': 'E', 'È': 'E', 'Ê': 'E', 'Ě': 'E', 'Ẽ': 'E', 'Ē': 'E', 'Ė': 'E', 'Ę': 'E',
    'Î': 'i', 'ì': 'i', 'í': 'i', 'ï': 'i', 'ǐ': 'i', 'ĩ': 'i', 'ī': 'i', 'ı': 'i', 'į': 'i',
    'Î': 'I', 'Ì': 'I', 'Í': 'I', 'Ï': 'I', 'Ǐ': 'I', 'Ĩ': 'I', 'Ī': 'I', 'İ': 'I', 'Į': 'I',
    'O': 'o', 'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o', 'ǒ': 'o', 'œ': 'o', 'ø': 'o', 'õ': 'o', 'ō': 'o', 'ő': 'o',
    'O': 'O', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Ö': 'O', 'Ǒ': 'O', 'Œ': 'O', 'Ø': 'O', 'Õ': 'O', 'Ō': 'O', 'Ő': 'O',
    'Ǔ': 'u', 'û': 'u', 'ù': 'u', 'u': 'u', 'ú': 'u', 'ü': 'u', 'ũ': 'u', 'ū': 'u', 'ű': 'u', 'ů': 'u', 'ų': 'u',
    'Ǔ': 'U', 'Û': 'U', 'Ù': 'U', 'Ú': 'U', 'Ü': 'U', 'Ũ': 'U', 'Ū': 'U', 'Ű': 'U', 'Ů': 'U', 'Ų': 'U',
    'Y': 'y', 'ý': 'y', 'ÿ': 'y', 'ŷ': 'y',
    'Y': 'Y', 'Ý': 'Y', 'Ÿ': 'Y', 'Ŷ': 'Y',
    'Ṣ': 's', 'ś': 's', 's̤': 's', 's̱': 's', 'ş': 's', 'ș': 's', 'š': 's', 'ß': 's',
    'Ṣ': 'S', 'Ś': 'S', 'S̤': 'S', 'S̱': 'S', 'Ş': 'S', 'Ș': 'S', 'Š': 'S', 'ẞ': 'S',
    'Z': 'z', 'ẓ': 'z', 'z̤': 'z', 'ž': 'z', 'ź': 'z', 'ż': 'z',
    'Z': 'Z', 'Ẓ': 'Z', 'Z̤': 'Z', 'Ž': 'Z', 'Ź': 'Z', 'Ż': 'Z',
    'Ń': 'n', 'ň': 'n', 'ņ': 'n', 'ṅ': 'n', 'ñ': 'n', 'ṇ': 'n', 'ṉ': 'n', 'ń': 'n',
    'Ń': 'N', 'Ň': 'N', 'Ņ': 'N', 'Ṅ': 'N', 'Ñ': 'N', 'Ṇ': 'N', 'Ṉ': 'N', 'Ń': 'N'
}

# Load the Excel file
file_path = r'C:\Users\shubham\OneDrive\Desktop\CS Projects\Footy_LLM\Book1.xlsx'
data = pd.read_excel(file_path, skiprows=2)

# Function to generate the scouting report using the external API
def generate_scouting_report(player_name, position, age, team, player_stats):
    # Constructing the prompt specifically for strengths and weaknesses
    prompt = f"""
    Here are the strengths and weaknesses of {player_name}:

    Strengths:
    - Describe the key strengths of {player_name} in his position.

    Weaknesses:
    - Identify areas of improvement for {player_name}.

    Player: {player_name}
    Position: {position}
    Age: {age}
    Team: {team}
    """
  '''Use your Desired Model to extract results '''
    
    
    print("Response Status Code:", response.status_code)

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    scouting_report = ""
    for chunk in response.iter_content(chunk_size=None):
        if chunk:
            try:
                response_json = json.loads(chunk)
                if 'response' in response_json:
                    scouting_report += response_json['response']
            except ValueError:
                pass

    return scouting_report

def fetch_football_scores(date):
    api_key = "Replace with your football-data.org API key"   
    base_url = 'https://api.football-data.org/v2/'
    headers = {
        'X-Auth-Token': api_key
    }

    endpoint = f'matches?dateFrom={date}&dateTo={date}'
    url = base_url + endpoint

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            matches = response.json()['matches']
            scores = []
            for match in matches:
                home_team = match['homeTeam']['name']
                away_team = match['awayTeam']['name']
                score = match['score']['fullTime']
                scores.append(f"{home_team} vs {away_team}: {score['homeTeam']} - {score['awayTeam']}")
            return scores
        else:
            return []
    except requests.exceptions.RequestException as e:
        return []

def find_player_and_generate_report(player_name):
    normalized_name = normalize_player_name(player_name)

    player_data = data[data['Player'] == normalized_name]

    if player_data.empty:
        return f"No data found for player: {player_name}", None
    else:
        player_data = player_data.iloc[0]
        position = player_data['Pos']
        age = player_data['Age']
        team = player_data['Squad']
        player_stats = player_data.drop(['Player', 'Pos', 'Age', 'Squad'])

        # Generate the scouting report
        scouting_report = generate_scouting_report(player_name, position, age, team, player_stats)
        return scouting_report, player_stats

# Function to normalize player name using translation table
def normalize_player_name(player_name):
    for char in translation_table:
        player_name = player_name.replace(char, translation_table[char])
    return player_name

# Function to generate radar chart for player comparison
def generate_radar_chart(player1_stats, player2_stats, player1_name, player2_name):
    # Filter for the required statistics
    stats_to_include = ['G+A', 'Goals', 'Assists', 'Min', 'PrgC', 'PrgP']
    player1_stats = player1_stats[stats_to_include]
    player2_stats = player2_stats[stats_to_include]
    
    categories = player1_stats.index.tolist()

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=player1_stats.values,
        theta=categories,
        fill='toself',
        name=player1_name
    ))
    fig.add_trace(go.Scatterpolar(
        r=player2_stats.values,
        theta=categories,
        fill='toself',
        name=player2_name
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 90] 
            )),
        showlegend=True
    )

    fig.show()

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Sia: Goodbye!")
        break
    elif any(greeting in user_input.lower() for greeting in ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']):
        greetings_responses = ["Hi!", "Hello!", "Hey!", "Good to see you!", "Greetings!"]
        import random
        print(f"Sia: {random.choice(greetings_responses)}")
    elif 'scout' in user_input.lower() or 'player' in user_input.lower():
        player_name = input("Sia: Enter the player's name: ")
        scouting_report, player_stats = find_player_and_generate_report(player_name)
        if scouting_report:
            print(f"Sia: Scouting Report for {player_name}:\n{scouting_report}\n")
            print(f"Sia: Statistics for {player_name}:\n{player_stats.to_markdown()}\n")
        else:
            print(f"Sia: No data found for player: {player_name}")
    elif 'score' in user_input.lower() or 'match' in user_input.lower():
        match_date = input("Sia: Enter the match date (YYYY-MM-DD): ")
        scores = fetch_football_scores(match_date)
        if scores:
            print("\nSia: Football Scores:")
            for score in scores:
                print(score)
        else:
            print("Sia: No matches found for the specified date.")
    elif 'compare' in user_input.lower():
        player1_name = input("Sia: Enter the first player's name: ")
        player2_name = input("Sia: Enter the second player's name: ")

        _, player1_stats = find_player_and_generate_report(player1_name)
        _, player2_stats = find_player_and_generate_report(player2_name)

        if player1_stats is not None and player2_stats is not None:
            generate_radar_chart(player1_stats, player2_stats, player1_name, player2_name)
        else:
            print(f"Sia: Could not find data for one or both players: {player1_name}, {player2_name}")
    else:
        print("Sia: I'm sorry, I don't have information on that topic yet. Feel free to ask me about players or football scores.")
