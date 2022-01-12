from github import Github


def get_repos(username, token):
    g = Github(login_or_token=token)
    return g.get_user(username).get_repos()


def list_repos(username, token):
    repos = get_repos(username=username, token=token)
    message = []
    for index, repo in enumerate(repos):
        message.append(f'{index + 1}: {repo.name}')
        languages = repo.get_languages()
        if len(languages) > 0:
            message.append(', '.join(list(languages)))
    return message


def repos_language_percentage(username, token):
    repos = get_repos(username=username, token=token)
    languages_counts = {}
    for repo in repos:
        languages = repo.get_languages()
        for l in languages:
            if l in languages_counts:
                languages_counts[l] += languages[l]
            else:
                languages_counts[l] = languages[l]
    s = sum(languages_counts.values())
    percentage = {k: 100 * v / s for k, v in sorted(languages_counts.items(), key=lambda item: item[1], reverse=True)}
    message = [f'{k}: {v:.2f}%' for k, v in percentage.items()]
    return message
