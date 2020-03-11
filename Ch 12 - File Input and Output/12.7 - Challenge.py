# 12.7 - Challenge.py

import csv
import pathlib

scores_file = pathlib.Path.home() / "scores.csv"
highscores_file = pathlib.Path.home() / "high_scores.csv"

scores_list = []

with scores_file.open(mode = "r", encoding="utf-8", newline="") as scores:
    reader = csv.DictReader(scores)
    for row in reader:
        scores_list.append(row)

high_scores_list = {}

for item in scores_list:
    name = item["name"]
    score = item["score"]
    if name not in high_scores_list:
        high_scores_list[name] = score
    else:
        if score > high_scores_list[name]:
            high_scores_list[name] = score

with highscores_file.open(mode = "w", encoding="utf-8", newline="") as high_scores:
    writer = csv.DictWriter(high_scores, fieldnames=["name", "high_score"])
    writer.writeheader()
    for name in high_scores_list:
        row = {"name": name, "high_score": high_scores_list[name]}
        writer.writerow(row)