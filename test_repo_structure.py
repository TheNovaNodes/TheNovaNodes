import os

def test_readme_exists():
    assert os.path.exists('README.md'), "README.md does not exist"

def test_agents_exists():
    assert os.path.exists('AGENTS.md'), "AGENTS.md does not exist"

def test_contributing_exists():
    assert os.path.exists('CONTRIBUTING.md'), "CONTRIBUTING.md does not exist"
