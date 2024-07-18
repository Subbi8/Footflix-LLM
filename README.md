
# Footflix-LLM

## Introduction
a Football LLM , This project aims to provide a comprehensive tool for scouting football players and comparing their statistics using data from an Excel file and external APIs.

## Project Overview
The tool fetches player data from an Excel sheet, normalizes player names using a translation table, generates scouting reports using an external API (llama3), fetches live football scores from football-data.org, and compares player statistics using radar charts.

## Tech Stack Used
- Python
- Flask (for backend)
- React (for frontend)
- Pandas (data handling)
- Requests (API calls)
- Plotly (for radar charts)
- Excel (for data storage)

## Key Components and Functionality

### Data Handling and Normalization
The project reads player data from an Excel file, normalizes player names using a translation table to handle special characters efficiently.

### Scouting Report Generation
The `generate_scouting_report` function constructs prompts for strengths and weaknesses of a player and sends a POST request to an external API (llama3) to generate detailed scouting reports.

### Live Football Scores
The `fetch_football_scores` function fetches live football scores for matches on a specified date using the football-data.org API.

### Player Comparison with Radar Charts
The `generate_radar_chart` function generates radar charts comparing key statistics (goals, assists, etc.) between two players.

## Commands
- `score` or `match`: Fetch live football scores for matches on a specific date.
- `scout` or `player`: Generate a scouting report and display statistics for a specific player.
- `compare`: Compare statistics between two players and visualize the comparison using radar charts.

