# DiabPredict

The goal of DiabPredict is to provide a reliable and efficient way to predict the likelihood of diabetes in patients. The project leverages machine learning techniques to analyze patient data and identify patterns that could indicate the presence of diabetes. The models are trained using a dataset containing various health metrics, and the project includes a feature engineering pipeline to enhance the predictive power of the models.

the project is broken into the following pipelines:
- [Backfill pipeline](#backfill-pipeline)
- [Replinshment pipeline](#replinshment-pipeline)
- [Model training pipeline](#model-training-pipeline)
- [Feature pipeline](#feature-pipeline)
- [Batch prediction pipeline](#batch-prediction-pipeline)


Backfill Feature Pipeline: Initially fill the feature group with historical data.<br>
Replinshment pipeline: Regularly update the feature group with new data.<br>
Training Pipeline: Train the model using the prepared data.<br>
Prediction Pipeline: Use the model to make predictions on new data.<br>
Detailed instructions for each pipeline can be found in the project documentation.

Installation Instructions
Clone the Repository

```bash
git clone https://github.com/Chukwukwadorom/DiabPredict.git
cd DiabPredict
```

Build Docker Image

Ensure you have Docker installed. Build the Docker image using:

```bash
sudo docker build -t diabpredict-streamlit-image .
Run the Docker Container
```

To run the application, use:

```bash
sudo docker run -d -p 8501:8501 --name diabpredict-streamlit-container --env-file .env diabpredict-streamlit-image
```
The application will be accessible at http://localhost:8501.

Usage Instructions
Environment Variables

Create a .env file in the project root with necessary environment variables. Example:


```
MLFLOW_TRACKING_URI=http://localhost:5000
HOPSWORKS_PROJECT_ID=your_project_id
HOPSWORKS_API_KEY=your_api_key
```

Running the Application

The Streamlit app can be accessed via the web browser at http://localhost:8501. The app allows you to input features and get predictions on diabetes.