# 🍷 End-to-End Wine Quality Prediction

A complete machine learning project for predicting wine quality using physicochemical properties. This project demonstrates end-to-end ML pipeline implementation with modular code structure, configuration management, and Flask web application deployment.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Workflows](#workflows)
- [API Endpoints](#api-endpoints)
- [Docker Deployment](#docker-deployment)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project predicts wine quality based on 11 physicochemical features:
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

The model is trained on the **Wine Quality Dataset** (Red Wine variant) and provides predictions through a user-friendly web interface.

## ✨ Features

- **Modular Code Architecture**: Well-structured components for data ingestion, validation, transformation, training, and evaluation
- **Configuration Management**: YAML-based configuration for easy parameter tuning
- **Pipeline Design**: Sequential stages for reproducible ML workflows
- **Web Interface**: Flask-based UI for real-time predictions
- **Docker Support**: Containerized deployment for easy scaling
- **Logging**: Comprehensive logging for debugging and monitoring
- **Exception Handling**: Robust error handling throughout the pipeline

## 📁 Project Structure

```
End-to-End-Wine-Quality-Prediction/
│
├── app.py                          # Flask application
├── main.py                         # Training pipeline orchestrator
├── Dockerfile                      # Docker configuration
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
├── template.py                     # Project template generator
│
├── config/
│   ├── config.yaml                 # Main configuration file
│   ├── params.yaml                 # Model parameters
│   └── schema.yaml                 # Data schema definition
│
├── data/
│   └── winequality-red.csv         # Dataset
│
├── src/mlProject/
│   ├── __init__.py
│   ├── components/                 # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── config/
│   │   └── configuration.py        # Configuration manager
│   │
│   ├── entity/
│   │   └── config_entity.py        # Data classes for configs
│   │
│   ├── pipeline/                   # Training & prediction pipelines
│   │   ├── stage_01_data_ingestion.py
│   │   ├── stage_02_data_validation.py
│   │   ├── stage_03_data_transformation.py
│   │   ├── stage_04_model_trainer.py
│   │   ├── stage_05_model_evaluation.py
│   │   └── prediction.py
│   │
│   ├── utils/
│   │   └── common.py               # Utility functions
│   │
│   └── constants/
│       └── __init__.py             # Project constants
│
├── research/                       # Jupyter notebooks for experimentation
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   └── 05_model_evaluation.ipynb
│
├── templates/                      # HTML templates
│   ├── index.html
│   └── results.html
│
└── static/                         # CSS, JS, and assets
    ├── css/
    ├── js/
    └── assets/
```

## 🚀 Installation

### Prerequisites
- Python 3.11 or higher
- Git

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/nandan-byte/End-to-End-Wine-Quality-Prediction.git
cd End-to-End-Wine-Quality-Prediction
```

2. **Create a virtual environment**
```bash
python -m venv mlproj
source mlproj/bin/activate  # On Windows: mlproj\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the package in editable mode**
```bash
pip install -e .
```

## 💻 Usage

### Training the Model

Run the complete training pipeline:

```bash
python main.py
```

This executes all five stages:
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation

### Running the Web Application

Start the Flask application:

```bash
python app.py
```

Access the application at: `http://localhost:8080`

### Making Predictions

1. Navigate to the home page
2. Enter wine characteristics in the form
3. Click "Predict Quality"
4. View the predicted quality score

## 🔄 Workflows

The project follows a systematic workflow:

1. **Update config.yaml** - Define data sources, artifacts paths
2. **Update schema.yaml** - Define data schema and column names
3. **Update params.yaml** - Set model hyperparameters
4. **Update entity** - Create configuration data classes
5. **Update configuration manager** - Handle config reading in `src/config`
6. **Update components** - Implement core ML logic
7. **Update pipeline** - Create stage-wise pipeline classes
8. **Update main.py** - Orchestrate all pipeline stages
9. **Update app.py** - Configure Flask routes and prediction endpoint

## 🔌 API Endpoints

### Home Page
```
GET /
```
Returns the main HTML page with input form.

### Training
```
GET /train
```
Triggers the complete ML training pipeline.

**Response:**
```
Training Successful!
```

### Prediction
```
POST /predict
```

**Request Body (Form Data):**
```json
{
  "fixed_acidity": 7.4,
  "volatile_acidity": 0.7,
  "citric_acid": 0.0,
  "residual_sugar": 1.9,
  "chlorides": 0.076,
  "free_sulfur_dioxide": 11.0,
  "total_sulfur_dioxide": 34.0,
  "density": 0.9978,
  "ph": 3.51,
  "sulphates": 0.56,
  "alcohol": 9.4
}
```

**Response:**
Renders `results.html` with predicted wine quality.

## 🐳 Docker Deployment

### Build the Docker Image

```bash
docker build -t wine-quality-app .
```

### Run the Container

```bash
docker run -p 8080:8080 wine-quality-app
```

Access the application at: `http://localhost:8080`

### Docker Compose (Optional)

Create a `docker-compose.yml`:

```yaml
version: '3.8'
services:
  wine-app:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./data:/app/data
    environment:
      - FLASK_ENV=production
```

Run with:
```bash
docker-compose up
```

## 🛠️ Technologies Used

### Core Libraries
- **Python 3.11**: Programming language
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **Flask**: Web framework
- **Flask-Cors**: CORS handling

### Configuration & Utilities
- **PyYAML**: YAML parsing
- **python-box**: Box configuration
- **ensure**: Type checking
- **joblib**: Model serialization
- **tqdm**: Progress bars

### Visualization
- **matplotlib**: Data visualization

## 📊 Model Details

The project uses scikit-learn's machine learning algorithms. Key aspects:

- **Algorithm**: Configurable through `params.yaml`
- **Evaluation Metrics**: R², RMSE, MAE
- **Data Split**: Train-test split defined in configuration
- **Feature Engineering**: Handled in data transformation stage

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Nandan Deshamukh**
- Email: nandandeshamukh9845@gmail.com
- GitHub: [@nandan-byte](https://github.com/nandan-byte)

## 🙏 Acknowledgments

- Wine Quality Dataset from UCI Machine Learning Repository
- Flask framework documentation
- scikit-learn community

## 📧 Contact

For questions or feedback, please reach out:
- Email: nandandeshamukh9845@gmail.com
- GitHub Issues: [Create an issue](https://github.com/nandan-byte/End-to-End-Wine-Quality-Prediction/issues)

---

⭐ If you found this project helpful, please give it a star!
