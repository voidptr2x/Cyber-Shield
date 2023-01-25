import requests

def getAllCommits() -> dict[str]:
    github_resp = requests.get("https://github.com/NefariousTheDev/Cyber-Shield/commits/main").text
    resp_lines = github_resp.split("\n")

    commits = {}
    last_commit = ""
    c = 0
    for line in resp_lines:
        if "View commit details" in line: last_commit = line.split(" ")[len(line.split(" "))-1]
        if "Link--primary text-bold js-navigation-open markdown-title" in line: commits[last_commit] = line.split(">")[len(line.split(">"))-2].replace("</a", "")

    return commits

"""
{
    "version": "commit_version",
    "comment": "commit_comment"
}
"""
def get_current_commit(commit_comment: str) -> dict:
    s = getAllCommits()
    info = {}
    for key in s:
        if s[key] == commit_comment:
            info['update'] = key
            info['comment'] = s[key]
            return info
    return info
