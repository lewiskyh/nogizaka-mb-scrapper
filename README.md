# Nogizaka46 Member Data Scraper

This project is designed to scrape data about the members of the Japanese idol group Nogizaka46 from the official website. It collects information such as member names, image URLs, and profile details, and stores this data in MongoDB for easy retrieval and use in various applications.

## Features

- **Data Scraping**: Automatically scrapes data using Python requests.
- **Data Parsing**: Parses JSON data and extracts detailed member information.
- **Database Integration**: Stores the scraped data in MongoDB Cloud, including member images and profile links.

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
   git clone https://github.com/lewiskyh/nogizaka-mb-scrapper.git

2. Nagivate to the project directory:
   ```bash
   cd nogizaka-mb-scraper
   
3. Install the Python packages:
   ```bash
   pip3 install -r requirements.txt

### Configuration

1. Create a '.env' file in the project root direcdtory

2. Add the following variables:
   ```bash
   DB_URI=mongodb+srv://<username>:<password>@<your-mongodb-cluster>/test?retryWrites=true&w=majority
   DB_NAME=<your-database-name>
   COLLECTION_NAME=<your-collection-name>

## Usage

To run the script by executing:
   ```bash
   python fetch-and-save-todb.py
   ```
This will start the scraping process, and the scraped data will be stored in your MongoDB database. You will then be able to view the data in your MongoDB database by accessing your MongoDB Atlas cluster.
