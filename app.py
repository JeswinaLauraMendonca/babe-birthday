import streamlit as st
from pathlib import Path
import random

st.set_page_config(page_title="For My Babe ❤️",page_icon="❤️",layout="wide")
ROOT=Path(__file__).parent
IMAGES=ROOT/"assets"/"images"
VIDEOS=ROOT/"assets"/"videos"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');
html,body,[data-testid="stAppViewContainer"]{background:radial-gradient(ellipse at 12% 0%,#501226 0%,#1a0a12 42%,#080609 82%)!important;color:#f8eee7!important}
[data-testid="stHeader"]{background:transparent!important}.block-container{max-width:1180px;padding-top:2rem;padding-bottom:5rem}
h1,h2,h3{font-family:'Cormorant Garamond',serif!important;color:#e7c98c!important}
p,li{color:#f3e5df}.hero{padding:5rem 1.2rem;text-align:center;border:1px solid #d7b36b66;border-radius:28px;background:linear-gradient(135deg,#35101fef,#10090eed);box-shadow:0 25px 80px #0009}
.hero h1{font-size:clamp(3.4rem,8vw,6.8rem);line-height:.94;margin:.6rem 0}.eyebrow{font-size:.72rem;letter-spacing:5px;color:#d8a9ae}
.goldline{height:2px;width:90px;background:#e7c98c;margin:1.4rem auto}.section{padding:2.8rem 0 1rem}.section h2{font-size:2.8rem;margin:.2rem 0}
.card{background:linear-gradient(145deg,#391324,#170b13);border:1px solid #d4ad6c66;border-radius:18px;padding:1.3rem;min-height:120px;margin-bottom:.7rem}
.card h3{font-size:1.6rem;margin:0 0 .4rem}.quote{font-family:'Cormorant Garamond',serif;font-size:1.65rem;color:#f1dcae;text-align:center;padding:2rem}
.stButton>button{background:linear-gradient(110deg,#74152f,#b52c4c)!important;color:white!important;border:1px solid #e7c98c99!important;border-radius:28px!important;padding:.55rem 1.1rem!important}
.stButton>button:hover{box-shadow:0 0 24px #cf8b7b77!important;border-color:#f6dba2!important}
div[data-testid="stExpander"]{background:#200d17;border:1px solid #c69a6555;border-radius:14px}footer{visibility:hidden}
</style>
""",unsafe_allow_html=True)

def sec(k,t,s=""):
    st.markdown(f'<div class="section"><div class="eyebrow">{k}</div><h2>{t}</h2><p>{s}</p><div class="goldline" style="margin-left:0"></div></div>',unsafe_allow_html=True)
def card(t,b):
    st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>',unsafe_allow_html=True)

st.markdown("""<div class="hero"><div class="eyebrow">A LITTLE SURPRISE MADE JUST FOR YOU</div>
<h1>Happy Birthday,<br>My Babe <span style="color:#b83250">♥</span></h1><div class="goldline"></div>
<p>November 4 · Your day, your story, our memories.</p>
<p style="font-family:'Cormorant Garamond';font-size:1.55rem;color:#e7c98c">“Some people feel like home. You are that person to me.”</p></div>""",unsafe_allow_html=True)
st.markdown('<div class="quote">From April 2025 to all the little moments that became ours — I am so glad I found you. ❤️</div>',unsafe_allow_html=True)

sec("OUR LITTLE TIME CAPSULE","The memories gallery","Every picture holds a moment I want to keep.")
photos=sorted([p for p in IMAGES.glob("*") if p.suffix.lower() in [".jpg",".jpeg",".png",".webp"]])
for start in range(0,len(photos),3):
    cols=st.columns(3)
    for col,p in zip(cols,photos[start:start+3]):
        with col: st.image(str(p),use_container_width=True)

sec("PRESS PLAY","Our moving memories","Choose a clip and relive the moment.")
videos=sorted([p for p in VIDEOS.glob("*") if p.suffix.lower() in [".mp4",".mov",".webm"]])
for start in range(0,len(videos),2):
    cols=st.columns(2)
    for col,p in zip(cols,videos[start:start+2]):
        with col:
            st.markdown("**"+p.stem.replace("-"," ").replace("_"," ").title()+"**")
            st.video(str(p))

sec("THE THINGS I LOVE","A thousand little reasons","But here are a few I never want you to forget.")
reasons=["The way you explain things and the way your mind works.","How thoughtfully you care for your mother and your family.","You make me feel understood, safe and never pressured.","Your maturity, kindness, intelligence and gentlemanly heart.","You changed the way I see love and made forever feel beautiful.","I want to support you, care for you and celebrate every version of you."]
for i in range(0,len(reasons),2):
    l,r=st.columns(2)
    with l: card("♥ A reason",reasons[i])
    with r:
        if i+1<len(reasons): card("♥ Another reason",reasons[i+1])

sec("MAKE A WISH","A cake just for you","Take a breath, make a wish and let the birthday magic happen.")
if "candles_out" not in st.session_state: st.session_state.candles_out=False
st.markdown('<div class="quote">🕯️ 🕯️ 🕯️ 🕯️ 🕯️<br><span style="font-size:5rem">🎂</span><br>Happy Birthday, Babe!</div>',unsafe_allow_html=True)
if st.button("💨 Blow out the candles" if not st.session_state.candles_out else "🕯️ Light the candles again"):
    st.session_state.candles_out=not st.session_state.candles_out
    if st.session_state.candles_out: st.balloons()
    st.rerun()
if st.session_state.candles_out: st.success("All your wishes deserve to come true. ❤️")
if st.button("🔪 Cut the cake"): st.balloons(); st.toast("A sweet birthday wish for my sweetest person! ❤️")

sec("GAME TIME · 01","Match the memories","Find all three matching pairs.")
pairs=["🌹 Rose","🎬 Movie","🌃 City lights"]
if "deck" not in st.session_state:
    d=pairs*2; random.shuffle(d); st.session_state.deck=d; st.session_state.opened=[]; st.session_state.matched=[]
if st.button("↻ Restart matching game"):
    d=pairs*2; random.shuffle(d); st.session_state.deck=d; st.session_state.opened=[]; st.session_state.matched=[]; st.rerun()
cols=st.columns(3)
for i,item in enumerate(st.session_state.deck):
    with cols[i%3]:
        label=item if i in st.session_state.opened or i in st.session_state.matched else "❔"
        if st.button(label,key=f"match{i}",use_container_width=True):
            if i not in st.session_state.opened and i not in st.session_state.matched and len(st.session_state.opened)<2:
                st.session_state.opened.append(i)
                if len(st.session_state.opened)==2:
                    x,y=st.session_state.opened
                    if st.session_state.deck[x]==st.session_state.deck[y]: st.session_state.matched.extend([x,y])
                    st.session_state.opened=[]
                st.rerun()
if len(st.session_state.matched)==6: st.success("You matched every memory! A perfect pair. ❤️")
else: st.caption(f"Pairs found: {len(st.session_state.matched)//2} / 3")

sec("GAME TIME · 02","Pick a heart, babe","Each heart has a little message hidden inside.")
msgs=["You are my favourite hello and my hardest goodbye. ❤️","Your smile is one of my favourite views. ✨","If I could relive a day, I'd choose another day with you. 🌹","I am always cheering for you, even from far away. 💌","You make ordinary moments feel special. 🥹","One day, let's make a thousand more memories. ♾️"]
cols=st.columns(3)
for i in range(6):
    with cols[i%3]:
        if st.button(f"❤️ Choose heart {i+1}",key=f"heart{i}",use_container_width=True): st.session_state.chosen=i
if "chosen" in st.session_state: st.markdown(f'<div class="quote">{msgs[st.session_state.chosen]}</div>',unsafe_allow_html=True)

sec("OPEN WHEN YOU ARE READY","A letter for my babe","A few things I want you to carry with you.")
with st.expander("💌 Tap here to open your letter"):
    st.markdown("""**My love,**

I love the way you think, the way you explain things, and the care you show the people you love. You make me feel heard and understood. You have changed the way I look at love, and with you, the idea of a future feels warm and beautiful.

I want to stand beside you through the easy days and the difficult ones. Your happiness matters to me, your family matters to me, and I hope we keep building memories together.

Happy birthday, babe. I am so grateful for you.

**Always yours. ❤️**""")
st.markdown('<div class="hero" style="margin-top:3rem;padding:3rem 1rem"><div class="eyebrow">ONE LAST THING</div><h2 style="font-size:3.1rem">Happy Birthday, my favourite person.</h2><p>May life be gentle with you, may your dreams find you, and may you never forget how loved you are.</p><div class="goldline"></div><p style="color:#e7c98c">With all my love · Forever and always ♥</p></div>',unsafe_allow_html=True)
