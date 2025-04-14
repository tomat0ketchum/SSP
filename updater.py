import subprocess


def update_github_repo():
    """
    This script will:
    1. Initialize (or re-initialize) the current directory as a Git repository.
    2. Add the GitHub remote 'origin' pointing to
    https://github.com/tomat0ketchum/SSP.git
    3. Stage all files (git add .)
    4. Commit with a default message.
    5. Push to the 'main' branch on GitHub.
    """

    # 1. Initialize or reinitialize the repository
    subprocess.run(["git", "init"], check=True)

    # 2. Set up remote origin (overwrites if it already exists)
    subprocess.run(["git", "remote", "remove", "origin"], check=False)
    subprocess.run(
        ["git", "remote", "add", "origin",
            "https://github.com/tomat0ketchum/SSP.git"],
        check=True
    )

    # 3. Stage all files except .gitignore
    subprocess.run(["git", "add", "."], check=True)

    # 4. Commit changes
    commit_message = "Update from Python script"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # 5. Push to the 'main' branch on GitHub
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)


if __name__ == "__main__":
    # Make sure you run this script from the directory
    # containing the files you want to push
    update_github_repo()
