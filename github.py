import subprocess
import datetime
import os


def run_git_command(command):
    try:
        result = subprocess.run(command, shell=True,
                                check=True, capture_output=True, text=True)
        if result.stdout:
            print(f"Success: {result.stdout}")
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False, str(e.stderr)


def check_git_config():
    """Check if git user email and name are configured"""
    email_cmd = "git config --get user.email"
    name_cmd = "git config --get user.name"

    success_email, email = run_git_command(email_cmd)
    success_name, name = run_git_command(name_cmd)

    if (not success_email or not success_name or
            not email.strip() or not name.strip()):
        print("\n⚠️ Git user configuration is incomplete!")
        print("Please configure git with:")
        print("git config --global user.email 'your@email.com'")
        print("git config --global user.name 'Your Name'")
        return False
    return True


def init_repository():
    """Initialize git repository if it doesn't exist"""
    if not os.path.exists('.git'):
        print("\n🔧 Initializing new git repository...")

        # Follow exact GitHub repository initialization steps
        commands = [
            'echo "# SSP" >> README.md',
            "git init",
            "git add README.md",
            'git commit -m "first commit"',
            "git branch -M main",
            "git remote add origin https://github.com/tomat0ketchum/SSP.git"
        ]

        for command in commands:
            print(f"\nExecuting: {command}")
            success, _ = run_git_command(command)
            if not success:
                print(f"❌ Failed to execute: {command}")
                return False
    return True


def update_git():
    print("\n=== Starting SSP Git Update ===")
    print("Repository: https://github.com/tomat0ketchum/SSP.git")

    # Check git configuration first
    if not check_git_config():
        return False

    # Initialize repository if needed
    if not init_repository():
        return False

    # Get current timestamp for commit message
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check if there are changes to commit
    status_success, status_output = run_git_command("git status --porcelain")
    if not status_success:
        print("\n❌ Failed to check git status!")
        return False

    if not status_output.strip():
        print("\n✨ No changes to commit!")
        return True

    # Commands to run
    commands = [
        "git add .",
        f'git commit -m "SSP: {timestamp}"',
        "git pull --rebase origin main",
        "git push -u origin main"
    ]

    for command in commands:
        print(f"\nExecuting: {command}")
        success, _ = run_git_command(command)
        if not success:
            print("\n❌ SSP git update failed!")
            return False

    print("\n✅ SSP update completed successfully!")
    return True


if __name__ == "__main__":
    print("SSP Git Updater")
    print("=====================================")
    input("Press Enter to start git update...")
    update_git()
    input("\nPress Enter to exit...")
