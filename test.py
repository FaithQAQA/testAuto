import requests
import subprocess
import os

# Define the GitHub repository and release information
GITHUB_REPO = "your_username/your_repository"
GITHUB_TOKEN = "your_github_token"  # Optional: for rate limiting purposes
RELEASE_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
script_version = "1.0.0"  # Define the version number of your script

def check_for_new_version():
    try:
        # Fetch the latest release information
        response = requests.get(RELEASE_API_URL)
        release = response.json()
        
        # Extract the latest tag (version) from the release
        latest_version = release["tag_name"]
        
        # Compare the latest version with the current version
        if latest_version!= script_version:
            return True  # A new version is available
        else:
            return False  # No new version
    except Exception as e:
        print(f"Error checking for new version: {e}")
        return False

def download_and_run_new_version(release_url):
    try:
        # Download the new version of the script
        response = requests.get(release_url)
        with open("new_version.py", "wb") as file:
            file.write(response.content)
        
        # Run the new version of the script
        subprocess.run(["python", "new_version.py"])
        
        # Optionally, delete the new version file after running it
        os.remove("new_version.py")
    except Exception as e:
        print(f"Error downloading and running new version: {e}")

if __name__ == "__main__":
    # Check for a new version
    if check_for_new_version():
        # URL of the new version of the script in the GitHub release
        release_url = f"https://github.com/{GITHUB_REPO}/releases/latest/download/new_version.py"
        
        # Download and run the new version
        download_and_run_new_version(release_url)
    else:
        # Continue with the current version of the script
        print("No new version available. Continuing with the current version.")
