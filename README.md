# Pybot

Discord bot made in python


#### Requirements

Discord.py Rewrite Branch (for python >3.6)

```pip3 install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]```

or

```python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py[voice]```

```aiohttp==<3.4.4```

```websockets==6.0```

```ddg3==0.6.6```

For music playback:

```PyNaCl```

```libops0```

```ffmpeg```

#### Usage


##### Commands

Commands are prefixed with '.' period

| Command | Reponse  |
| -------- | -------- |
| .bitcoin     | Get bitcoin prices |
| .help  |  Shows help message |
| .search | Search DuckDuckGo for results |
| .serverlist | Lists current game servers & Status  |
| .pingit | Pings a server, checks up or down |
| .play URL | Plays clip from youtube/twitch/other media .help for more commands |
| .weather <args> [args] | Current weather |
|  yay | Response with a random cheer!    |


#### Todo

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
