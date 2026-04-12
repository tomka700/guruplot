import matplotlib.pyplot as plt
import pandas as pd

data = [
    # replace this with the input
]
if not data: raise ValueError("No Data")
rank = data[0].replace("_", " ")
rank = rank.replace("legend", "1k") if "top" in rank else rank.replace("diamond ", "d").replace("to", "-").replace(" legend", "l").replace("1", "d1")
df = pd.DataFrame(data[1])

class_colors = {
    "Death Knight": "#6C699A",
    "DK": "#6C699A",
    "Demon Hunter": "#256F3D",
    "DH": "#256F3D",
    "Druid": "#FF7F0E",
    "Hunter": "#2CA02C",
    "Mage": "#17BECF",
    "Paladin": "#F0BD27",
    "Priest": "#C7C7C7",
    "Rogue": "#7F7F7F",
    "Shaman": "#2B7DB4",
    "lock": "#A27099",
    "Warrior": "#C81518"
}
df["class"] = df["name"].str.extract(f"({"|".join(class_colors.keys())})")
df["color"] = df["class"].map(class_colors).fillna("black")
df["class"] = df["class"].replace("lock", "Warlock")
df["is_hl"] = df["name"].str.contains("HL|Highlander")

#df = df[df["winrate"] >= 40]
#df = df[df["pop"] >= 70]
#df = df[df["pop"] <= 300]
#df = df[df["is_hl"]]
#df = df[df["class"] == "Druid"]
#df = df[df["winrate"] == df.groupby("class")["winrate"].transform("max")]

plt.figure(figsize=(10, 6))
plt.scatter(df["pop"], df["winrate"], c=df["color"], s=90, edgecolor="black", alpha=0.9, zorder=3)
plt.xlabel(f"# of games ({rank} this patch)")
plt.xscale("log")
plt.ylabel("Win Rate (%)")
l = [m*z for e in range(len(str(min(df["pop"])))-1,len(str(max(df["pop"])))) for m in range(1,10) if min(df["pop"])-(z:=10**e) < m*z < max(df["pop"])+z]
plt.xticks(l, l)
plt.yticks(range(round(min(df["winrate"])) - 1, round(max(df["winrate"])) + 2))
plt.axhline(y=50, color="black", linewidth=0.6)
plt.grid()

for _, row in df.iterrows():
    plt.annotate(row["name"], (row["pop"], row["winrate"]), fontsize=10, alpha=0.7)

plt.show()
