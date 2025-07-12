# Cat vs Dog Classifier

A full-stack web application to classify images as cat or dog using a PyTorch model and Django backend.

## Features
- Image upload and prediction
- User authentication (email & Google via django-allauth)
- Token system (each prediction costs tokens)
- Prediction history
- Responsive UI

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Cat-VS-Dog-Classifier.git
cd Cat-VS-Dog-Classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
Use the provided script or download from Kaggle. See EDA/perform_eda.ipynb for data exploration.

### 4. Train the model
Train your model in Google Colab or locally. Save the `.pth` file in the project root.

### 5. Django setup
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Optional, for admin access
python manage.py runserver
```

### 6. Access the app
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Development Notes
- Media uploads are stored in the `media/` folder (excluded from git).
- Model weights (`*.pth`) are excluded from git.
- Emails are printed to the console for development.
- For production, configure a real email backend and secure settings.

## Credits
- Dataset: [Kaggle - Dog and Cat Classification Dataset](https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset)
- PyTorch, Django, django-allauth.
