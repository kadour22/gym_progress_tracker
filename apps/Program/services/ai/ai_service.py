import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
class AI_Service:
    client = OpenAI(
        base_url =os.getenv("base_url"),
        api_key  = os.getenv("api_key")
    )
    def generate_gym_program(self, user_data):

        prompt = f"""
        You are a professional fitness coach. Create a personalized workout program based on the user's data below.

        User Data:
        - Age: {user_data.age}
        - Gender: {user_data.gender}
        - Goal: {user_data.progam_goal} (loss fat, bulking, cutting)
        - Duration: {user_data.durations}
        - Training frequency: {user_data.training} (days per week)
        - Height: {user_data.height} cm
        - Weight: {user_data.weight} kg

        IMPORTANT: Respond ONLY with a valid JSON object. No markdown, no explanation, no extra text.

        The JSON must follow this exact structure:
        {{
        "program_name": "string",
        "goal": "string",
        "duration": "string",
        "days_per_week": 3,
        "warmup": [
            {{"exercise": "string", "duration": "string"}}
        ],
        "days": [
            {{
            "day": "Day 1",
            "focus": "string",
            "exercises": [
                {{
                "name": "string",
                "sets": "string",
                "reps": "string",
                "rest": "string",
                "tips": "string"
                }}
            ]
            }}
        ],
        "cooldown": ["string"],
        "general_tips": ["string"]
        }}
        """

        response = self.client.chat.completions.create(
            model="x-ai/grok-4.1-fast",
            messages=[
                {"role": "system", "content": "You are a professional fitness coach. Always respond with valid JSON only — no markdown, no extra text."},
                {"role": "user", "content": prompt}
            ],
        )

        raw_text = response.choices[0].message.content.strip()

        # Strip markdown fences if the model adds them anyway
        clean_text = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_text, flags=re.MULTILINE).strip()

        try:
            program_data = json.loads(clean_text)
        except json.JSONDecodeError as e:
            # Fallback: return raw text with error info for debugging
            raise ValueError(f"AI returned invalid JSON: {e}\nRaw response: {raw_text[:300]}")

        return program_data