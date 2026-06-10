import subprocess
import datetime


def get_current_branch():
    """Get the current branch name."""
    return subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"]
    ).decode().strip()


def get_commit_dates():
    """Return list of commit dates (oldest first) from git log on current branch."""
    output = subprocess.check_output(
        ["git", "log", "--pretty=format:%ad", "--date=iso"]
    ).decode().splitlines()
    return [datetime.datetime.fromisoformat(d) for d in output]


if __name__ == "__main__":
    branch = get_current_branch()
    dates = get_commit_dates()
    if len(dates) >= 2:
        elapsed_hours = (dates[0] - dates[-1]).total_seconds() / 3600.0
        print(f"Branch: {branch}")
        print(f"Total commits: {len(dates)}")
        print(f"Elapsed time: {elapsed_hours:.2f} hours")
    else:
        print("Not enough commits to calculate elapsed time.")
