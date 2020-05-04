from random import random

import discord

client=discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game=discord.Game("김견 만세")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("견자야"):
        await message.channel.send("멍")
    if message.content.startswith("김견아"):
        await message.channel.send("왈")
    if message.content.startswith("견아"):
        await message.channel.send("왈왈")
    if message.content.startswith("사람 말"):
        await message.channel.send("뭐 시발련아")
    if message.content.startswith("뭐 시발련아"):
        await message.channel.send("왈왈")
    if message.content.startswith("권애미"):
        await message.channel.send("자자자자자자자자자자자잦자자자자ㅏ자자자자자자자자자잦자")
    if message.content.startswith("김기현"):
        await message.channel.send("만세 만세 만세")
    if message.content.startswith("자기소개 해 봐"):
        await message.channel.send("저는 동물의 왕 견자입니다")
    if message.content.startswith("산책"):
        await message.channel.send("멍멍멍멍멍멍")
    if message.content.startswith("다양하게 짖어"):
        await message.channel.send("멍왈멍왈멍왈")
    if message.content.startswith("이용호 캐리"):
        await message.channel.send("이용호세요??")
    if message.content.startswith("구민상"):
        await message.channel.send("돼지^_^")
    if message.content.startswith("장구라"):
        await message.channel.send("ㄹㄹㅋ")
    if message.content.startswith("이윤우"):
        await message.channel.send("분식의 왕 신참")
    if message.content.startswith("박기태"):
        await message.channel.send("머        두")
    if message.content.startswith("엄마 없나"):
        await message.channel.send("패드립은 나빠요^_^")
    if message.content.startswith("시 ㅡ 발"):
        await message.channel.send("욕 하지마^_^")
    if message.content.startswith("시벌"):
        await message.channel.send("욕 하지마^_^")
    if message.content.startswith("씨발"):
        await message.channel.send("욕 하지마^_^")
    if message.content.startswith("개새끼"):
        await message.channel.send("욕 하지마^_^")
    if message.content.startswith("시ㅡ발"):
        await message.channel.send("욕 하지마^_^")
    if message.content.startswith("씨ㅡ발"):
        await message.channel.send("욕 하지마^_^")
    if message.content.startswith("조정원"):
        await message.channel.send("믿거조")
    if message.content.startswith("정진안"):
        await message.channel.send("피파 ㅈ밥")
    if message.content.startswith("노준노"):
        await message.channel.send("킹 갓 회장님")
    if message.content.startswith("이준이"):
        await message.channel.send("맹                 구")
    if message.content.startswith("이용호"):
        await message.channel.send("읍읍읍읍")
    if message.content.startswith("짖어"):
        await message.channel.send("싫은데ㅋ")
    if message.content.startswith("송건우"):
        await message.channel.send("딱딱이")
    if message.content.startswith("크르릉"):
        await message.channel.send("개세요?")
    if message.content.startswith("김기현 병신"):
        await message.channel.send("ㅇ ㅇㄴㅇ")
    if message.content.startswith("병신"):
        await message.channel.send("욕 하지마^_^")
    if message.content.startswith("김기현 ㅂㅅ"):
        await message.channel.send("ㅇ ㅇㄴㅇ")
    if message.content.startswith("이재현"):
        await message.channel.send("어쩔 수 없네 잘ㄱr")
    if message.content.startswith("21"):
        await message.channel.send("ㅎㅗㅏㄴ")
    if message.content.startswith("이일환"):
        await message.channel.send("1224")
    if message.content.startswith("이일"):
        await message.channel.send("환환환환")
    if message.content.startswith("이용호 엄마"):
        await message.channel.send("silver zero")
    if message.content.startswith("야"):
        await message.channel.send("왜 불렁")
    if message.content.startswith("마인드"):
        await message.channel.send("KING GOD LEGEND")
    if message.content.startswith("용호"):
        await message.channel.send("21212121")
    if message.content.startswith("애미 없나"):
        await message.channel.send("ㄴㄱㅁ ㅅㅂㄹㅇ")
    if message.content.startswith("보신탕"):
        await message.channel.send("미안해 시발")
    if message.content.startswith("투애니원"):
        await message.channel.send("ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ")
    if message.content.startswith("누가 범인이야??"):
        await message.channel.send("구민상이요")
    if message.content.startswith("경아야"):
        await message.channel.send("빨 거 없나~^^")
    if message.content.startswith("신참"):
        await message.channel.send("엽떡 드세요^_^")
    if message.content.startswith("다딱이"):
        await message.channel.send("딱딱")
    if message.content.startswith("ㄱㅇㅁㅈ"):
        await message.channel.send("왕뽕짬")
    if message.content.startswith("병신"):
        await message.channel.send("ㅇ ㅇㄴㅇ")
    if message.content.startswith("코드네임:205"):
        await message.channel.send("205친위대가 말이 됩니까 기호 1번 동물의 왕 견자를 친위대로 올립시다 여러분")









client.run("Njk0MjkxOTI4ODIwMjE5OTU1.XoMYCQ.rh7SVIFwjMWLTwPzWqrnhEMRwxI")
