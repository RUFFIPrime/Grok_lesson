import requests 


class GitHubClient:
    def __init__(self):  
        self.base_url = "https://api.github.com"  
    
    def get_user_info(self, username):
        response = requests.get(f"{self.base_url}/users/{username}")
        return response.json() if response.status_code == 200 else {"error": f"Ошибка {response.status_code}"}    
    
    def get_repos(self, username):  
        response = requests.get(f"{self.base_url}/users/{username}/repos")  
        if response.status_code == 200:  
            return [repo['name'] for repo in response.json()]  
        else:  return {"error": f"Статус-код {response.status_code}"} 
    
    def get_repo_stars(self, username, repo_name):
        response = requests.get(f"{self.base_url}/repos/{username}/{repo_name}")
        if response.status_code == 200:
            return response.json()['stargazers_count']
        else:
            return {"error": f"Статус-код {response.status_code}"}


client = GitHubClient() 
print(client.get_repo_stars("torvalds", "linux"))