import openai
from enum import Enum
from typing import Optional
from fastapi import FastAPI, Form, Request, Depends
from pydantic_settings import BaseSettings

app = FastAPI()

class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ".env"
settings = Settings()

openai.api_key = settings.openai_api_key

def generate_prompt(gender, age, symptoms):
    return """You are a healthcare assistant, List all the possible conditions associated with the symptom, symptoms assosiated with the different conditions, their overviews, causes and treatment options based on the gender, age and symptoms given.

Gender: female
Age: 21
Symptoms: cough, cold sensation , fever 100.5f to 102f , pain in upper body , pain below the waist
Possible conditions: Influenza (Flu) Adults
Symptoms assosiated: Fever, sore throat, runny nose, headache, muscle aches, cough, tiredness
Overview: The flu is a respiratory tract infection caused by the influenza virus. Flu symptoms include fever, sore throat, runny nose, headache, cough, muscle aches, and fatigue. The flu spreads easily from person to person. Most people recover at home with rest and over-the-counter medications, but for some people flu can be severe and even life-threatening. Young children, older adults, pregnant women, and people with health problems are at risk for complications from the flu, such as pneumonia. Prescription antiviral medication can reduce the duration of symptoms and help speed recovery. Getting a yearly flu vaccine is the best way to prevent the flu.
Causes: Smoking, having a weak immune system, being exposed to someone with the virus, having a job that involves contact with many people, such as a teacher or nurse
Treatment options: The flu usually gets better on its own in one to two weeks with rest. Antihistamines, decongestants, pain relievers, drinking plenty of fluids, and inhaling steam may help ease symptoms. For people at risk for complications and those with severe symptoms, antiviral medications such as oseltamivir (Tamiflu), baloxavir (Xofluza),peramivir (Rapivar), or orzanamivir (Relenza) may help reduce the duration of symptoms, shorten the illness, and prevent complications if they are taken soon after symptoms appear.

Gender: male
Age: 40
Symptoms: bladder loses feeling/unable to feel normal sensations , lower stomach pain , constipation , tiredness , muscle spasm , numbness tingling in chest
Possible conditions: Hypothyroidism (Adult)
Symptoms assosiated: Hypothyroid symptoms include weight gain, severe fatigue, weakness, slowed thinking, confusion, trouble concentrating, sensitivity to cold, depression, paranoia, hearing loss, dry skin, coarse hair, and hair loss.
Overview: Hypothyroidism occurs when the thyroid gland can't produce enough thyroid hormone. The thyroid is a butterfly-shaped gland that wraps around the front of the windpipe. It controls how the body uses energy. Without enough thyroid hormone, your body functions slow down, making you gain weight and feel tired all the time. Women are more likely to get thyroid disease than men. Hypothyroidism is fairly common and easy to treat.
Causes: Low-iodine diet, lack of iodized salt
Treatment options: As the metabolism slows down, symptoms get worse and cause puffiness, slowed heart rate, and swelling in the legs. If not treated, hypothyroidism can lead to a rare, life-threatening coma. Taking thyroid hormone replacement returns levels to normal within a few weeks and symptoms disappear. Most people need to take thyroid medicine for the rest of their life.

Gender: female
Age: 81
Symptoms: itchy throat , gassy , one side of low back hurts , rash limited to face , pain in upper body , pain below the waist
Possible conditions: Broken (Fractured) Hip
Symptoms assosiated: Symptoms of a broken hip include pain in the hip, outer upper thigh, or groin that gets worse when trying to move the hip. The injured leg may be shorter than the other leg if the hip is completely broken. In most cases, it's not possible to walk or put weight on the hurt leg.
Overview: A broken or fractured hip is a break in the thighbone under the hip joint. Usually a fall or injury causes the break. Conditions such as cancer or osteoporosis can weaken the bone, making it more likely to break. Females lose bone mass faster after menopause, so women ages 65 and older are most likely to have a hip fracture. A broken hip is serious and can keep you from walking, so you need immediate medical care. Surgery is usually necessary to fix or replace the hip. Physical therapy and using a walking aid help most people recover in a year or possibly earlier.
Causes: Any form of rigorous activity.
Treatment options: Don't try to care for a broken hip yourself. Call 911 or go to the emergency room.

Gender: {}
Age: {}
Symptoms: {}
Possible conditions:...
Symptoms assosiated:...
Overview:...
Causes:...
Treatment options:...

""".format(
        gender, age, symptoms
    )

class GenderEnum(str, Enum):
    male = "male"
    female = "female"

@app.post("/", response_model=list)
async def check_symptoms(request: Request, gender: GenderEnum, age: int, symptoms: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(gender, age, symptoms),
        temperature=0.6,
        max_tokens=2000
    )

    response: str = response.choices[0].text.strip()

    splitted_strings: list[str] = response.split("\n")

    # remove empty strings
    sections = [value for value in splitted_strings if len(value) > 0]

    return sections, {"Disclaimer":" The Symptom Checker app is intended to provide general information and is not a substitute for professional medical advice. Users should always consult with a qualified healthcare provider for accurate diagnosis and treatment recommendations."}

