---
layout: assignment
title: "Advanced HW6: OOP Simulation Engine & Debugging Masterclass"
assignment_number: "HW6"
due_date: 2025-11-03 23:59:00
points: 150
difficulty: "Advanced"
estimated_time: "10-12 hours"
github_classroom_url: "https://classroom.github.com/a/advanced-hw6"
starter_repo: "ap2025-advanced-hw6-starter"
topics:
  - "Advanced OOP design"
  - "Design patterns"
  - "Debugging techniques"
  - "Testing strategies"
  - "Performance profiling"
bonus: true
status: "open"
---

## Overview

**This is an OPTIONAL grade booster assignment** worth 150 bonus points. Build a complex object-oriented simulation engine, then debug increasingly difficult problems using professional debugging techniques.

## The Challenge: "City Simulation Engine"

Create a full city simulation with citizens, buildings, transportation, economy, and events. Then debug a series of complex issues in provided buggy code.

## Part 1: OOP Architecture Design (40 points)

### Core Class Hierarchy

```python
# Base classes to implement
class Entity:
    """Base class for all simulation entities"""
    def __init__(self, id, name, position):
        pass
    
    def update(self, delta_time):
        """Called each simulation tick"""
        pass
    
    def __repr__(self):
        """Debugging representation"""
        pass

class Living(Entity):
    """Base for living entities"""
    def __init__(self, id, name, position, health=100, age=0):
        pass
    
    def age_up(self):
        pass
    
    def take_damage(self, amount):
        pass

class Building(Entity):
    """Base for all buildings"""
    def __init__(self, id, name, position, capacity, cost):
        pass
    
    def can_enter(self, entity):
        pass
    
    def maintain(self):
        """Monthly maintenance"""
        pass
```

### Required Classes (Implement All)

#### Citizens
```python
class Citizen(Living):
    """
    Attributes:
    - job: Job object or None
    - home: Building object or None
    - happiness: 0-100
    - money: float
    - skills: dict of skill -> level
    - relationships: dict of citizen -> relationship_score
    - schedule: list of daily activities
    - inventory: list of items
    
    Methods:
    - work(): Perform job, earn money
    - socialize(): Build relationships
    - shop(): Buy necessities
    - rest(): Restore energy
    - find_job(): Look for employment
    - find_home(): Look for housing
    """
    pass

class Student(Citizen):
    """Citizen attending school"""
    pass

class Worker(Citizen):
    """Employed citizen"""
    pass

class Retiree(Citizen):
    """Retired citizen"""
    pass
```

#### Buildings
```python
class Residential(Building):
    """Houses citizens"""
    pass

class Commercial(Building):
    """Shops and services"""
    pass

class Industrial(Building):
    """Factories and production"""
    pass

class School(Building):
    """Education facility"""
    pass

class Hospital(Building):
    """Healthcare facility"""
    pass

class Park(Building):
    """Recreation area"""
    pass
```

#### Transportation
```python
class Vehicle(Entity):
    """Base vehicle class"""
    pass

class Bus(Vehicle):
    """Public transport"""
    pass

class Car(Vehicle):
    """Private transport"""
    pass

class Bicycle(Vehicle):
    """Eco-friendly transport"""
    pass

class TransportNetwork:
    """Manages all transportation"""
    def find_route(self, start, end):
        """Pathfinding algorithm"""
        pass
```

#### Economy System
```python
class Economy:
    """
    Manages city economy:
    - Jobs and employment
    - Supply and demand
    - Prices and inflation
    - Taxes and budget
    """
    pass

class Job:
    """
    Job definition:
    - title, salary, requirements
    - schedule, location
    - satisfaction factors
    """
    pass

class Market:
    """
    Marketplace for goods:
    - products with prices
    - supply/demand curves
    - price adjustments
    """
    pass
```

### Design Patterns to Implement

#### 1. Observer Pattern (8 points)
```python
class EventSystem:
    """Publish-subscribe for game events"""
    def subscribe(self, event_type, callback):
        pass
    
    def publish(self, event):
        pass

class Event:
    """Base event class"""
    pass

class CitizenBornEvent(Event):
    pass

class BuildingConstructedEvent(Event):
    pass
```

#### 2. Factory Pattern (8 points)
```python
class EntityFactory:
    """Creates entities from configuration"""
    @staticmethod
    def create_citizen(config):
        pass
    
    @staticmethod
    def create_building(building_type, config):
        pass
```

#### 3. Strategy Pattern (8 points)
```python
class AIBehavior:
    """Base AI behavior"""
    def decide_action(self, citizen, context):
        pass

class WorkerBehavior(AIBehavior):
    pass

class StudentBehavior(AIBehavior):
    pass

class LeisureBehavior(AIBehavior):
    pass
```

#### 4. Singleton Pattern (8 points)
```python
class SimulationEngine:
    """Singleton that runs the simulation"""
    _instance = None
    
    def __new__(cls):
        pass
    
    def run(self):
        pass
```

#### 5. Decorator Pattern (8 points)
```python
class BuildingModifier:
    """Decorates buildings with upgrades"""
    pass

class SolarPanels(BuildingModifier):
    """Reduces energy costs"""
    pass

class SecuritySystem(BuildingModifier):
    """Improves safety"""
    pass
```

## Part 2: Advanced Features (30 points)

### Time System (10 points)
```python
class TimeManager:
    """
    Manages simulation time:
    - Hours, days, months, years
    - Speed control (pause, 1x, 2x, 5x)
    - Scheduled events
    - Seasonal effects
    """
    pass

class Schedule:
    """Daily schedule for citizens"""
    pass

class SeasonalEffect:
    """Weather and seasonal changes"""
    pass
```

### Pathfinding System (10 points)
```python
class PathFinder:
    """
    A* pathfinding implementation:
    - Grid-based navigation
    - Obstacle avoidance
    - Traffic consideration
    - Multiple transport modes
    """
    pass
```

### Statistics and Analytics (10 points)
```python
class CityStatistics:
    """
    Track and analyze:
    - Population demographics
    - Economic indicators
    - Happiness index
    - Crime rate
    - Education level
    - Health metrics
    - Environmental quality
    
    Generate reports and visualizations
    """
    pass
```

## Part 3: Debugging Challenge (40 points)

### Debugging Scenarios

You'll receive 5 buggy simulation files. Each has multiple bugs of different types. Your task is to:

1. **Identify all bugs** using debugging techniques
2. **Fix the bugs** properly
3. **Write tests** to prevent regression
4. **Document** your debugging process

#### Scenario 1: The Population Crisis (8 points)
```python
# buggy_population.py
"""
Bug symptoms:
- Citizens randomly disappear
- Population count becomes negative
- Citizens duplicate themselves
- Age increases exponentially

Use debugging techniques:
- Print debugging
- Assertions
- Logging
- Unit tests
"""
```

#### Scenario 2: The Economic Collapse (8 points)
```python
# buggy_economy.py
"""
Bug symptoms:
- Money becomes infinite
- Prices go negative
- Jobs pay nothing
- Market crashes randomly

Use debugging techniques:
- Debugger breakpoints
- Watch variables
- Call stack analysis
- State inspection
"""
```

#### Scenario 3: The Traffic Nightmare (8 points)
```python
# buggy_transport.py
"""
Bug symptoms:
- Vehicles teleport
- Pathfinding infinite loops
- Buses carry negative passengers
- Roads disconnect randomly

Use debugging techniques:
- Step-through debugging
- Conditional breakpoints
- Memory profiling
- Performance profiling
"""
```

#### Scenario 4: The Memory Monster (8 points)
```python
# buggy_memory.py
"""
Bug symptoms:
- Memory usage grows infinitely
- Deleted objects persist
- Circular references
- Resource leaks

Use debugging techniques:
- Memory profilers
- Garbage collection analysis
- Reference counting
- Weak references
"""
```

#### Scenario 5: The Race Condition (8 points)
```python
# buggy_concurrent.py
"""
Bug symptoms:
- Random crashes
- Inconsistent state
- Deadlocks occasionally
- Data corruption

Use debugging techniques:
- Thread safety analysis
- Lock debugging
- Race condition detection
- Synchronization fixes
"""
```

### Debugging Report Format

For each scenario, create a report:

```markdown
# Debugging Report: [Scenario Name]

## Initial Investigation
### Symptoms Observed
- [List all symptoms]

### Hypothesis
[Initial thoughts on causes]

## Debugging Process

### Step 1: [Technique Used]
```python
# Code or commands used
```
**Finding**: [What you discovered]

### Step 2: [Next Technique]
[Continue for all steps]

## Root Causes Identified

### Bug 1: [Description]
- **Location**: [File:line]
- **Type**: [Logic/Memory/Concurrency/etc]
- **Impact**: [What it breaks]
- **Fix Applied**:
```python
# Fixed code
```

### Bug 2: [Continue for all bugs]

## Testing

### Test Cases Added
```python
def test_[name]():
    """Test to prevent regression"""
    pass
```

## Lessons Learned
[Key takeaways from this debugging session]
```

## Part 4: Testing Suite (20 points)

### Comprehensive Testing

Create a full testing suite for your simulation:

#### Unit Tests (10 points)
```python
# test_citizens.py
class TestCitizen:
    def test_creation(self):
        """Test citizen initialization"""
        pass
    
    def test_aging(self):
        """Test age progression"""
        pass
    
    def test_work_income(self):
        """Test job and money"""
        pass
    
    def test_relationships(self):
        """Test social interactions"""
        pass
    
    # ... minimum 20 unit tests
```

#### Integration Tests (5 points)
```python
# test_integration.py
class TestCityIntegration:
    def test_citizen_building_interaction(self):
        """Test citizens entering buildings"""
        pass
    
    def test_economy_flow(self):
        """Test money circulation"""
        pass
    
    def test_transport_system(self):
        """Test complete journey"""
        pass
    
    # ... minimum 10 integration tests
```

#### Performance Tests (5 points)
```python
# test_performance.py
class TestPerformance:
    def test_simulation_speed(self):
        """Ensure 1000 citizens run at 30 FPS"""
        pass
    
    def test_memory_usage(self):
        """Check memory doesn't exceed limits"""
        pass
    
    def test_pathfinding_performance(self):
        """Pathfinding under 10ms"""
        pass
```

## Part 5: Visualization and UI (20 points)

### ASCII Visualization

Create a text-based UI for the simulation:

```
╔════════════════════════════════════════════════════════════╗
║  CITY SIMULATION v1.0  │  Day: 42  Time: 14:30  Speed: 2x  ║
╠════════════════════════════════════════════════════════════╣
║  Map View (20x10)                   │  Statistics          ║
║  ┌────────────────────────────────┐ │  Population: 523    ║
║  │RRRR  CCC  III  ████  RRR      │ │  Happiness: 72%     ║
║  │R🏠R  C🏪C  I🏭I  ████  R🏠R    │ │  Employment: 89%    ║
║  │RRRR  CCC  III  ████  RRR      │ │  GDP: $1.2M         ║
║  │                                │ │  Crime Rate: 3%     ║
║  │████  PPP  HHH  SSS   ████     │ │                     ║
║  │████  P🌳P  H🏥H  S🏫S  ████    │ │  Recent Events:     ║
║  │████  PPP  HHH  SSS   ████     │ │  • New park opened  ║
║  │                                │ │  • Traffic jam on 5 ║
║  │──🚌──🚗──🚲──────🚗──🚌────── │ │  • Baby boom (+12)  ║
║  └────────────────────────────────┘ │                     ║
╠════════════════════════════════════════════════════════════╣
║  Selected: John Smith (ID: 42)                             ║
║  Age: 34 | Job: Teacher | Home: Apt 7B | Happy: 85%       ║
║  Actions: Working at School                                ║
╠════════════════════════════════════════════════════════════╣
║  Commands: [P]ause [S]peed [B]uild [V]iew [H]elp [Q]uit   ║
╚════════════════════════════════════════════════════════════╝
```

### Required UI Features

1. **Map View**: Show city layout with buildings and roads
2. **Statistics Panel**: Real-time city metrics
3. **Event Log**: Recent important events
4. **Detail View**: Selected entity information
5. **Command Interface**: User controls
6. **Graph View**: ASCII charts for trends

## Deliverables

```
city-simulation/
├── core/
│   ├── entities.py      # Entity classes
│   ├── buildings.py     # Building classes
│   ├── citizens.py      # Citizen classes
│   ├── economy.py       # Economy system
│   ├── transport.py     # Transportation
│   └── time_system.py   # Time management
├── patterns/
│   ├── observer.py      # Event system
│   ├── factory.py       # Entity factory
│   ├── strategy.py      # AI behaviors
│   ├── singleton.py     # Engine singleton
│   └── decorator.py     # Building modifiers
├── debugging/
│   ├── scenario1_report.md
│   ├── scenario2_report.md
│   ├── scenario3_report.md
│   ├── scenario4_report.md
│   ├── scenario5_report.md
│   └── fixed_code/      # Fixed versions
├── tests/
│   ├── test_units.py
│   ├── test_integration.py
│   └── test_performance.py
├── ui/
│   ├── renderer.py      # ASCII rendering
│   └── interface.py     # User interface
├── simulation.py        # Main simulation loop
├── config.json         # Configuration file
└── README.md           # Complete documentation
```

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| OOP Design | 40 | Class hierarchy, patterns, organization |
| Advanced Features | 30 | Time, pathfinding, statistics |
| Debugging | 40 | Bug fixes, process documentation |
| Testing | 20 | Coverage, quality, performance |
| Visualization | 20 | UI functionality, usability |
| **Total** | **150** |

## Performance Requirements

- Support 1000+ citizens smoothly
- Simulation runs at 30+ updates/second
- Memory usage < 200MB
- Save/load < 2 seconds
- Pathfinding < 10ms per request

## Tips for Success

- **Design First**: Plan your class hierarchy before coding
- **Start Simple**: Get basic simulation working, then add features
- **Debug Systematically**: Use proper debugging tools, not just print
- **Test Continuously**: Write tests as you code
- **Profile Often**: Check performance regularly

## Academic Integrity

This is an individual assignment. You may discuss design patterns and debugging techniques but must implement all code yourself.

---

*This optional grade booster demonstrates mastery of OOP design, debugging skills, and software engineering practices.*