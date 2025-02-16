import httpx
import json
import pprint
import time


def main():
    # Task 1
    user_id = input("Please type the user's id you want: ")
    try:
        response = httpx.get("https://jsonplaceholder.typicode.com/users?id=" + user_id)
        response.raise_for_status()
        chosen_user = response.json()[0]
        print("User name: " + str(chosen_user["name"]) + "\nEmail: " + str(chosen_user["email"]) + "\nAddress: " + str(chosen_user["address"]["street"]) + ", " + str(chosen_user["address"]["city"]) )
    except (httpx.HTTPStatusError, IndexError):            
        if response.status_code == 500:
            print("Server error. Please try again later.")
        else:
            print("User not found\n")
        
    # Task 2

    for i in range(3):
        try:
            print("Fetching System metrics ...")
            URL = "https://api.example.com/system/metrics"
            headers = {"Authorization": "Bearer YOUR_API_KEY"}
            params = {"metrics": "cpu,memory"}
            response = httpx.get(URL, params=params, headers=headers)
            if response.status_code == 401:
                print("Invalid API key")
                break
            if response.status_code == 500:
                print("Server is currently down")
                break
        except httpx.HTTPError:
            print(f"attempt {i + 1} failed: server is currently down.")
            time.sleep(2)
            print("Retrying in 2 seconds.")
        
             
                
        
            

if __name__=="__main__":
    main()