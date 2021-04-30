import random
from datetime import datetime
import discord
from discord.ext import commands
todaymessage = 0
settings = {
    'token': 'NzE5ODE3ODE3OTkzNzczMDY3.Xt88lQ.1gmOFUMzHz0CGHQQa6b_lqP9h-8',
    'bot': 'Efirium bot',
    'id': 719817817993773067,
    'prefix': 'c.'
}



































# ниже я открываю текстовые фаилы в которые записываються данные

bot = commands.Bot(command_prefix=settings['prefix'])

log = []
#это я создаю масив в который будут сохраняться карточки игрока
userCart = []
#далее я записываю в файл колоду карт
f = open('cart.txt', 'w')
c1 = open('1.txt', 'r')
c2 = open('2.txt')
c3 = open('3.txt')
c4 = open('4.txt')
c5 = open('5.txt')
c6 = open('6.txt')
c7 = open('7.txt')
c8 = open('8.txt')
c9 = open('9.txt')
c10 = open('10.txt')
c11 = open('11.txt')
c12 = open('12.txt')
c13 = open('13.txt')
c14 = open('14.txt')
c15 = open('15.txt')
c16 = open('16.txt')
c17 = open('17.txt')
c18 = open('18.txt')
c19 = open('19.txt')
c20 = open('20.txt')
c21 = open('21.txt')
c22 = open('22.txt')
c23 = open('23.txt')
c24 = open('24.txt')
c25 = open('25.txt')
c26 = open('26.txt')
c27 = open('27.txt')
c28 = open('28.txt')
c29 = open('29.txt')
c30 = open('30.txt')
c31 = open('31.txt')
c32 = open('32.txt')
c33 = open('33.txt')
c34 = open('34.txt')
c35 = open('35.txt')
c36 = open('36.txt')
time = datetime.now()
allcart = []
f.write(str(allcart))
f.close()


#карта мира в масиве
g = ':green_square:'

r = '🟥'

s = ':black_large_square:'

y = '🟨'

o = '🟧'

p = ':mens:'
map1 = {
    '00': str(g),
    '01': str(g),
    '02': str(g),
    '03': str(g),
    '04': str(g),
    '05': str(g),
    '06': str(g),
    '07': str(g),
    '08': str(g),
    '09': str(g),
    '10': str(g),
    '11': str(g),
    '12': str(g),
    '13': str(g),
    '14': str(g),
    '15': str(g),
    '16': str(g),
    '17': str(g),
    '18': str(g),
    '19': str(y),
    '20': str(g),
    '21': str(g),
    '22': str(g),
    '23': str(g),
    '24': str(g),
    '25': str(g),
    '26': str(g),
    '27': str(g),
    '28': str(y),
    '29': str(y),
    '30': str(g),
    '31': str(g),
    '32': str(g),
    '33': str(g),
    '34': str(g),
    '35': str(g),
    '36': str(g),
    '37': str(g),
    '38': str(y),
    '39': str(y),
    '40': str(g),
    '41': str(g),
    '42': str(g),
    '43': str(g),
    '44': str(g),
    '45': str(g),
    '46': str(g),
    '47': str(g),
    '48': str(y),
    '49': str(y),
    '50': str(g),
    '51': str(g),
    '52': str(g),
    '53': str(g),
    '54': str(g),
    '55': str(g),
    '56': str(g),
    '57': str(y),
    '58': str(y),
    '59': str(y),
    '60': str(g),
    '61': str(g),
    '62': str(g),
    '63': str(g),
    '64': str(g),
    '65': str(g),
    '66': str(y),
    '67': str(y),
    '68': str(y),
    '69': str(y),
    '70': str(g),
    '71': str(g),
    '72': str(g),
    '73': str(y),
    '74': str(y),
    '75': str(y),
    '76': str(y),
    '77': str(y),
    '78': str(y),
    '79': str(o),
    '80': str(s),
    '81': str(s),
    '82': str(s),
    '83': str(y),
    '84': str(y),
    '85': str(y),
    '86': str(y),
    '87': str(y),
    '88': str(o),
    '89': str(o),
    '90': str(s),
    '91': str(r),
    '92': str(s),
    '93': str(y),
    '94': str(y),
    '95': str(y),
    '96': str(y),
    '97': str(y),
    '98': str(o),
    '99': str(o),
}
txt = '4.4.txt'
world1 = {
    'health': '10',
    'pY': 0,
    'pX': 0,
    '00': str(g),
    '01': str(g),
    '02': str(g),
    '03': str(g),
    '04': str(g),
    '05': str(g),
    '06': str(g),
    '07': str(g),
    '08': str(g),
    '09': str(g),
    '10': str(g),
    '11': str(g),
    '12': str(g),
    '13': str(g),
    '14': str(g),
    '15': str(g),
    '16': str(g),
    '17': str(g),
    '18': str(g),
    '19': str(y),
    '20': str(g),
    '21': str(g),
    '22': str(g),
    '23': str(g),
    '24': str(g),
    '25': str(g),
    '26': str(g),
    '27': str(g),
    '28': str(y),
    '29': str(y),
    '30': str(g),
    '31': str(g),
    '32': str(g),
    '33': str(g),
    '34': str(g),
    '35': str(g),
    '36': str(g),
    '37': str(g),
    '38': str(y),
    '39': str(y),
    '40': str(g),
    '41': str(g),
    '42': str(g),
    '43': str(g),
    '44': str(g),
    '45': str(g),
    '46': str(g),
    '47': str(g),
    '48': str(y),
    '49': str(y),
    '50': str(g),
    '51': str(g),
    '52': str(g),
    '53': str(g),
    '54': str(g),
    '55': str(g),
    '56': str(g),
    '57': str(y),
    '58': str(y),
    '59': str(y),
    '60': str(g),
    '61': str(g),
    '62': str(g),
    '63': str(g),
    '64': str(g),
    '65': str(g),
    '66': str(y),
    '67': str(y),
    '68': str(y),
    '69': str(y),
    '70': str(g),
    '71': str(g),
    '72': str(g),
    '73': str(y),
    '74': str(y),
    '75': str(y),
    '76': str(y),
    '77': str(y),
    '78': str(y),
    '79': str(o),
    '80': str(s),
    '81': str(s),
    '82': str(s),
    '83': str(y),
    '84': str(y),
    '85': str(y),
    '86': str(y),
    '87': str(y),
    '88': str(o),
    '89': str(o),
    '90': str(s),
    '91': str(r),
    '92': str(s),
    '93': str(y),
    '94': str(y),
    '95': str(y),
    '96': str(y),
    '97': str(y),
    '98': str(o),
    '99': str(o),
}
print(
    world1['90'] + world1['91'] + world1['92'] + world1['93'] + world1['94'] + world1['95'] + world1['96'] + world1['97'] + world1['98'] + world1['99'] + '\n'
    + world1['80'] + world1['81'] + world1['82'] + world1['83'] + world1['84'] + world1['85'] + world1['86'] + world1['87'] + world1['88'] + world1['89'] + '\n'
    + world1['70'] + world1['71'] + world1['72'] + world1['73'] + world1['74'] + world1['75'] + world1['76'] + world1['77'] + world1['78'] + world1['79'] + '\n'
    + world1['60'] + world1['61'] + world1['62'] + world1['63'] + world1['64'] + world1['65'] + world1['66'] + world1['67'] + world1['68'] + world1['69'] + '\n'
    + world1['50'] + world1['51'] + world1['52'] + world1['53'] + world1['54'] + world1['55'] + world1['56'] + world1['57'] + world1['58'] + world1['59'] + '\n'
    + world1['40'] + world1['41'] + world1['42'] + world1['43'] + world1['44'] + world1['45'] + world1['46'] + world1['47'] + world1['48'] + world1['49'] + '\n'
    + world1['30'] + world1['31'] + world1['32'] + world1['33'] + world1['34'] + world1['35'] + world1['36'] + world1['37'] + world1['38'] + world1['39'] + '\n'
    + world1['20'] + world1['21'] + world1['22'] + world1['23'] + world1['24'] + world1['25'] + world1['26'] + world1['27'] + world1['28'] + world1['29'] + '\n'
    + world1['10'] + world1['11'] + world1['12'] + world1['13'] + world1['14'] + world1['15'] + world1['16'] + world1['17'] + world1['18'] + world1['19'] + '\n'
    + world1['00'] + world1['01'] + world1['02'] + world1['03'] + world1['04'] + world1['05'] + world1['06'] + world1['07'] + world1['08'] + world1['09'])


@bot.command()


async def creates(ctx):
    global id
    global save
    global  map
    save = []
    if ctx.message.content == 'c.creates 1':
        map = 1
    else:
        map = 1
    userstat = '0 ' + '0 ' + '10 ' + '1 ' + '0 ' + '10 ' + '0 ' + str(map) + ' ' + '\n' + ' 5' + ' 4' + ' 5' + ' 4'
    #первых два это кординаты YX третье это здоровье, четвёртое это день, пьятое это количество еды, шестое это голод, седьмое это опыт, восьмое это карта
    #девятое и десятое это кординаты первого животного, 11 и 12 второго
    id = str(ctx.message.author.id) + '.txt'
    a = open(id, 'w')
    a.write(userstat)
    a.close()

@bot.command()
async def s(ctx):
    global log
    global author
    global channel
    global channelid
    global authorid
    global content
    global audit
    log = [log]
    author = ctx.message.author
    channel = ctx.message.channel.name
    channelid = ctx.message.channel.id
    authorid = ctx.message.author.id
    content = ctx.message.content
    #while ниже используется для фильтрации сообщений
    #while authorid==582518704860823560:
    print(str(author)+': '+str(content)+" (" + str(authorid) + ") #"+str(channel))
    log.append(str(author)+': '+str(content)+" (" + str(authorid) + ") #"+str(channel))
    audit = str(str(authorid)+":  "+str(content) + "( " + str(author) + ' )')
    auditsend()

def auditsend():
    t = open('log.txt', 'a')
    t.write(audit + '\n')
    t.close()
@bot.command()

async def hi(ctx):
    embed = discord.Embed(
        title='test',
        description='ахаё',
        colour=discord.Colour.from_rgb(0, 200, 0)
    )
    await ctx.send(embed=embed)

#async def take_cart(ctx):
#    take = 0
#    while take==0:
#        random_cart = random.randint(1, 36)
#        if random_cart>1:
#            if c1!='none':
#                userCart.append(c1)
#                c1.write('none')
#                take = 1




#def up():
@bot.command()
async def test(ctx):
    await ctx.send(world1['90'] + world1['91'] + world1['92'] + world1['93'] + world1['94'] + world1['95'] + world1['96'] + world1['97'] + world1['98'] + world1['99'] + '\n'
+ world1['80'] + world1['81'] + world1['82'] + world1['83'] + world1['84'] + world1['85'] + world1['86'] + world1['87'] + world1['88'] + world1['89'] + '\n'
+ world1['70'] + world1['71'] + world1['72'] + world1['73'] + world1['74'] + world1['75'] + world1['76'] + world1['77'] + world1['78'] + world1['79'] + '\n'
+ world1['60'] + world1['61'] + world1['62'] + world1['63'] + world1['64'] + world1['65'] + world1['66'] + world1['67'] + world1['68'] + world1['69'] + '\n'
+ world1['50'] + world1['51'] + world1['52'] + world1['53'] + world1['54'] + world1['55'] + world1['56'] + world1['57'] + world1['58'] + world1['59'] + '\n'
+ world1['40'] + world1['41'] + world1['42'] + world1['43'] + world1['44'] + world1['45'] + world1['46'] + world1['47'] + world1['48'] + world1['49'] + '\n'
+ world1['30'] + world1['31'] + world1['32'] + world1['33'] + world1['34'] + world1['35'] + world1['36'] + world1['37'] + world1['38'] + world1['39'] + '\n'
+ world1['20'] + world1['21'] + world1['22'] + world1['23'] + world1['24'] + world1['25'] + world1['26'] + world1['27'] + world1['28'] + world1['29'] + '\n'
+ world1['10'] + world1['11'] + world1['12'] + world1['13'] + world1['14'] + world1['15'] + world1['16'] + world1['17'] + world1['18'] + world1['19'] + '\n'
+ world1['00'] + world1['01'] + world1['02'] + world1['03'] + world1['04'] + world1['05'] + world1['06'] + world1['07'] + world1['08'] + world1['09'])

@bot.command()
async def map(ctx):
    embed = discord.Embed(
        title=('карта мира'),
        description=(world1['90'] + world1['91'] + world1['92'] + world1['93'] + world1['94'] + world1['95'] + world1['96'] + world1['97'] + world1['98'] + world1['99'] + '\n'
    + world1['80'] + world1['81'] + world1['82'] + world1['83'] + world1['84'] + world1['85'] + world1['86'] + world1['87'] + world1['88'] + world1['89'] + '\n'
    + world1['70'] + world1['71'] + world1['72'] + world1['73'] + world1['74'] + world1['75'] + world1['76'] + world1['77'] + world1['78'] + world1['79'] + '\n'
    + world1['60'] + world1['61'] + world1['62'] + world1['63'] + world1['64'] + world1['65'] + world1['66'] + world1['67'] + world1['68'] + world1['69'] + '\n'
    + world1['50'] + world1['51'] + world1['52'] + world1['53'] + world1['54'] + world1['55'] + world1['56'] + world1['57'] + world1['58'] + world1['59'] + '\n'
    + world1['40'] + world1['41'] + world1['42'] + world1['43'] + world1['44'] + world1['45'] + world1['46'] + world1['47'] + world1['48'] + world1['49'] + '\n'
    + world1['30'] + world1['31'] + world1['32'] + world1['33'] + world1['34'] + world1['35'] + world1['36'] + world1['37'] + world1['38'] + world1['39'] + '\n'
    + world1['20'] + world1['21'] + world1['22'] + world1['23'] + world1['24'] + world1['25'] + world1['26'] + world1['27'] + world1['28'] + world1['29'] + '\n'
    + world1['10'] + world1['11'] + world1['12'] + world1['13'] + world1['14'] + world1['15'] + world1['16'] + world1['17'] + world1['18'] + world1['19'] + '\n'
    + world1['00'] + world1['01'] + world1['02'] + world1['03'] + world1['04'] + world1['05'] + world1['06'] + world1['07'] + world1['08'] + world1['09'] + '\n' + '\n' +
                     '❤ваше здоровье: ' + world1['health']),
        colour=discord.Colour.from_rgb(0, 140, 0)
    )
    await ctx.send(embed=embed)


@bot.command()

async def log(ctx):

    for i in int(len(log)+1):
        send = str(str(send) + str(log[i+1]) + '      /      ')
    await ctx.send(send)

@bot.command()

async def rand_cart(ctx):
    global allcart
    allcart = ['6♥', '7♥', '8♥', '9♥', '10♥', 'B♥', 'Q♥', 'K♥', 'A♥',
               '6♦', '7♦', '8♦', '9♦', '10♦', 'B♦', 'Q♦', 'K♦', 'A♦',
               '6♠', '7♠', '8♠', '9♠', '10♠', 'B♠', 'Q♠', 'K♠', 'A♠',
               '6♣', '7♣', '8♣', '9♣', '10♣', 'B♣', 'Q♣', 'K♣', 'A♣']

@bot.command()

async def go(ctx):
    global save
    global reply
    global g
    global map1
    save = []
    id = str(ctx.message.author.id) + '.txt'
    with open(id, 'r') as f:
        for line in f:
            for word in line.split():
                save.append(word)
    global s
    global XP
    aY1 = int(save[8])
    aX1 = int(save[9])
    aY2 = int(save[10])
    aX2 = int(save[11])
    pY = int(save[0])
    pX = int(save[1])
    health = int(save[2])
    day = int(save[3])
    food = int(save[4])
    hunger = int(save[5])
    XP = int(save[6])
    map = int(save[7])
    s = ':black_large_square:'
    do = ctx.message.content
    if do=='c.go up':
        pY = pY+1
        reply = "вы выбрали действие движения вверх"
    elif do=='c.go down':
        pY = pY-1
        reply = "вы выбрали действие движения вниз"
    elif do=='c.go right':
        pX = pX+1
        reply = "вы выбрали действие движения вправо"
    elif do=='c.go left':
        pX = pX-1
        reply = "вы выбрали действие движения влево"
    elif do=='c.go hunt':
        pYX = str(pY) + str(pX)
        rand = 0
        if map1[pYX] == g:
            rand = 3
            reply = 'вы по охотились на поляне'
        elif map1[pYX] == s or map1[pYX]==y:
            rand = 1
            reply = 'вы по охотились в пустыне'
        elif map1[pYX] == o:
            rand = 5
            reply = 'вы по охотились в песчаных скалах'
        food = food + random.randint(0, rand)
        health = health - random.randint(0, 3)
    elif do=='c.go eat' and food>0:
        hunger = hunger + 3
        health = health + random.randint(0, 1)
        food = food - 1
        reply = 'вы востановили силы'
    else:
        reply = "вы пропустили ход либо не правильно вввели действие \n действия движения: up; down; right; left; \n действия с едой: eat; hunt; fish; \n действия игровые: win; stats;"
    pYX = str(pY) + str(pX)
    day = day + 1
    hunger = hunger - 1
    if map1[pYX] ==r:
        health = 0
    if health < 1 or hunger < 1:
        XP = int(save[6])
        XP = XP + day
        reply = 'вы умерли и весь ваш прогресс анулируеться \n ✳XP: ' + str(XP)
        userstat = '0 ' + '0 ' + '10 ' + '1 ' + '0 ' + '10 ' + str(XP) + ' ' + '0' + ' ' + '0' + ' ' + '0' + ' ' + '0' + ' '
        id = str(ctx.message.author.id) + '.txt'
        a = open(id, 'w')
        a.write(userstat)
        a.close()
    else:
        health = health + 1
    if health > 10:
        health = 10
    if hunger > 10:
        hunger = 10
        if day > 49:
            if aY1 > pY:
                aY1 = aY1 - 1
            if aY1 < pY:
                aY1 = aY1 + 1
            if aX1 > pX:
                aX1 = aX1 - 1
            if aX1 < pX:
                aX1 = aX1 + 1
    if aY1 == pY and aX1 == pX:
        anim = day / 5 + 2
        play = health + hunger + food
        if play

    if map == 1:
        world1 = {
        'health': str(health),
        '00': str(g),
        '01': str(g),
        '02': str(g),
        '03': str(g),
        '04': str(g),
        '05': str(g),
        '06': str(g),
        '07': str(g),
        '08': str(g),
        '09': str(g),
        '10': str(g),
        '11': str(g),
        '12': str(g),
        '13': str(g),
        '14': str(g),
        '15': str(g),
        '16': str(g),
        '17': str(g),
        '18': str(g),
        '19': str(y),
        '20': str(g),
        '21': str(g),
        '22': str(g),
        '23': str(g),
        '24': str(g),
        '25': str(g),
        '26': str(g),
        '27': str(g),
        '28': str(y),
        '29': str(y),
        '30': str(g),
        '31': str(g),
        '32': str(g),
        '33': str(g),
        '34': str(g),
        '35': str(g),
        '36': str(g),
        '37': str(g),
        '38': str(y),
        '39': str(y),
        '40': str(g),
        '41': str(g),
        '42': str(g),
        '43': str(g),
        '44': str(g),
        '45': str(g),
        '46': str(g),
        '47': str(g),
        '48': str(y),
        '49': str(y),
        '50': str(g),
        '51': str(g),
        '52': str(g),
        '53': str(g),
        '54': str(g),
        '55': str(g),
        '56': str(g),
        '57': str(y),
        '58': str(y),
        '59': str(y),
        '60': str(g),
        '61': str(g),
        '62': str(g),
        '63': str(g),
        '64': str(g),
        '65': str(g),
        '66': str(y),
        '67': str(y),
        '68': str(y),
        '69': str(y),
        '70': str(g),
        '71': str(g),
        '72': str(g),
        '73': str(y),
        '74': str(y),
        '75': str(y),
        '76': str(y),
        '77': str(y),
        '78': str(y),
        '79': str(o),
        '80': str(s),
        '81': str(s),
        '82': str(s),
        '83': str(y),
        '84': str(y),
        '85': str(y),
        '86': str(y),
        '87': str(y),
        '88': str(o),
        '89': str(o),
        '90': str(s),
        '91': str(r),
        '92': str(s),
        '93': str(y),
        '94': str(y),
        '95': str(y),
        '96': str(y),
        '97': str(y),
        '98': str(o),
        '99': str(o),
        }
    world1[pYX] = str(p)
    print(pYX)
    print(ctx.message.content)
    userstat = str(pY) +  " " + str(pX) + " " +  str(health) + " " + str(day) + " " + str(food) + " " + str(hunger) + " " + str(XP) + " " + str(map) + ' ' + str(aY1) + ' ' + str(aX1) + ' ' + str(aY2) + ' ' + str(aX2)
    a = open(id, 'w')
    a.write(userstat)
    a.close()
    embed = discord.Embed(
        title='карта мира',
        description=(world1['90'] + world1['91'] + world1['92'] + world1['93'] + world1['94'] + world1['95'] + world1['96'] + world1['97'] + world1['98'] + world1['99'] + '\n'
    + world1['80'] + world1['81'] + world1['82'] + world1['83'] + world1['84'] + world1['85'] + world1['86'] + world1['87'] + world1['88'] + world1['89'] + '\n'
    + world1['70'] + world1['71'] + world1['72'] + world1['73'] + world1['74'] + world1['75'] + world1['76'] + world1['77'] + world1['78'] + world1['79'] + '\n'
    + world1['60'] + world1['61'] + world1['62'] + world1['63'] + world1['64'] + world1['65'] + world1['66'] + world1['67'] + world1['68'] + world1['69'] + '\n'
    + world1['50'] + world1['51'] + world1['52'] + world1['53'] + world1['54'] + world1['55'] + world1['56'] + world1['57'] + world1['58'] + world1['59'] + '\n'
    + world1['40'] + world1['41'] + world1['42'] + world1['43'] + world1['44'] + world1['45'] + world1['46'] + world1['47'] + world1['48'] + world1['49'] + '\n'
    + world1['30'] + world1['31'] + world1['32'] + world1['33'] + world1['34'] + world1['35'] + world1['36'] + world1['37'] + world1['38'] + world1['39'] + '\n'
    + world1['20'] + world1['21'] + world1['22'] + world1['23'] + world1['24'] + world1['25'] + world1['26'] + world1['27'] + world1['28'] + world1['29'] + '\n'
    + world1['10'] + world1['11'] + world1['12'] + world1['13'] + world1['14'] + world1['15'] + world1['16'] + world1['17'] + world1['18'] + world1['19'] + '\n'
    + world1['00'] + world1['01'] + world1['02'] + world1['03'] + world1['04'] + world1['05'] + world1['06'] + world1['07'] + world1['08'] + world1['09'] + '\n' + '\n' +
                     '🎈текущий день: '+ str(day) + '\n' +'❤ваше здоровье: '  + str(health) + '\n' +'🍖ваш голод: '  + str(hunger) +'\n'+'🌾количество еды: ' + str(food) +'\n'+'🌄ваш биом: '+map1[pYX]+'\n'+'\n'+ reply),
        colour=discord.Colour.from_rgb(0, 0, 200)
    )
    await ctx.send(embed=embed)


bot.run(settings['token'])