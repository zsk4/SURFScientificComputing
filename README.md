# ResearchProgrammingIntro

Introduction to some tools and workflows research software engineers use when programming. Hopefully some may be useful to integrate into your own research code.

This repository is based on my experience at INTERSECT Bootcamp 2024 and modules on the INTERSECT [website](https://intersect-training.org/curriculum/), and the United States Research Software Engineer (US-RSE) association.

## Prerequisites
- Git installed locally; GitHub account
- Local git installation able to authenticate with your GitHub account (Tutorial [here](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git#authenticating-with-github-from-git))
- Working knowledge of basic git commands
  
# Set up your local repository
1. Create a fork of this repository in your GitHub account.

2. Clone a local copy of the repository and create the included conda environment (or make sure you have a conda env with the packages in environment.yml).
```
git clone https://github.com/zsk4/ResearchProgrammingIntro.git
cd ResearchProgrammingIntro
conda env create -f environment.yml
conda activate RSE
```
3. Install the pre=commit environment
```
pre-commit install
```

# Contents
- Collaborative Git
  - Git Branches ([Learn Git Branching](https://learngitbranching.js.org/?NODEMO))
  - Pull Requests
- Pre-commit hooks
  - Linting (e.g. Ruff, Black)
  - Type Checking (e.g. MyPy)
- Continuous Integration (GitHub Actions)
  - Unit Testing (e.g. PyTest, Coverage)

Additional topics: Project design and structure, documentation, packaging for PyPi, issue tracking, programmer quality of life (terminal personalization, IDEs, etc.)

# Why
Why should you take additional time to integrate these tools into your coding practices?
1. ***Version Control*** Git and GitHub allow you to keep track of and access previous versions of your code, even if multiple people are collaborating on a project simultaneously.
2. ***Readable Code*** These strategies help people better understand how your code works. This has benefits for you (remembering what your script does after not touching it for a while so it can be adapted for a new project), your peers (sharing code that doesn't require your coworker to struggle to understand what it does), reviewers (making data processing for a paper clear), and end users (ease of use of any software your publish).
