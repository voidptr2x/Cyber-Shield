import requests

def getAllCommits() -> dict:
    github_resp = requests.get("https://github.com/NefariousTheDev/Cyber-Shield/commits/main").text
    resp_lines = github_resp.split("\n")

    commits = {}
    last_commit = ""
    last_commit_comment = ""
    c = 0
    for line in resp_lines:
    
        if "Link--primary text-bold js-navigation-open markdown-title" in line: 
            last_commit_comment = line.split(">")[len(line.split(">"))-2].replace("</a", "")

        if "View commit details" in line: commits[line.split(" ")[len(line.split(" "))-1]] = last_commit_comment

    return commits

"""
{
    "version": "commit_version",
    "comment": "commit_comment"
}
"""
def get_current_commit(commit_comment: str) -> dict:
    s = getAllCommits()
    return {next(iter(s)): s[next(iter(s))]}
