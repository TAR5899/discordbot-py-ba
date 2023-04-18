from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os, discord, asyncio, datetime, pytz
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("학생회 업무 담당"))

@client.event
async def on_message(message):
    if message.content == "안녕 린": # 메세지 감지
        await message.channel.send ("{} 선생님, 안녕하세요!".format(message.author.mention))

    if message.content == "!공지1": # 메세지 감지
        await message.channel.send ("교직원휴게실 디스코드에 오신 것을 환영합니다.\n\n저희 서클은 총력전 상위 랭크를 지향하는 서클입니다.\n\n서로간의 예의를 지켜 즐거운 게임 할 수 있도록 합시다!\n\n* 게임 미접 3일 경과시 무통보 추방되오니 꼭 서클 AP 수령해주세요.")

    if message.content == "!공지2": # 메세지 감지
        await message.channel.send ("규칙을 제대로 읽지 않아서 얻은 불이익은 전부 본인 책임이며, 모두 공유, 협력하며 도우며 즐길 수 있으면 좋겠습니다!")

    if message.content == "!!채널 알림":
        ch = client.get_channel(1038793481499451483)
        await ch.send ("채널 알림입니다")
    
    if message.content == "임베드1": # 메세지 감지
        embed = discord.Embed(title="1️⃣ 모든 채팅방은 기본적으로 존댓말 사용", description='- 즐거운 커뮤니티 사용 및 게임 이용을 위해 존댓말을 사용해 주세요.', color=0x00ff00)
        await message.channel.send (embed=embed)

    if message.content == "임베드2":
        embed = discord.Embed(title="2️⃣ 분쟁, 싸움 금지", description='- 분쟁이나 싸움을 유발 할 수 있는 민감한 소재 언급, 혹은 공개적인 채팅방이나 음성 채팅방에서 공격적인 언어, 시비, 말다툼 등을 금지합니다.\n\n - 개인적인 사유로 생긴 말다툼은 되도록 공개적인 채팅방이 아닌 개인 DM으로 해결 부탁드리며 해결이 불가능할 시에 관리자에게 연락해주세요.', color=0x00f2ff)
        await message.channel.send (embed=embed)

    if message.content == "임베드3":
        embed = discord.Embed(title="3️⃣ 남들이 봤을 때 불편할 만한 대화, 단어 사용, 사진 금지", description='- 과하게 혐오스럽거나 공포스러운 요소의 대화와 사진은 되도록 자제해 주세요.\n\n- 정치 관련 및 젠더 갈등 유발 발언은 엄금합니다.', color=0x001dff)
        await message.channel.send (embed=embed)

    if message.content == "임베드4":
        embed = discord.Embed(title="4️⃣ 부적절한 프로필 사진 금지", description='- 3️⃣에서 언급된 소재들이 보이는 프로필 사진을 금지합니다.\n\n- 해당 되는 프로필 사진은 관리자가 수정 요청을 부탁드릴 수 있습니다.', color=0xa400ff)
        await message.channel.send (embed=embed)

    if message.content == "임베드5":
        embed = discord.Embed(title="5️⃣ 서버 내에서 계정 구매 및 거래 금지", description='- 서클 서버인 만큼 계정 거래는 물론 금전적인 거래가 이뤄지지 않은 양도 또한 허용하지 않습니다.', color=0xff00d1)
        await message.channel.send (embed=embed)

    if message.content == "임베드6":
        embed = discord.Embed(title="6️⃣ 계정 보안에 신경써 주세요", description='- 본인 부주의로 해킹을 당해 밴을 당한 경우 인게임 채팅에서 글 남겨주세요.', color=0xff0004)
        await message.channel.send (embed=embed)

    if message.content == "임베드7":
        embed = discord.Embed(title="7️⃣ 자랑게시판 외의 게시판 및 음성채널에서 과도한 비틱, 자랑 금지", description='- 본인이 원했던 캐릭터를 뽑아서 자랑하고 싶은 마음은 잘 아나 게시판에서\n과도한 자랑을 하는 행위를 금지합니다.\n\n- 자랑게시판에서도 언어 사용에 신경써주시어 쾌적한 게시판 이용을\n부탁드리겠습니다.', color=0xb7ff00)
        embed.add_field(name="좋은 예", value="이로하 드디어 뽑았습니다ㅠㅠ\nㄴ 오 축하드립니다 ㅊㅊㅊ", inline=False)
        embed.add_field(name="나쁜 예", value="와카모 20연차에 나온건데 좋은건가요?\n사키 뽑을 생각 없었는데 그냥 나오네요;", inline=False)
        await message.channel.send (embed=embed)

    if message.content == "임베드8":
        embed = discord.Embed(title="8️⃣ 규칙의 기재되지 않아도 서클원들에게 피해를 주는 행위를 자제해 주세요", description='- 상호간의 예의를 잘 지켜 서로 상처받는 일이 없도록 합시다.\n\n- 규칙을 제대로 읽지 않아서 얻은 불이익은 전부 본인 책임이며,\n모두 공유, 협력하여 주신다면 감사하겠습니다!!', color=0xff6cc4)
        await message.channel.send (embed=embed) 

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
