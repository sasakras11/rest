import openai
from django.conf import settings

def suggest_task_category(description):
    try:
        response = openai.ChatCompletion.create(
            model="o3-mini",
            messages=[
                {"role": "system", "content": "You are a task categorizer. Respond with only one word."},
                {"role": "user", "content": f"What category best fits this task: {description}"}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return None