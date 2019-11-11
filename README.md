# Pybot

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Spcktr/PyBot.svg)
![GitHub](https://img.shields.io/github/license/spcktr/pybot.svg)
![GitHub top language](https://img.shields.io/github/languages/top/spcktr/pybot.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Maintenance](https://img.shields.io/maintenance/yes/2019.svg)

---

Discord bot made in python. Contact Waka#1920 If you need help or want to make suggestions.


### Requirements

##### **Python 3.5.3 or higher is required**


Discord.py Rewrite Branch (for python >3.5)

```pip3 install -U discord.py[voice]```

or

```python3 -m pip install -U discord.py[voice]```

```aiohttp==3.4.4```

```websockets==6.0```

```ddg3==0.6.6```

For music playback:

```PyNaCl```

```libopus0```

```ffmpeg```
```youtube_dl```

##### Commands

Commands are prefixed with '.' period

| Command | Reponse  |
| -------- | -------- |
| .help  |  Shows help message |
| .btc     | Get bitcoin prices |
| .coinlist     | Get top 10 cryptocoin prices |
| .clock | displays world clock times |
| .search | Search DuckDuckGo for results |
| .serverlist | Lists current game servers & Status  |
| .ping | Pings a server, checks up or down |
| .play URL | Plays clip from youtube/twitch/other media .help for more commands |
| .pun | displays random groan inducing pun |
| .r4chan | randomly selects image & thread from 4chan (NSFW/NSFL)|
| .weather <args> [args] | Current weather |
|  yay | Response with a random cheer!    |
  
#### Known Issues

##### Playback not/no longer working. 
If playback is not longer working, please update youtube_dl as it needs to periodically update security certs then try again.

#### Todo

~~- [ ] Add Fuzzy string matching to game price searching~~
- [x] Add Eightball function(removed)
- [x] Add bitcoin prices(AUD/USD)
- [x] Add weather
- [x] Add ping function to detect offline game servers
- [x] Add ping to game server list
- [ ] Add admin level commands to control Bot
- [ ] Make server list admin/client-side editable
- [x] Add web search
- [x] Add audio playback

## On-hold features

- [ ] Youtube Search
- [ ] 'Has started streaming' notification

---

#### Contribs
[4chan roulette code u/Memekip](https://www.reddit.com/r/Python/comments/ccrh6o/i_just_made_the_most_5050_script_ever_it_selects/)
