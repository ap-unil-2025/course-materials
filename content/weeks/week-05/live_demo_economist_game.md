# Live Demo: "The Economist's Coffee Shop" 
## An Interactive Economic Simulation Game

### The Challenge (5 minutes to build!)
"Create a text-based coffee shop simulation where students play as economists managing supply, demand, and pricing in real-time"

### Live Demo Script

```markdown
## Part 1: The Setup (30 seconds)
"Class, let's build something fun together! We'll create an economics game in 5 minutes using Claude/Cursor/Aider"

## Part 2: The Prompt (Copy this exactly)
```

**Initial Prompt to Agent:**
```
Create a fun Python text-based game called "The Economist's Coffee Shop" where players manage a coffee shop for 7 days. 

The game should:
1. Start with $1000 cash and 100 units of coffee beans
2. Each day, show random customer demand (20-80 customers)
3. Let player set coffee price ($1-10 per cup)
4. Apply demand elasticity: 
   - At $3, serve 100% of demand
   - Each $1 above $3 reduces sales by 20%
   - Each $1 below $3 increases sales by 15% (capped at inventory)
5. Coffee beans cost: 1 bean = 1 cup, can buy beans at $2 each
6. Random events each day:
   - "Competitor opens!" (demand -30%)
   - "Influencer visits!" (demand +50%)  
   - "Bean shortage!" (bean price doubles)
   - "Normal day" (no change)
7. Show daily profit/loss and graph at the end
8. Win condition: End with more than $2000
9. Add emoji and colors to make it fun! ☕💰📈

Include ASCII art for the coffee shop logo.
```

### Expected Agent Output Structure:

```python
# The agent should generate something like this:
import random
import time
from typing import Dict, List, Tuple

class CoffeeShopGame:
    def __init__(self):
        self.cash = 1000
        self.beans = 100
        self.day = 1
        self.history = []
        
    def display_shop(self):
        print("""
        ☕ THE ECONOMIST'S COFFEE SHOP ☕
        ════════════════════════════════
            )))
           (((
         +-----+
         |     |]  Time to brew profits!
         `-----'
        """)
        
    def calculate_demand_with_elasticity(self, base_demand: int, price: float) -> int:
        """Apply price elasticity of demand"""
        # ... implementation
        
    def random_event(self) -> Tuple[str, float]:
        events = [
            ("📰 Competitor opened nearby!", 0.7),
            ("🌟 Influencer posted about us!", 1.5),
            ("🚨 Bean shortage crisis!", 1.0),  # affects cost not demand
            ("😊 Normal business day", 1.0)
        ]
        return random.choice(events)
        
    def run_day(self):
        # ... game logic
        
    def show_results(self):
        # ... create simple ASCII graph
```

### Live Demonstration Flow:

**Minute 1: Initial Generation**
- Copy the prompt into Claude/Cursor
- Watch it generate the base game structure
- Point out: "Look how it's creating the economic model!"

**Minute 2: First Test Run**
```bash
python coffee_shop_game.py
```
- Play one day together as a class
- "What price should we set? Let's vote!"
- Show the demand elasticity in action

**Minute 3: Add a Feature (Live)**
"The game works! But let's add something..."

**Second Prompt:**
```
Add a "marketing campaign" option that costs $200 but increases tomorrow's demand by 40%. Also add a competitor AI that adjusts their prices based on ours.
```

**Minute 4: Test Enhanced Version**
- Run the improved game
- Show how the agent handled the new complexity
- "Notice how it integrated the new feature seamlessly!"

**Minute 5: Student Challenge**
"Now each of you suggest a feature!"
- Collect 3-4 suggestions from students
- Pick the most interesting one
- Let the agent implement it live
- Examples students might suggest:
  - Weather affecting demand
  - Employee management
  - Different coffee types
  - Customer loyalty program

### Key Teaching Points During Demo:

1. **Speed**: "We built a working game in 5 minutes!"

2. **Economic Concepts**: "Look, it correctly implemented:
   - Price elasticity of demand
   - Supply and demand dynamics
   - Profit maximization
   - Market competition"

3. **Iteration**: "See how we can quickly add features and test them"

4. **Debugging**: When something breaks (it might!):
   - "This is perfect! Let's see how the agent fixes it"
   - Copy error message to agent
   - Watch it debug and fix

5. **Code Quality**: Point out:
   - Clean function structure
   - Docstrings
   - Error handling
   - Game state management

### Fun Variations for Different Classes:

**For Finance Focus:**
"The Option Trader's Dilemma" - Build a options trading simulator

**For Data Science Focus:**
"The Data Scientist's A/B Test" - Create an A/B testing game

**For Economics Focus:**
"The Central Banker's Challenge" - Manage interest rates and inflation

### Backup Plan if Demo Fails:

Have a pre-built version ready:
```python
# If live demo fails, switch to this
print("Let's look at what the agent built earlier...")
# Show pre-generated code
# Still demonstrate adding a feature live
```

### Post-Demo Discussion Questions:

1. "What would have taken longest to code manually?"
2. "What economic concepts did it get right/wrong?"
3. "How would you extend this game?"
4. "Could you build this yourself now by reviewing the code?"

### Assignment Tie-In:
"For this week's assignment, use an agent to build YOUR own economic simulation game. Requirements:
- Must model at least 2 economic principles
- Include random events
- Have win/lose conditions
- Document which parts the AI generated vs. what you modified"

---

## Why This Demo Works:

✅ **Interactive**: Students vote on prices, suggest features
✅ **Relevant**: Uses economic concepts they're learning
✅ **Visual**: ASCII art, emojis, live gameplay
✅ **Fail-Safe**: Errors become teaching moments
✅ **Memorable**: They'll remember the coffee shop game
✅ **Practical**: Shows real agent capabilities
✅ **Time-Bounded**: Exactly 5 minutes of core demo

## Materials Needed:
- Claude.ai / Cursor / Aider open and ready
- Terminal/command prompt visible to class
- Backup code file just in case
- Projector with good font size (>20pt)

## Pro Tips:
- Have students access the game on their laptops too
- Create a GitHub repo during class and push the code
- Let students fork and modify during the session
- Run a tournament: whose modified version makes most profit?