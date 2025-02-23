import requests

class LocalModels:
    def local_llm(self, system_message, user_message):
        body = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0
        }

        # Adding API Key in headers (example)
        headers = {
            "Authorization": "Bearer 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"
        }

        endpoint = "https://api.groq.com/openai/v1/chat/completions"
        print("endpoint::::::::::::", endpoint)
        
        try:
            response = requests.post(endpoint, json=body, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                answer = result['choices'][0]['message']['content']
                print("length of ans --", len(answer))
                return answer
            else:
                print("Failed to get response from local LLM", response.status_code, response.text)
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
