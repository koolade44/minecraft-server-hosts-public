import time


t = time.asctime()
i1 = input('Cracked? (y/n)')
y = str('y')
if i1 == y:
    o1 = str('false')
else:
    o1 = str('true')


i2 = input('Gamemode? (survival/creative): ')
i3 = input('Pvp? (true/false): ')
i4 = input('server description: ')
x = open('server.properties', 'w')
x.write('''#Minecraft server properties
#%s
spawn-protection=16
max-tick-time=60000
query.port=40236
generator-settings=
force-gamemode=false
allow-nether=true
enforce-whitelist=false
gamemode=%s
broadcast-console-to-ops=true
enable-query=true
player-idle-timeout=0
difficulty=easy
spawn-monsters=true
broadcast-rcon-to-ops=true
op-permission-level=4
pvp=%s
snooper-enabled=false
level-type=default
hardcore=false
enable-command-block=true
max-players=10
network-compression-threshold=256
resource-pack-sha1=
max-world-size=29999984
function-permission-level=2
server-port=40236
rcon.port=25575
server-ip=
spawn-npcs=true
allow-flight=false
level-name=world
view-distance=10
resource-pack=
spawn-animals=true
white-list=false
rcon.password=
generate-structures=true
online-mode=%s
max-build-height=256
level-seed=
use-native-transport=true
prevent-proxy-connections=false
enable-rcon=false
motd=%s''' % (t, i2, i3, o1, i4))
