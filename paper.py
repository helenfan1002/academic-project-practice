import json

paper = {"title": "Example Paper", "authors":["Alice", "Bob"], "year":2023}
with open("paper.json","w",encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)
with open("paper.json","r",encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded["title"])