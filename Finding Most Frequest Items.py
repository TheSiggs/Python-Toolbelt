from collections import Counter

story = '''
It starts with a smile. You look into my eyes for a brief moment as we walk toward each other in the courtyard at the college. The trees hum in the wind. A few leaves fall down. We’re lost in a crowd of people but there it is. I see your face and you see mine and you tilt your head, lips curved up with interest. I smile back and I don’t think of you.
Not for five minutes. At night I try to remember your face, but my brain keeps replacing yours with someone else’s. I strain, but it doesn’t fade into reality. I wonder if you’re special. I figure I spent too much time dreaming again. I decide to give up on you. It doesn’t work.
Not for a week. I see you again at the school cafe. The smell of coffee fills the air and I’m warm in a sweater I bought last year. There are many conversations and they hum into meaningless noise. I look at you and I know your face. I try to memorize it. You don’t look my way.
Not for ten minutes. By then your stomach’s full of pumpkin bread and your head repeats that song for hours. You don’t remember where you heard it and you can’t quite catch the lyrics in your head. It plays over and over and it’s my new favorite song.
I wake up every morning and wonder if I’ll see you again. I remember your face. I halfheartedly browse mutual friends on Facebook to see if I notice you. I give up after five minutes. I remind myself not to get my hopes up again. I decide to stop thinking about you. It doesn’t last.
Not for two nights. I wake up too early. I’ve rolled on my phone in the middle of the night and pressed play on that song again. I lie awake at three in the morning, considering my feelings on fate. I drift off again and wake up late for class. I rush out of bed and swear in traffic. I don’t make it in time.
Not for half an hour. The teacher locks the door and won’t let in any tardy students. I wander over to the library to waste time. I see you. The computers hum and it’s nearly empty. It’s early and most people at the college are in class at this time. You look up and smile. Your eyes know mine.
I sit at the table next to yours and pull out a novel to read. It’s for a class. I wish I had something more interesting to show off my personality. I clear my throat and try to look intently at the book. But I’m staring out my peripherals trying to even my breath. You say nothing.
Not for a minute.
“Hi.”
My heart beats fast and I can feel the cold laminated wood of the table under my hands. I can smell a muffin from breakfast on my breath. I look at you and give you a bright smile. You don’t kiss me.
Not for two weeks. We’re seeing a movie we’re both excited about. It doesn’t disappoint. You smile and hold my hand as we walk out, the LED lights glowing on the floor. The smell of popcorn and the feeling of a cherry slushie mixed with infatuation sits in my gut. I’m telling you my thoughts and you look at me with interest. We stand outside and there are few stars. People stream past us in an ocean of reviews as you look into my eyes softly, kindly. The fluorescent lights hum along to the flight of the moths. You brush a hair out of my face and kiss me. Sparks erupt in my heart. My synapses fire. But I don’t love you.
Not for six months. We’re sitting on a pier with sushi on our plates. Your coat is around me and we look out at the ocean as the sun sets. Peach- and atlas- colored clouds are painted at the border of the ocean’s skin. My cheeks hurt from laughing all evening. You look at me and I find myself so full of contentment I might burst. You hum our song and a soft breeze pulls at my hair.
“I love you.”
You don’t say anything back.
Not for one second.
“I love you, too.”
We kiss and hold each other for a long time. I feel like I’m dreaming. It’s a moment of pure bliss. We hold hands when we walk together. We make each other breakfast. We moan at night, woven together under blankets. We go to cafes. We scream on rollercoasters. We go to Paris. Tokyo. London. We don’t come home.
Not for three months. We drag our feet across our welcome mats, exhausted. We sleep a lot. We listen to the rain outside. We begin to dread the length of road between our homes. We look at matching plates and cups. We talk about how it’s the same effort to lift or lower the seat of the toilet. We don’t move in together.
Not for two months. We sweat in the summer heat. We argue about fans and air conditioners. We get used to each other’s bodies. We eat frozen burritos for breakfast. We agree on a coffee brand. We work longer hours to make things easier. We don’t have sex.
Not for two weeks. We shout over what’s recyclable or not. We disagree on whether one-ply is worth it. We hate our brand of mouth wash. We fall into bed. We let out our frustrations. We talk all night. We vow to communicate more. We learn to discuss instead. We don’t fight.
Not for one day. We forget. We talk again. We fuck again. We don’t get mad.
Not for one month. Your ex comes back in town. She’s doing well. She looks amazing. You meet her for coffee to catch up. She wants you back again. I am hurt, but I say nothing.
Not for two weeks. You’ve seen her three more times. You stay longer each time. We have the worst fight we’ve ever had. We don’t know why it’s not working.
Not for two months. We disagree on politics. We have different goals. You like dogs. I like cats. It should be seventy-five degrees, not seventy-nine. I don’t want kids. You want three. We don’t break up.
Not for a few more months. We fall out of love. We want other people. We get angry. We have different opinions. We wait out the lease. We sign papers. We say goodbye. We don’t talk again.
Not once.
'''

words = story.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)

























