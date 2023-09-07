# Symptom Checker

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation and Usage](#installation-and-usage)
- [API Endpoints](#api-endpoints)
- [Disclaimer](#disclaimer)
- [Conclusion](#conclusion)

## Introduction <a name="introduction"></a>

The Symptom Checker app is a healthcare tool built using FastAPI and
Python that allows users to input their age, gender, and symptoms they
are experiencing. Based on this information, the app provides a
preliminary assessment of potential health conditions or
recommendations. The app utilizes OpenAI's advanced language processing
capabilities to offer users a quick and convenient way to assess their
health status.

## Features <a name="features"></a>

- User-friendly API for submitting age, gender, and symptoms data.
- Leveraging OpenAI's language model to analyze input and generate
  health-related insights.
- Provides instant preliminary assessment of potential health
  conditions.
- Helps users make informed decisions about seeking medical attention.
- Privacy-conscious design, with no personal data stored beyond the
  session.

## Installation and Usage <a name="installation-and-usage"></a>

1. **Clone the repository to your local machine:**

   git clone https://github.com/Roseford/symptom-checker.git

2. **Navigate to the app's directory:**

   cd symptom-checker

3. **Install required Python packages:**

   pip install -r requirements.txt

4. **Run the FastAPI app:**

   uvicorn main:app --reload

5. **Access the API documentation**

   Access the app's API documentation through your web browser at:
   http://localhost:8000/docs.

## API Endpoints <a name="api-endpoints"></a>

- POST /check-symptoms: Submit age, gender, and symptoms data to receive
  a preliminary health assessment.

## Disclaimer <a name="disclaimer"></a>

The Symptom Checker app is intended to provide general information and
is not a substitute for professional medical advice. Users should always
consult with a qualified healthcare provider for accurate diagnosis and
treatment recommendations.

## Conclusion <a name="conclusion"></a>

The Symptom Checker app aims to empower users with initial health
assessments based on their provided information. By combining FastAPI's
efficient backend framework and OpenAI's language processing
capabilities, the app offers a streamlined and user-friendly experience.
As with any medical tool, it's essential to remember that the app is not
a replacement for professional medical advice. We hope that this app
proves valuable in helping users make informed decisions about their
health and wellness.

**Thank you for your interest in the Symptom Checker app!**
