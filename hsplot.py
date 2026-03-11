import matplotlib.pyplot as plt
import math
from re import sub

data = [
    # replace this with the input
]

data = list(filter(lambda x: x["winrate"] >= 4, data))
data = list(filter(lambda x: x["pop"] >= 4, data))
#data = list(filter(lambda x: x["pop"] <= 300, data))
#data = list(filter(lambda x: "HL" in x["archetype"] or "Highlander" in x["archetype"], data))
#data = list(filter(lambda x: "Druid" in x["archetype"], data))

for item in data:
    s = item["archetype"]
    if "Mage" in s:
        s = sub(r"\S", "*", s)
        if s.startswith("*** "):
            s = s.replace("***", "JtU", 1)
        elif s.startswith("** ** "):
            s = s.replace("** **", "XL HL", 1)
        elif s.startswith("** "):
            s = s.replace("**", "XL", 1)
    item["archetype"] = s

archetypes = [i["archetype"] for i in data]
pop = [i["pop"] for i in data]
win_rates = [i["winrate"] for i in data]

class_colors = {
    "Death Knight": "#6C699A",
    "DK": "#6C699A",
    "Demon Hunter": "#256F3D",
    "DH": "#256F3D",
    "Druid": "#FF7F0E",
    "Hunter": "#2CA02C",
    "****": "#17BECF",
    "Paladin": "#F0BD27",
    "Priest": "#C7C7C7",
    "Rogue": "#7F7F7F",
    "Shaman": "#2B7DB4",
    "lock": "#A27099",
    "Warrior": "#C81518"
}
colors = [next((c for cls, c in class_colors.items() if cls in d["archetype"]), "black") for d in data]

plt.figure(figsize=(10, 6))
plt.scatter(pop, win_rates, c=colors, s=90, edgecolor='k', alpha=0.9, zorder=3)
plt.xlabel("# of games (top 1k this patch)")
plt.xscale("log")
plt.ylabel("Win Rate (%)")
plt.xticks((l:=[m*z for e in range(len(str(min(pop)))-1,len(str(max(pop)))) for m in range(1,10) if min(pop)-(z:=10**e)<m*z<max(pop)+z]),labels=l)
plt.yticks(range(math.floor(min(win_rates)), math.ceil(max(win_rates))+1))
plt.axhline(y=50, color="black", linewidth=0.6)
plt.grid(True)

for i, x in enumerate(archetypes):
    plt.annotate(x, (pop[i], win_rates[i]), fontsize=10, alpha=0.7)

plt.show()