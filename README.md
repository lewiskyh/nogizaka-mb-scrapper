# Nogizaka46 Member Data Scraper

This project is designed to scrape data about the members of the Japanese idol group Nogizaka46 from their official website. It collects information such as member names, images, and profile details, and stores this data in MongoDB for easy retrieval and use in various applications.

## Features

- **Data Scraping**: Automatically scrapes data using Python requests.
- **Data Parsing**: Parses JSON data and extracts detailed member information.
- **Database Integration**: Stores the scraped data in MongoDB, including member images and profile links.
- **Error Handling**: Robust error handling to manage network issues and data inconsistencies.

## Technologies Used

- Python 3
- PyMongo
- Requests
- Python-dotenv
- MongoDB Atlas
- Certifi (for SSL certificate validation)

## Setup

To run this project, you will need to install some Python packages and set up MongoDB Atlas.

### Prerequisites

- Python 3.8 or above
- Pip (Python package installer)
- MongoDB Atlas account

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-github-username>/nogizaka46-scraper.git
