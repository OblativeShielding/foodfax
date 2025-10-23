# FoodFax

A collaborative HCI project that uses Optical Character Recognition (OCR) to extract nutritional information from food label images and track daily macro intake.

## Project Overview

FoodFax is a web application that allows users to upload images of food nutrition labels and automatically extract macro information (protein, fat, carbohydrates, calories) using computer vision technology. The application provides a clean interface for tracking daily nutritional intake without manual data entry.

## Team Members

- **OblativeShielding** (Joseph) - Project Lead, Documentation
- **mowery39** (Kaleb) - Testing, Video Documentation  
- **J** (Jalen) - Primary Developer, Backend/Frontend Implementation
- **Thugmelon** - Documentation, Feature Development

## Technical Stack

- **Backend**: Python Flask with EasyOCR
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **OCR Engine**: EasyOCR for text extraction
- **Data Processing**: Regex pattern matching for nutrition parsing

## Features

- **Image Upload**: Support for PNG, JPG, JPEG formats
- **OCR Processing**: Automatic text extraction from nutrition labels
- **Macro Tracking**: Real-time calculation of protein, fat, and carbohydrate totals
- **Results Table**: Individual meal breakdown with running totals
- **Debug Mode**: Raw OCR text display for troubleshooting
- **Responsive Design**: Works on desktop and mobile devices

## Installation & Setup

1. **Install Python Dependencies**:
   ```bash
   pip install flask flask-cors easyocr
   ```

2. **Run the Backend Server**:
   ```bash
   python ImageReader.py
   ```

3. **Access the Application**:
   - Open `foodFax.html` in a web browser
   - Or use a local server (VS Code Live Server extension recommended)

## Usage

1. Click "Add Meal" button
2. Select an image of a food nutrition label
3. The application will automatically:
   - Extract text using OCR
   - Parse nutritional information
   - Add to your daily totals
   - Display results in the table

## Project Status

- Code implementation complete
- Video demonstration recorded
- Lo-fi prototype documentation
- Ongoing feature development

## Future Enhancements

- **Data Visualization**: Pie charts and bar graphs for macro breakdown
- **Data Persistence**: Save meal history and user progress
- **Goal Tracking**: Set and monitor daily macro targets
- **Camera Integration**: Direct photo capture functionality
- **Food Database**: Validation against nutrition databases

## Development Notes

- Backend runs on `localhost:5000`
- CORS enabled for cross-origin requests
- Error handling for failed OCR processing
- Responsive grid layout for optimal viewing
- Real-time table updates with JavaScript

## Troubleshooting

- Ensure Python server is running before accessing HTML file
- Check that all required libraries are installed
- Verify image format (PNG, JPG, JPEG only)
- Use browser developer tools for debugging API calls

---