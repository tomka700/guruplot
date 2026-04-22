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

#Esetleg kiplot-olhatnánk egy kördiagrammon az öt leggyakrabban játszott archetype-ot,
#azzal együtt hogy mennyire népszerűek
#mondjuk itt még ki kell küszöbölni, ha nagyon kicsik az eltérések (akkor nem látszódank a szeletek rendesen)
top_archetypes = df.nlargest(5, 'pop')
explode = [0.1, 0.5, 0, 0, 0]
colors = ( "orange", "cyan", "yellow","blue", "green",)

plt.pie(top_archetypes['pop'], labels=top_archetypes['name'], explode=explode, autopct='%1.2f%%', colors=colors, shadow=True)
plt.show()

#minden Adatoszlopnál kivehetnénk az 5 (vagy több) leggyaakrabban használt archetype-ot, 
#minden tulajdonságra (winrate, popularity, turns) egy-egy (5 vagy több oszlopos) oszlop diagrammot csinálhatnánk , 
#alájuk írnánk az archetype-ok nevét,

fig, axs = plt.subplots(2, 3, figsize=(12, 8), layout='constrained') 

top_winrate_arch = df.nlargest(5, 'winrate')
axs[0, 0].bar(top_winrate_arch['name'],top_winrate_arch['winrate'], color='green', edgecolor='darkgreen')
axs[0, 0].set_title("Legnagyobb nyerésrátájúak")

top_pop_arch = df.nlargest(5, 'pop')
axs[0, 1].bar(top_pop_arch['name'],top_pop_arch['pop'], color='blue', edgecolor='darkblue')
axs[0, 1].set_title("Legnagyobb győzelmiaránnyal rendelkezők")
axs[0, 1].set_ylabel("Adatok %-ban")

top_turn_arch = df.nlargest(5, 'turns')
axs[0, 2].bar(top_turn_arch['name'],top_turn_arch['turns'], color='green', edgecolor='darkgreen')
axs[0, 2].set_title("Legtöbb körösek")

top_dur_arch = df.nlargest(5, 'duration')
axs[1, 0].bar(top_dur_arch['name'],top_dur_arch['duration'], color='magenta', edgecolor='red')
axs[1, 0].set_title("?Nem tudom hogy hívják ezt?")

top_climb_arch = df.nlargest(5, 'climb_speed')
axs[1, 1].bar(top_climb_arch ['name'],top_climb_arch ['climb_speed'], color='grey', edgecolor='black')
axs[1, 1].set_title("?Nem tudom hogy hívják ezt?")
plt.show()

####### ehhez van egy másik megoldásom is #######
fig = plt.figure(figsize=(24, 14),layout='constrained')

fig.suptitle('Legjobb archetype-ok')
fig1, fig2, fig3 = fig.subfigures(1, 3)


top_winrate_arch = df.nlargest(5, 'winrate')
top_pop_arch = df.nlargest(5, 'pop')
x1_1=np.arange(len(top_winrate_arch))
y1_1 = np.linspace(0,top_winrate_arch['winrate'].max(),5) 
ax1 = fig1.subplots(2, 1, sharex=True)
ax1[0].set_xlabel('Legnagyobb nyerésrátájúak')
ax1[0].bar(x1_1,top_winrate_arch['winrate'], color='green', edgecolor='darkgreen')
ax1[0].set_xticks(x1_1)
ax1[0].set_yticks(y1_1)
ax1[0].set_xticklabels(top_winrate_arch['name'], rotation=45)

y1_2 = np.linspace(top_pop_arch['pop'].min(),top_pop_arch['pop'].max(),5)
x1_2=np.arange(len(top_pop_arch))
ax1[1].set_xlabel('Legnépszerűbbek')
ax1[1].bar(x1_2,top_pop_arch['pop'], color='blue', edgecolor='darkblue')
ax1[1].set_xticks(x1_2)
ax1[1].set_yticks(y1_2)
ax1[1].set_xticklabels(top_pop_arch['name'], rotation=45)


top_turn_arch = df.nlargest(5, 'turns')
top_dur_arch = df.nlargest(5, 'duration')
ax2 = fig2.subplots(2,1, sharex=True)
x2_1=np.arange(len(top_turn_arch))
y2_1 = np.linspace(0,top_turn_arch['turns'].max(),5)
ax2[0].set_xlabel('Legtöbb körösek')
ax2[0].bar(x2_1,top_turn_arch['turns'], color='green', edgecolor='darkgreen')
ax2[0].set_xticks(x2_1)
ax2[0].set_yticks(y2_1)
ax2[0].set_xticklabels(top_turn_arch['name'], rotation=45)

x2_2=np.arange(len(top_dur_arch))
y2_2 = np.linspace(0,top_dur_arch['duration'].max(),5)
ax2[1].set_xlabel('?Nem tudom hogy hívják ezt?')
ax2[1].bar(x2_2,top_dur_arch['duration'], color='magenta', edgecolor='red')
ax2[1].set_xticks(x2_2)
ax2[1].set_yticks(y2_2)
ax2[1].set_xticklabels(top_dur_arch['name'], rotation=45)


top_climb_arch = df.nlargest(5, 'climb_speed')
ax3 = fig3.subplots(1,1, sharex=True)
y3 = np.linspace(0,top_climb_arch['climb_speed'].max(),5)
ax3.set_title('?Nem tudom hogy hívják ezt?')
ax3.bar(top_climb_arch ['name'],top_climb_arch ['climb_speed'], color='grey', edgecolor='black')
#x =  np.arange(len(top_climb_arch ['name']))
ax3.set_yticks(y3)
ax3.tick_params(axis='x', rotation=45)

plt.show()



#rendezhetnénk népszerűségben csökkenő/növekvő sorrendben az archetype-okat, 
#és kilpotolhatnánk az értékekei ilyen pontokkal és azokra ileszthetnénk egy görbét, 
import numpy as np
from scipy import interpolate

df = df.sort_values(by='pop')
num_rows = len(df.index)
#xdata = np.arange(1,num_rows+1)
xdata = np.arange(len(df))
ydata = df["pop"]

f_lin = interpolate.interp1d(xdata, ydata, kind="linear", fill_value="extrapolate")
f_cub = interpolate.interp1d(xdata, ydata, kind="cubic", fill_value="extrapolate")

xx = np.linspace(1,num_rows+1, 400)

plt.figure()
plt.plot(xdata, ydata, "o", label="Eredeti adatok")
plt.plot(xx, f_lin(xx))
plt.plot(xx, f_cub(xx))
plt.xticks(xdata-1, df['name'])
plt.tick_params(axis='x', rotation=45)
plt.legend()
plt.title("Archetype-ok népszerűsége")
plt.show()



#lehetne csinálni olyat hogy class-onként megkeres max-ot,átlagot, mint és kiplotol egy bars-t
df_max = df.groupby("class")["winrate"].max().reset_index()
df_min = df.groupby("class")["winrate"].min().reset_index()
df_avr = df.groupby("class")["winrate"].mean().reset_index()

barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

br1 = np.arange(len(df_max["class"])) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

plt.bar(br1, df_max["winrate"], color ='r', width = barWidth, edgecolor ='grey', label ='max') 
plt.bar(br2, df_avr["winrate"], color ='g', width = barWidth, edgecolor ='grey', label ='avrage') 
plt.bar(br3, df_min["winrate"], color ='b', width = barWidth, edgecolor ='grey', label ='min') 

plt.xticks([r + barWidth for r in range(len(df_max["class"]))],df_max["class"])
plt.xlabel('Classas', fontweight ='bold', fontsize = 15) 
plt.ylabel('Winrates', fontweight ='bold', fontsize = 15) 
plt.legend()
plt.show()



#Lehetne hogy a Durid class elemeit kiválogatjuk, 
#x tengely pontjai:abc szerint sorba rakva a nevek, 
#pot-okra görbét illeszt, rá mutat legnagyobb étékű pontra a plot-on

df = df[df["class"] == "Druid"]
sorted_df = df.sort_values('name').reset_index(drop=True)
#winrate_sort_df = df.sort_values('winrate')

num_rows = len(sorted_df.index)
x = np.linspace(0, num_rows - 1, num_rows)
y = sorted_df["winrate"]

f_lin = interpolate.interp1d(x, y, kind="linear")

max_y = sorted_df["winrate"].max()
max_names = sorted_df[sorted_df["winrate"] == max_y]["name"]

xx = np.linspace(0, num_rows - 1, 400)
plt.figure()
plt.plot(x, y, "o")
plt.plot(xx, f_lin(xx))
plt.xticks(x, sorted_df['name'], rotation=45)
if num_rows>=4:
    f_cub = interpolate.interp1d(x, y, kind="cubic")
    plt.plot(xx, f_cub(xx))
for i in max_names.index:
    plt.annotate("max értékű",
                 xy=(x[i], sorted_df.loc[i, "winrate"]), 
                 xytext=(x[i], sorted_df.loc[i, "winrate"] + 1), 
                 arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
plt.show()
