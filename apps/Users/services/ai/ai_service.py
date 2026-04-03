from openai import openAI


class AI_Service:
    client = openAI(
        base_url = "",
        api_key  = ""
    )
    def generate_gym_program(self,user_data):

        prompt = f"""
           You are a professional fitness coach with years of experience designing training programs for users of all levels. Your task is to create a personalized workout program based on the user's data. The program should include:

            1. Warm-up routine
            2. Main exercises (split by muscle groups or full body)
            3. Number of sets and reps for each exercise
            4. Rest time between sets
            5. Optional tips for proper form and progression

            Use the following user data to customize the program:
            - Age: {user_data.age}
            - Gender: {user_data.gender}
            - Goal: {user_data.goal} (loss fat, bulking, cutting)
            - Duration: {user_data.duration} (1 month, 2 months, etc.)
            - Training frequency: {user_data.training} (number of days per week)
            - Height: {user_data.height}
            # - Weight: {user_data.weight} (optional if you have it)

            Output the program in a structured and easy-to-read format. Include explanations for why each exercise is included and adapt intensity to the user’s level. Be concise but professional.
        """ 
        response = self.client.completions.create(
            model="x-ai/grok-4.1-fast",
            messages=[{"role": "user", "content": prompt}],
        )

        program_text = response['choices'][0]['message']['content'].strip()
        return program_text