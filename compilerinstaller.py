import shutil
from git import Repo

# Local directory where you want to clone the repository
local_temp_directory = 'temp'
final_directory = 'compiler'
# GitHub repository URL
repo_url = 'https://github.com/LizardRush/Crystal.git'
# Clone the repository to a temporary directory
Repo.clone_from(repo_url, local_temp_directory)
shutil.move(f"{local_temp_directory}/compiler", final_directory)
open('compiler/crystal.lock', 'w').close
# Clean up: Remove the temporary directory
shutil.rmtree(local_temp_directory)
