import random
import sqlite3
import requests
from discord.ext import commands, tasks
import discord
import json
import datetime


f = open('config.json')
datac = json.load(f)
token = datac['token']
newsRoomChannel = datac['newsRoom']
newReleaseRoomChannel = datac['releaseRoom']
top10Channel = datac['top10']
db = sqlite3.connect('database.sqlite')
cursor = db.cursor()


TOKEN = token

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!",intents=intents)
client.remove_command('help')
colors = [1752220,1146986,3066993,2067276,3447003,2123412,10181046,7419530,15277667,11342935,15844367,12745742,15105570,11027200,15158332,10038562,9807270,9936031,8359053,12370112,3426654,2899536,16776960]
color = random.choice(colors)


@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name = "over Netflix news"))






@tasks.loop(seconds=50)
async def newsRoom():
    today = datetime.date.today().strftime('%Y-%m-%d')
    tomorrow = datetime.date.today() - datetime.timedelta(days=364)
    firstLink = f"https://about.netflix.com/api/data/articles?language=en&globalPage=1&regionPage=1&startDate={tomorrow}T02:29Z&endDate={today}T16:29Z&region=ceYWnOBbG7eXqCKiEw2l8&category=0&excludeFeatured=true&pageSize=15"
    secondLink =f"https://about.netflix.com/api/data/articles?language=en&globalPage=1&regionPage=1&startDate={tomorrow}T02:29Z&endDate={today}T16:29Z&region=1nTZYSDjUgVVtTGuij2uDI&category=0&excludeFeatured=true&pageSize=15"
    thirdLink =f"https://about.netflix.com/api/data/articles?language=en&globalPage=1&regionPage=1&startDate={tomorrow}T02:29Z&endDate={today}T16:29Z&region=4scinOKdKO3JYkJYksvBeo&category=0&excludeFeatured=true&pageSize=15"
    fourthLink = f"https://about.netflix.com/api/data/articles?language=en&globalPage=1&regionPage=1&startDate={tomorrow}T02:29Z&endDate={today}T16:29Z&region=t4ZhFiq3sYgX6NStiwOWB&category=0&excludeFeatured=true&pageSize=15"


    rglobal = requests.get(url=firstLink)
    dataglobal = rglobal.json()
    globalID = dataglobal['entities']['global']['globalArticles'][0]['id']
    globalTitle = dataglobal['entities']['global']['globalArticles'][0]['title']
    globalSlug = dataglobal['entities']['global']['globalArticles'][0]['slug']
    globalPubish = dataglobal['entities']['global']['globalArticles'][0]['publishedDate']

    globalThumbnail = "http:/"+dataglobal['entities']['global']['globalArticles'][0]['heroImage']['primaryThumbnail'][1:-12]
    cursor.execute(f"SELECT global FROM newsRoom")
    IDCheck = cursor.fetchone()

    if IDCheck[0] == globalID:
        pass
    else:
        cursor.execute(f"UPDATE newsRoom SET global = '{globalID}'")
        db.commit()
        embed = discord.Embed(title = f"NewsRoom Post",description=f"{globalTitle}\n",url="https://about.netflix.com/en/news/"+globalSlug,color=color)
        embed.set_image(url=globalThumbnail)
        embed.set_footer(text=f"Published at {globalPubish}")
        channel = await client.fetch_channel(newsRoomChannel)
        await channel.send(embed=embed)

    usaglobal = requests.get(url=firstLink)
    datausa = usaglobal.json()
    usaID = datausa['entities']['region']['regionArticles'][0]['id']
    usaTitle = datausa['entities']['region']['regionArticles'][0]['title']
    usaSlug = datausa['entities']['region']['regionArticles'][0]['slug']
    usaPublish = datausa['entities']['region']['regionArticles'][0]['publishedDate']
    usaThumbnail = "http:/"+datausa['entities']['region']['regionArticles'][0]['heroImage']['primaryThumbnail'][1:-12]
    cursor.execute(f"SELECT USA FROM newsRoom")
    usaIDCheck = cursor.fetchone()
    if usaIDCheck[0] == usaID:
        pass
    else:
        cursor.execute(f"UPDATE newsRoom SET USA = '{usaID}'")
        db.commit()
        embed = discord.Embed(title=f"NewsRoom Post", description=f"{usaTitle}\n",
                              url="https://about.netflix.com/en/news/" + usaSlug,color=color)
        embed.set_image(url=usaThumbnail)
        embed.set_footer(text=f"Published at {usaPublish}")
        channel = await client.fetch_channel(newsRoomChannel)
        await channel.send(embed=embed)



    jpglobal = requests.get(url=secondLink)
    datajp = jpglobal.json()
    jpID = datajp['entities']['region']['regionArticles'][0]['id']
    jpTitle = datajp['entities']['region']['regionArticles'][0]['title']
    jpSlug = datajp['entities']['region']['regionArticles'][0]['slug']
    jpPublish = datajp['entities']['region']['regionArticles'][0]['publishedDate']
    jpThumbnail = "http:/" + datajp['entities']['region']['regionArticles'][0]['heroImage']['primaryThumbnail'][1:-12]
    cursor.execute(f"SELECT Japan FROM newsRoom")
    jpIDCheck = cursor.fetchone()
    if jpIDCheck[0] == jpID:
        pass
    else:
        cursor.execute(f"UPDATE newsRoom SET Japan = '{jpID}'")
        db.commit()
        embed = discord.Embed(title=f"NewsRoom Post", description=f"{jpTitle}\n",
                              url="https://about.netflix.com/en/news/" + jpSlug,color=color)
        embed.set_image(url=jpThumbnail)
        embed.set_footer(text=f"Published at {jpPublish}")
        channel = await client.fetch_channel(newsRoomChannel)
        await channel.send(embed=embed)



    skglobal = requests.get(url=thirdLink)
    datask = skglobal.json()
    skID = datask['entities']['region']['regionArticles'][0]['id']
    skTitle = datask['entities']['region']['regionArticles'][0]['title']
    skSlug = datask['entities']['region']['regionArticles'][0]['slug']
    skPublish = datask['entities']['region']['regionArticles'][0]['publishedDate']
    skThumbnail = "http:/" + datask['entities']['region']['regionArticles'][0]['heroImage']['primaryThumbnail'][1:-12]
    cursor.execute(f"SELECT SouthK FROM newsRoom")
    skIDCheck = cursor.fetchone()
    if skIDCheck[0] == skID:
        pass
    else:
        cursor.execute(f"UPDATE newsRoom SET SouthK = '{skID}'")
        db.commit()
        embed = discord.Embed(title=f"NewsRoom Post", description=f"{skTitle}\n",
                              url="https://about.netflix.com/en/news/" + skSlug,color=color)
        embed.set_image(url=skThumbnail)
        embed.set_footer(text=f"Published at {skPublish}")
        channel = await client.fetch_channel(newsRoomChannel)
        await channel.send(embed=embed)


    ukglobal = requests.get(url=fourthLink)
    datauk = ukglobal.json()
    ukID = datauk['entities']['region']['regionArticles'][0]['id']
    ukTitle = datauk['entities']['region']['regionArticles'][0]['title']
    ukSlug = datauk['entities']['region']['regionArticles'][0]['slug']
    ukPublish = datauk['entities']['region']['regionArticles'][0]['publishedDate']
    ukThumbnail = "http:/" + datauk['entities']['region']['regionArticles'][0]['heroImage']['primaryThumbnail'][1:-12]
    cursor.execute(f"SELECT UnitedK FROM newsRoom")
    ukIDCheck = cursor.fetchone()
    if ukIDCheck[0] == ukID:
        pass
    else:
        cursor.execute(f"UPDATE newsRoom SET UnitedK = '{ukID}'")
        db.commit()
        embed = discord.Embed(title=f"NewsRoom Post", description=f"{ukTitle}\n",
                              url="https://about.netflix.com/en/news/" + ukSlug,color=color)
        embed.set_image(url=ukThumbnail)
        embed.set_footer(text=f"Published at {ukPublish}")
        channel = await client.fetch_channel(newsRoomChannel)
        await channel.send(embed=embed)


@tasks.loop(seconds=50)
async def newReleases():
    movies = 2694103
    series = 2170013
    specials = 2173907
    games = 81500273

    dramas = 1307182
    comedies = 1305630
    realityProgramming = 100199
    horrorTrillers = 81246423
    documentaries = 100148
    childrenFamily = 2070367
    fantasy = 81246426
    arcadeGame = 81495675
    actionGame = 81474312
    mysteries = 81325761
    adventures = 81325760
    anime = 100173

    releaseLink = "https://about.netflix.com/api/data/releases?language=en&page=1&country=US"
    r = requests.get(releaseLink)
    releaseData = r.json()
    id = releaseData['data'][0]['videoID']
    country = releaseData['data'][0]['country']
    title1 = releaseData['data'][0]['title1']
    title2 = releaseData['data'][0]['title2']
    image = releaseData['data'][0]['image']
    collection = releaseData['data'][0]['collection']
    genre = releaseData['data'][0]['genre']
    dateD = str(releaseData['data'][0]['startTime'])[:10]

    dateLink = f"https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp={dateD}"
    dateData = requests.get(dateLink)
    date = str(dateData.text)[1:11]



    if collection == movies:
        collection = "Movies"
    elif collection == series:
        collection = "Series"
    elif collection == specials:
        collection = "Specials"
    elif collection == games:
        collection = "Games"
    else:
        collection = "Unknown"

    if genre == dramas:
        genre = "Dramas"
    elif genre == comedies:
        genre = "Comedies"
    elif genre == realityProgramming:
        genre = "Reality Programming"
    elif genre == horrorTrillers:
        genre = "Horror/Thrillers"
    elif genre == documentaries:
        genre = "Documentaries"
    elif genre == childrenFamily:
        genre = "Children & Family Movie"
    elif genre == fantasy:
        genre = "Fantasy"
    elif genre == arcadeGame:
        genre = "Arcade Game"
    elif genre == actionGame:
        genre = "Action Game"
    elif genre == mysteries:
        genre = "Mysteries"
    elif genre == adventures:
        genre = "Adventure"
    elif genre == anime:
        genre = "Anime"
    else:
        genre = "Unknown"

    if collection != "Series":
        season = ""
    else:
        season = f" - {title2}"

    cursor.execute(f"SELECT ID FROM NewReleases")
    checkID = cursor.fetchone()
    if checkID[0] == id:
        pass
    else:
        embed = discord.Embed(title="New Release",description=f"**{title1}**\n"
                                                              f"*Collection*: `{collection}{season}`\n"
                                                              f"*Genre*: `{genre}`\n"
                                                              f"*Country*: `{country}`",color=color)
        embed.set_footer(text=f"Released at {date}")
        embed.set_image(url=image)
        channel = await client.fetch_channel(newReleaseRoomChannel)
        await channel.send(embed=embed)
        cursor.execute(f"UPDATE NewReleases SET ID = {id}")
        db.commit()


@tasks.loop(seconds=50)
async def top10():
    cursor.execute(f"SELECT moviesID FROM top10")
    check = cursor.fetchone()
    cursor.execute(f"SELECT seriesID FROM top10")
    check2 = cursor.fetchone()

    top10MoviesLink = "https://top10.netflix.com/_next/data/j2tFIZERt9_9qx-FjHPGy/index.json"
    top10SeriesLink = "https://top10.netflix.com/_next/data/j2tFIZERt9_9qx-FjHPGy/tv.json"
    r = requests.get(top10MoviesLink)
    data = r.json()
    d = data['pageProps']['data']['weeklyTopTen']
    mname1 = d[0]['name']
    mname2 = d[1]['name']
    mname3 = d[2]['name']
    mname4 = d[3]['name']
    mname5 = d[4]['name']
    mname6 = d[5]['name']
    mname7 = d[6]['name']
    mname8 = d[7]['name']
    mname9 = d[8]['name']
    mname10 = d[9]['name']

    r2 = requests.get(top10SeriesLink)
    data2 = r2.json()
    d2 = data2['pageProps']['data']['weeklyTopTen']
    sname1 = d2[0]['name']
    sname2 = d2[1]['name']
    sname3 = d2[2]['name']
    sname4 = d2[3]['name']
    sname5 = d2[4]['name']
    sname6 = d2[5]['name']
    sname7 = d2[6]['name']
    sname8 = d2[7]['name']
    sname9 = d2[8]['name']
    sname10 = d2[9]['name']

    testMovies = mname1+mname2+mname3+mname4+mname5+mname6+mname7+mname8+mname9+mname10
    testSeries = sname1+sname2+sname3+sname4+sname5+sname6+sname7+sname8+sname9+sname10
    if check[0] == testMovies:
        pass
    elif check2[0] == testSeries:
        pass
    else:
        membed = discord.Embed(title = "Top10 Films",description=f"1. **{mname1}**\n"
                                                                f"2. **{mname2}**\n"
                                                                f"3. **{mname3}**\n"
                                                                f"4. **{mname4}**\n"
                                                                f"5. **{mname5}**\n"
                                                                f"6. **{mname6}**\n"
                                                                f"7. **{mname7}**\n"
                                                                f"8. **{mname8}**\n"
                                                                f"9. **{mname9}**\n"
                                                                f"10. **{mname10}**\n",color=color)

        sembed = discord.Embed(title="Top10 Series", description=f"1. **{sname1}**\n"
                                                                f"2. **{sname2}**\n"
                                                                f"3. **{sname3}**\n"
                                                                f"4. **{sname4}**\n"
                                                                f"5. **{sname5}**\n"
                                                                f"6. **{sname6}**\n"
                                                                f"7. **{sname7}**\n"
                                                                f"8. **{sname8}**\n"
                                                                f"9. **{sname9}**\n"
                                                                f"10. **{sname10}**\n",color=color)
        channel = await client.fetch_channel(top10Channel)
        await channel.purge()
        await channel.send(embed=membed)
        await channel.send(embed=sembed)
        cursor.execute(f"UPDATE top10 SET moviesID = '{testMovies}'")
        db.commit()
        cursor.execute(f"""UPDATE top10 SET seriesID = "{testSeries}" """)
        db.commit()


@client.command()
async def start(ctx):
    top10.start()
    newReleases.start()
    newsRoom.start()
    embed = discord.Embed(description="I just started to monitor.")
    await ctx.message.auhor.send(embed=embed)


client.run(TOKEN)
print(client.user.name)