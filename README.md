# Research Artifact - Reusing My Own Code: Preliminary Results for Competitive Coding in Jupyter Notebooks

> This is a research artifact for the 29th Asia-Pacific Software Engineering Conference (APSEC 2022) ERA paper "**Reusing My Own Code: Preliminary Results for Competitive Coding in Jupyter Notebooks**".

## Abstract

The reuse of already existing code is widely considered as a popular software development practice, that provides both benefits and drawbacks for all stakeholders involved. Prior work reports on how code reuse is a common practice in software development projects, and data science projects such as machine learning pipelines. Recently, there has been much code reuse work in the context of competitive programming. Although there is work such as detecting plagiarism, there is no work that studies how a competitor will reuse their own code. In this paper, we present a preliminary study on the code reuse behavior of three grandmasters' Jupyter notebooks in the Kaggle Competitions, an online competition platform for data scientists. and report the types of code they often reuse. Grandmasters are the highest level reached in competitions (novice, expert, master, and grandmaster). We find that Grandmasters are less likely to reuse specialized code, but instead tend to reuse common functions like importing packages (importing the pandas library). They are most likely to reuse common abstractions like importing packages, configurations, file IO operations, show data, plot graphs, define functions and explore files.
The work opens up new research potential into recommending how developers can reuse their own code.

## Dependencies
- Dataset: [KGTorrent](https://zenodo.org/record/4468523)
- Tool: [NCDSearch](https://github.com/takashi-ishio/NCDSearch)

## Manual Tasks
We run the automated script to generate the result of code reusing. The result will be written as a CSV file named `output.csv`. (One file / One competitor)
Then, we do a manual [code type classification](https://docs.google.com/spreadsheets/d/1V_JtBJURIcg-o8r25Go7eDnjsbA61gUP_0NEAsfdlpg/) and visualization (`playground.ipynb`).