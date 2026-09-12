import os

def test_readme_exists():
    assert os.path.exists('README.md'), "README.md does not exist"

def test_agents_exists():
    assert os.path.exists('AGENTS.md'), "AGENTS.md does not exist"

def test_contributing_exists():
    assert os.path.exists('CONTRIBUTING.md'), "CONTRIBUTING.md does not exist"

def test_license_exists():
    assert os.path.exists('LICENSE'), "LICENSE does not exist"

def test_security_exists():
    assert os.path.exists('SECURITY.md'), "SECURITY.md does not exist"

def test_gitattributes_exists():
    assert os.path.exists('.gitattributes'), ".gitattributes does not exist"

def test_readme_no_phantom_repos():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    phantom_repos = [
        'google-jules-stitch-gate',
        'mcp-gh-pr-reviewer',
        'anythingllm-mcp-control',
        'searxng-mcp-control',
        'nextcloud-mcp-control',
        'antigravity-cli-telegram-bot',
    ]
    for phantom in phantom_repos:
        assert phantom not in content, f"Phantom or private repository '{phantom}' must not be referenced in README.md"

def test_readme_verified_public_repos_present():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    expected_repos = [
        'mcp-router',
        'antigravity-telegram-agent',
        'agent-vault',
        'google-jules-mcp',
        'anythingllm-mcp-gateway',
        'searxng-mcp-gateway',
        'nextcloud-mcp-gateway',
        'mailru-mcp-server',
        'thenovanodes-portal',
    ]
    for repo in expected_repos:
        assert repo in content, f"Verified public repository '{repo}' is missing from README.md"

def test_agents_integrity():
    with open('AGENTS.md', 'r', encoding='utf-8') as f:
        content = f.read()

    assert "ЗавЛаб" in content, "User title 'ЗавЛаб' must be present in AGENTS.md"
    assert "agent-vault" in content, "Vault directive must be present in AGENTS.md"
    assert "SOUL.md" not in content, "Non-existent SOUL.md must not be referenced in AGENTS.md"
