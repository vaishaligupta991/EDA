import os 
import json
import random
from datetime import datetime

REWARDS = {
    "story": [
        {"id": "jathara", "name_tel": "జాతర జయుడు", "emoji": "🎭", "points": 10},
        {"id": "katha_ratna", "name_tel": "కథా రత్నం", "emoji": "📖", "points": 15},
    ],
    "meme": [
        {"id": "navvula_veerudu", "name_tel": "నవ్వుల వీరుడు", "emoji": "😂", "points": 8},
        {"id": "chitti_fun", "name_tel": "చిట్టి ఫన్", "emoji": "🤖", "points": 10},
    ],
    "recipe": [
        {"id": "pindi_vanta", "name_tel": "పిండి వంటా పటాస్", "emoji": "🍛", "points": 12},
        {"id": "aru_mudda", "name_tel": "అరు ముద్ద", "emoji": "🥣", "points": 10},
    ],
    "art": [
        {"id": "kalaloka", "name_tel": "కళలొక", "emoji": "🎨", "points": 14},
        {"id": "rangula_ratna", "name_tel": "రంగుల రత్నం", "emoji": "🖌️", "points": 11},
    ]
}

def award_user(activity_type):
    badge = random.choice(REWARDS.get(activity_type, []))
    reward = {
        "timestamp": datetime.utcnow().isoformat(),
        "activity": activity_type,
        "badge_id": badge["id"],
        "badge_name_tel": badge["name_tel"],
        "badge_emoji": badge["emoji"],
        "points": badge["points"]
    }
    os.makedirs("data", exist_ok=True)
    with open("data/rewards.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(reward, ensure_ascii=False) + "\n")
    return reward