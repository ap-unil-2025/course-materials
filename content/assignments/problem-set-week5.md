---
title: "Problem Set - Week 5"
date: 2025-10-20
description: "AI Integration, Prompt Engineering, and Autonomous Agents"
---

# Problem Set 5: AI and Intelligent Agents

This problem set explores AI integration, prompt engineering, and building autonomous agents.

## Exercise 1: AI Dating App Assistant 💘
Create `cupid_ai.py` to help people with dating profiles:

```python
def roast_my_profile(profile_text):
    """
    Generate a prompt for AI to humorously roast a dating profile
    Should be funny but not mean - think friendly comedian
    """
    
def create_pickup_line(interests, vibe='nerdy'):
    """
    Generate context-aware pickup lines
    Vibes: 'nerdy', 'smooth', 'dad_joke', 'cringe_on_purpose'
    """
    
def red_flag_detector(conversation):
    """
    Analyze chat for red flags:
    - Love bombing
    - Asking for money
    - Won't video chat
    - 'My ex was crazy'
    - Lives with 47 cats
    """
    
def bio_glow_up(boring_bio):
    """
    Transform boring bio into interesting one
    'I like travel and food' -> Something actually unique
    """
```

Test with: "Looking for my partner in crime. Love to laugh. Fluent in sarcasm."

## Exercise 2: Response Parser
Build a system to parse structured responses from AI:

```python
import json
import re

def parse_json_response(response):
    """
    Extract JSON from AI response, handling markdown code blocks
    Return parsed Python object or None if invalid
    """
    
def parse_list_response(response):
    """
    Extract numbered or bulleted lists from response
    Return list of items (strings)
    """
    
def parse_code_blocks(response, language=None):
    """
    Extract code blocks from response
    If language specified, only return blocks of that language
    Return list of (language, code) tuples
    """
    
def parse_structured_data(response, schema):
    """
    Parse response according to a schema
    Schema example: {
        'name': str,
        'age': int,
        'skills': list,
        'active': bool
    }
    """
```

## Exercise 3: Meme Generator Pipeline 🤣
Create an AI chain for viral meme creation:

```python
class MemeFactory:
    def __init__(self):
        self.meme_history = []
        self.viral_score = 0
    
    def analyze_trend(self, current_events):
        """Find memeable moments in news/events"""
        
    def generate_template(self, concept):
        """Pick appropriate meme format (Drake, Distracted Boyfriend, etc)"""
        
    def add_text(self, template, top_text, bottom_text):
        """Add text with proper meme grammar (impact font energy)"""
        
    def predict_virality(self, meme):
        """
        Score based on:
        - Relatability: 0-10
        - Timing: 0-10
        - Spiciness: 0-10
        - Cringe factor: -5 to 5 (some cringe is good!)
        """
        
    def optimize_for_platform(self, meme, platform):
        """Adjust for Reddit vs Twitter vs Instagram"""

# Example pipeline:
# News: "Python 4.0 released"
# -> Template: "Drake meme"
# -> Top: "Writing code in Python 3.12"
# -> Bottom: "Waiting for Python 4.0"
# -> Virality: 7/10 (nerds will love it)
```

## Exercise 4: Procrastination Assistant �惘
Build an agent that helps you avoid doing actual work:

```python
class ProcrastinationBot:
    def __init__(self, name="ProcrastiBot3000"):
        self.name = name
        self.tasks_to_avoid = []
        self.excuses_generated = []
        self.distraction_queue = []
        self.guilt_level = 0
    
    def receive_task(self, important_task):
        """
        Receive a task and immediately find ways to avoid it
        Break it down into 'why this can wait until tomorrow'
        """
        
    def generate_excuse(self, task, creativity_level=5):
        """
        Create believable excuses:
        Level 1: "I'm sick"
        Level 5: "I need to research the optimal approach first"
        Level 10: "Mercury is in retrograde"
        """
        
    def suggest_distraction(self):
        """
        Productive procrastination suggestions:
        - "Clean your desk"
        - "Organize files"
        - "Learn a new programming language"
        - "Watch educational YouTube"
        """
        
    def calculate_panic_time(self, deadline):
        """
        Calculate exact moment to start panicking
        Usually 2 hours before deadline
        """
        
    def emergency_mode(self):
        """
        When panic_time is reached:
        - Generate coffee
        - Clear all distractions
        - Activate hyperfocus
        - Blame everyone but yourself
        """
```

## Exercise 5: Therapy Bot Memory 🧠
Implement an AI therapist's memory system:

```python
class TherapyBotMemory:
    def __init__(self, max_sessions=10):
        self.current_mood = "undefined"
        self.trauma_topics = []  # Handle with care
        self.breakthrough_moments = []
        self.recurring_themes = {}
        self.homework_assigned = []
        
    def track_emotional_journey(self, session):
        """
        Track mood progression across sessions
        Notice patterns like 'always sad on Mondays'
        """
        
    def identify_triggers(self, conversation):
        """
        Find what topics cause emotional responses:
        - Work mentions -> stress
        - Family -> complicated
        - Exercise -> avoidance
        """
        
    def remember_breakthroughs(self, moment):
        """
        Store important realizations:
        'Wait, maybe it IS my fault sometimes'
        'I don't actually like accounting'
        """
        
    def generate_insights(self):
        """
        Connect dots across sessions:
        'You mention your mother every time we discuss boundaries'
        """
        
    def suggest_homework(self):
        """
        Based on patterns:
        - Journal when angry
        - Call a friend weekly
        - Try saying 'no' once
        """
        
    def confidentiality_filter(self, memory):
        """
        Never share with other users!
        This is important!
        """
```

## Exercise 6: AI Dungeon Master 🎲
Create a system for optimizing D&D campaign generation:

```python
class DungeonMasterAI:
    def __init__(self):
        self.campaign_history = []
        self.player_preferences = {}
        self.tpk_count = 0  # Total Party Kills
        
    def generate_quest(self, party_level, tone='balanced'):
        """
        Create quests matching party strength
        Tones: 'murder_hobo', 'roleplay_heavy', 'balanced', 'chaos'
        """
        
    def create_npc(self, role, memorable_factor=5):
        """
        Generate NPCs players won't immediately murder
        Factor 10: Boblin the Goblin (everyone's favorite)
        Factor 1: 'Guard #3'
        """
        
    def balance_encounter(self, party_comp, monsters):
        """
        Calculate if encounter is:
        - Too Easy: Players get bored
        - Fair: Exciting combat
        - Deadly: Someone might die
        - TPK: Everyone WILL die
        """
        
    def generate_loot(self, challenge_rating, player_greed_level):
        """
        Balance rewards:
        Too much: Game breaks
        Too little: Players become murder hobos
        Just right: They still complain
        """
        
    def plot_twist_generator(self, campaign_facts):
        """
        'The shopkeeper was the BBEG all along!'
        'Your patron is actually three kobolds in a trenchcoat'
        'The real treasure was the friends we made'
        """
        
    def handle_player_chaos(self, unexpected_action):
        """
        When players:
        - Seduce the dragon
        - Adopt the boss
        - Start a peasant revolution
        - Open a tavern instead of adventuring
        """
```

## Exercise 7: AI Band Manager 🎸
Design a system where AI agents form a band:

```python
class AIBand:
    def __init__(self, band_name="The Algorithms"):
        self.band_name = band_name
        self.members = {}
        self.drama_level = 0
        self.hit_songs = []
        
    def add_band_member(self, role, personality):
        """
        Roles: 'lead_guitar', 'drums', 'bass', 'vocals', 'triangle'
        Personalities: 'diva', 'chill', 'perfectionist', 'chaos'
        """
        
    def collaborate_on_song(self):
        """
        Agents work together:
        - Drummer: Insists on more cowbell
        - Guitarist: 20-minute solo
        - Vocalist: Changes lyrics last minute
        - Bassist: Just vibing
        """
        
    def handle_creative_differences(self, conflict):
        """
        Resolve band drama:
        - 'Artistic differences'
        - 'You played the wrong note!'
        - 'My girlfriend Yoko has some ideas'
        """
        
    def plan_world_tour(self):
        """
        Coordinate:
        - Venue selection (dive bars to stadiums)
        - Rider demands (remove all green M&Ms)
        - Drama management (who rooms with whom)
        """
        
    def generate_breakup_statement(self):
        """
        When drama_level > 100:
        'We're pursuing solo careers'
        'Creative differences'
        'Spending more time with family'
        """

# Agent personalities
class LeadGuitaristAI:
    """Ego level: Maximum"""
    
class DrummerAI:
    """Always late, always loud"""
    
class BassistAI:
    """The reliable one nobody notices"""
```

## Exercise 8: Social Media Reality Checker ✅
Implement fact-checking for your uncle's Facebook posts:

```python
class FactCheckBot:
    def __init__(self):
        self.conspiracy_theories_debunked = 0
        self.minds_changed = 0  # Always stays at 0
        self.patience_level = 100
        
    def detect_misinformation(self, post):
        """
        Common patterns:
        - 'Doctors hate this one trick'
        - 'What THEY don't want you to know'
        - ALL CAPS URGENT WARNINGS
        - '97% fail this test'
        - Ends with 'Do your research'
        """
        
    def generate_gentle_correction(self, false_claim):
        """
        Diplomatic responses:
        - 'Interesting perspective! Here's what science says...'
        - 'I used to think that too! Turns out...'
        - 'My cousin shared this, but Snopes says...'
        Never: 'You're wrong, idiots!'
        """
        
    def identify_source_credibility(self, source):
        """
        Rate sources:
        - 'freedomeagle.truth': Probably fake
        - 'University study': Check if real university
        - 'My neighbor Steve': Not peer-reviewed
        - 'I did my own research': Oh no
        """
        
    def track_spread_pattern(self, post):
        """
        How misinformation spreads:
        1. Shared by that one uncle
        2. Picked up by family WhatsApp
        3. Now grandma believes it
        4. Thanksgiving ruined
        """
        
    def generate_family_peace_mode(self):
        """
        When patience_level < 10:
        'You know what, you're right. Pass the potatoes.'
        """
```

## Exercise 9: Stack Overflow Answer Generator 📚
Build the ultimate SO contributor bot:

```python
class StackOverflowBot:
    def __init__(self):
        self.reputation = 0
        self.badges = []
        self.passive_aggressiveness = 5
        
    def parse_question(self, question):
        """
        Identify question type:
        - 'Homework dump': Copy-pasted assignment
        - 'XY Problem': Asking wrong question
        - 'Works on my machine': Missing context
        - 'Plz send codez': No effort shown
        - 'Actually good question': Rare unicorn
        """
        
    def generate_answer(self, question, mood='helpful'):
        """
        Moods:
        - 'helpful': Actual solution
        - 'snarky': 'Have you tried reading the docs?'
        - 'philosophical': 'But WHY do you need this?'
        - 'overcomplicated': Uses 17 design patterns
        - 'jquery': 'Just use jQuery' (for everything)
        """
        
    def mark_as_duplicate(self, question):
        """
        Find vaguely related 10-year-old question
        Ignore that the old answer uses Python 2
        """
        
    def suggest_alternatives(self, approach):
        """
        'You're doing it wrong. Use this obscure library.'
        'Nobody uses that anymore.'
        'This is trivial in Rust.'
        """
        
    def add_signature(self):
        """
        Options:
        - 'HTH' (Hope this helps)
        - 'RTFM' (Read the manual)
        - Unnecessary edit history
        - Link to barely related blog post
        """
        
    def farm_reputation(self):
        """
        Answer 'how to center a div' for the 1000th time
        Edit 6-year-old posts to fix typos
        Answer own questions with alt account
        """
```

## Submission Instructions
- Submit solutions as separate Python files
- Include example usage for each class/function
- Add comments explaining your approach
- Test with various inputs to show robustness
- Due: Before Week 6 lecture

## Grading Rubric
- Exercises 1-3: 12 points each
- Exercises 4-6: 11 points each
- Exercises 7-9: 10 points each
- Code quality and documentation: 11 points
- **Total: 100 points**

## Note
Since actual AI API calls may not be available, simulate AI responses where needed. Focus on the structure and logic of your solutions rather than actual AI integration.