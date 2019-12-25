# nasa-apod-frontend
This Flask application acts as a frontend for the  [NASA APOD API](https://api.nasa.gov/). After selecting a specific date, it returns the NASA Astronomical Pictuer of the Day for the specific day chosen. The user can choose whether to show a high/low resolution image, and can export it to pdf, including a short caption. The [jsPDF library](https://github.com/MrRio/jsPDF) was used in order to export to pdf.

## Running
In order to run the app, you need to install Flask. After installing Flask, you can simply run the app using `python3 application.py' inside the repository root directory.