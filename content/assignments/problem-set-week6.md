---
title: "Problem Set - Week 6"
date: 2025-10-27
description: "Object-Oriented Programming and Debugging Techniques"
---

# Problem Set 6: OOP and Debugging

This problem set challenges you to build real-world applications using object-oriented design, inheritance, polymorphism, and debugging strategies.

## Exercise 1: Game Character System 🎮
Build a complete RPG character system with abilities and combat mechanics:

```python
from abc import ABC, abstractmethod
import random
from enum import Enum

class DamageType(Enum):
    PHYSICAL = "physical"
    MAGICAL = "magical"
    FIRE = "fire"
    ICE = "ice"
    POISON = "poison"

class Character(ABC):
    """Base class for all game characters"""
    def __init__(self, name, hp, attack, defense, speed):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.status_effects = []  # List of active status effects
        self.abilities = []
        self.experience = 0
        self.level = 1
        
    @abstractmethod
    def special_ability(self, target):
        """Each character class has unique special ability"""
        pass
        
    def take_damage(self, amount, damage_type=DamageType.PHYSICAL):
        """Apply damage with type-based resistances"""
        # Implement damage calculation with defense and resistances
        
    def heal(self, amount):
        """Heal character"""
        
    def is_alive(self):
        return self.current_hp > 0
        
    def gain_experience(self, amount):
        """Level up system"""
        # Implement leveling mechanics
        
    def attack_target(self, target):
        """Basic attack"""
        damage = self.calculate_damage(target)
        target.take_damage(damage)
        return damage

class Warrior(Character):
    """Tank class with high defense"""
    def __init__(self, name):
        super().__init__(name, hp=120, attack=15, defense=20, speed=5)
        self.rage = 0  # Special resource
        
    def special_ability(self, target):
        """Berserker Rage: Double damage, lose defense"""
        # Implement rage mode
        
    def shield_bash(self, target):
        """Stun enemy for one turn"""

class Mage(Character):
    """Magic damage dealer"""
    def __init__(self, name):
        super().__init__(name, hp=60, attack=8, defense=5, speed=10)
        self.mana = 100
        self.spells = ["fireball", "ice_shard", "teleport"]
        
    def special_ability(self, target):
        """Cast random elemental spell"""
        
    def cast_spell(self, spell_name, target):
        """Cast specific spell with mana cost"""

class Rogue(Character):
    """High damage, low health assassin"""
    def __init__(self, name):
        super().__init__(name, hp=80, attack=20, defense=8, speed=15)
        self.stealth = False
        self.combo_points = 0
        
    def special_ability(self, target):
        """Shadow Strike: Critical hit from stealth"""
        
    def vanish(self):
        """Enter stealth mode"""

class Boss(Character):
    """Special boss enemy with phases"""
    def __init__(self, name, phase_count=3):
        super().__init__(name, hp=500, attack=25, defense=15, speed=8)
        self.phase = 1
        self.phase_count = phase_count
        
    def change_phase(self):
        """Boss changes attack pattern at health thresholds"""
        
    def area_attack(self, targets):
        """Attack all enemies"""

# Combat System
class CombatEngine:
    """Manages turn-based combat"""
    def __init__(self, team1, team2):
        self.team1 = team1  # List of characters
        self.team2 = team2
        self.turn_order = []
        self.turn_count = 0
        
    def determine_turn_order(self):
        """Sort by speed attribute"""
        
    def execute_turn(self, attacker, action, target):
        """Process one character's turn"""
        
    def check_victory(self):
        """Check if either team has won"""
        
    def simulate_battle(self):
        """Auto-battle simulation"""
```

Requirements:
- Implement all character classes with unique abilities
- Create a damage calculation system with elemental resistances  
- Add status effects (stun, poison, burn, freeze)
- Implement combo system for Rogue class
- Create boss phase mechanics
- Add loot drops and equipment system

## Exercise 2: Real-Time Stock Trading Simulator 📈
Build a complete stock trading platform with real-time updates:

```python
import random
import time
from datetime import datetime, timedelta
from collections import deque
from typing import Dict, List, Optional

class Stock:
    """Represents a tradable stock with price history"""
    def __init__(self, symbol, name, initial_price):
        self.symbol = symbol
        self.name = name
        self.current_price = initial_price
        self.price_history = deque(maxlen=100)  # Last 100 prices
        self.volume = 0
        self.market_cap = initial_price * 1000000  # Simplified
        self.volatility = random.uniform(0.01, 0.05)
        
    def update_price(self):
        """Simulate price movement based on volatility"""
        # Implement realistic price movement
        change = random.gauss(0, self.volatility)
        self.current_price *= (1 + change)
        self.price_history.append((datetime.now(), self.current_price))
        
    def get_moving_average(self, periods=20):
        """Calculate moving average"""
        
    def get_rsi(self):
        """Calculate Relative Strength Index"""
        
class Portfolio:
    """Manages user's stock holdings"""
    def __init__(self, initial_cash=10000):
        self.cash = initial_cash
        self.holdings = {}  # {symbol: quantity}
        self.transaction_history = []
        self.total_profit_loss = 0
        
    def buy_stock(self, stock: Stock, quantity: int):
        """Execute buy order"""
        
    def sell_stock(self, symbol: str, quantity: int, current_price: float):
        """Execute sell order"""
        
    def get_portfolio_value(self, market: 'StockMarket'):
        """Calculate total portfolio value"""
        
    def get_performance_metrics(self):
        """Return ROI, best/worst trades, etc."""

class Order:
    """Represents a buy/sell order"""
    def __init__(self, order_type, symbol, quantity, price=None):
        self.order_type = order_type  # 'buy', 'sell', 'limit', 'stop-loss'
        self.symbol = symbol
        self.quantity = quantity
        self.price = price  # For limit orders
        self.timestamp = datetime.now()
        self.status = 'pending'
        
class TradingStrategy:
    """Base class for automated trading strategies"""
    def analyze(self, stock: Stock, portfolio: Portfolio):
        """Analyze stock and return trading signal"""
        raise NotImplementedError
        
class MomentumStrategy(TradingStrategy):
    """Buy rising stocks, sell falling ones"""
    def analyze(self, stock: Stock, portfolio: Portfolio):
        # Implement momentum trading logic
        pass
        
class MeanReversionStrategy(TradingStrategy):
    """Buy oversold, sell overbought"""
    def analyze(self, stock: Stock, portfolio: Portfolio):
        # Implement mean reversion logic
        pass

class StockMarket:
    """Simulates a stock market"""
    def __init__(self):
        self.stocks = {}
        self.order_book = []
        self.market_open = True
        self.trading_hours = (9, 16)  # 9 AM to 4 PM
        
    def add_stock(self, stock: Stock):
        """List a new stock"""
        
    def place_order(self, order: Order):
        """Place buy/sell order"""
        
    def execute_orders(self):
        """Match and execute orders"""
        
    def simulate_trading_day(self):
        """Run a full trading day simulation"""
        
    def get_top_movers(self):
        """Return biggest gainers and losers"""

class TradingBot:
    """Automated trading bot"""
    def __init__(self, strategy: TradingStrategy, portfolio: Portfolio):
        self.strategy = strategy
        self.portfolio = portfolio
        self.active = False
        
    def start_trading(self, market: StockMarket):
        """Begin automated trading"""
        
    def backtest(self, historical_data):
        """Test strategy on historical data"""
```

Requirements:
- Implement realistic price movements with volatility
- Create order matching engine for limit orders
- Add technical indicators (RSI, MACD, Bollinger Bands)
- Implement stop-loss and take-profit orders
- Create backtesting framework for strategies
- Add market events (crashes, rallies) that affect all stocks
- Track and display portfolio performance metrics

## Exercise 3: AI-Powered Chess Engine ♟️
Build a chess game with AI opponent using OOP principles:

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Tuple, Optional
import copy

class Color(Enum):
    WHITE = "white"
    BLACK = "black"
    
class PieceType(Enum):
    PAWN = "pawn"
    KNIGHT = "knight"
    BISHOP = "bishop"
    ROOK = "rook"
    QUEEN = "queen"
    KING = "king"

class Position:
    """Represents a board position"""
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
        
    def __hash__(self):
        return hash((self.row, self.col))
        
    def to_chess_notation(self):
        """Convert to chess notation (e.g., 'e4')"""
        return f"{chr(97 + self.col)}{8 - self.row}"

class Piece(ABC):
    """Abstract base class for chess pieces"""
    def __init__(self, color: Color, position: Position):
        self.color = color
        self.position = position
        self.has_moved = False
        self.value = 0  # Piece value for AI evaluation
        
    @abstractmethod
    def get_valid_moves(self, board: 'Board') -> List[Position]:
        """Return all valid moves for this piece"""
        pass
        
    @abstractmethod
    def symbol(self) -> str:
        """Unicode symbol for display"""
        pass
        
    def can_attack(self, target_pos: Position, board: 'Board') -> bool:
        """Check if piece can attack target position"""
        return target_pos in self.get_valid_moves(board)

class Pawn(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)
        self.value = 1
        self.en_passant_vulnerable = False
        
    def get_valid_moves(self, board: 'Board') -> List[Position]:
        """Pawn movement: forward, capture diagonally"""
        # Implement pawn logic including:
        # - Single/double move from starting position
        # - Diagonal captures
        # - En passant
        # - Promotion
        
    def symbol(self) -> str:
        return '♙' if self.color == Color.WHITE else '♟'

class Knight(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)
        self.value = 3
        
    def get_valid_moves(self, board: 'Board') -> List[Position]:
        """L-shaped movement"""
        
    def symbol(self) -> str:
        return '♘' if self.color == Color.WHITE else '♞'

class Bishop(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)
        self.value = 3
        
    def get_valid_moves(self, board: 'Board') -> List[Position]:
        """Diagonal movement"""
        
    def symbol(self) -> str:
        return '♗' if self.color == Color.WHITE else '♝'

class Rook(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)
        self.value = 5
        
    def get_valid_moves(self, board: 'Board') -> List[Position]:
        """Horizontal and vertical movement"""
        
    def symbol(self) -> str:
        return '♖' if self.color == Color.WHITE else '♜'

class Queen(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)
        self.value = 9
        
    def get_valid_moves(self, board: 'Board') -> List[Position]:
        """Combination of rook and bishop movement"""
        
    def symbol(self) -> str:
        return '♕' if self.color == Color.WHITE else '♛'

class King(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)
        self.value = 1000  # Infinite value
        
    def get_valid_moves(self, board: 'Board') -> List[Position]:
        """One square in any direction, plus castling"""
        
    def symbol(self) -> str:
        return '♔' if self.color == Color.WHITE else '♚'

class Move:
    """Represents a chess move"""
    def __init__(self, piece: Piece, from_pos: Position, to_pos: Position, 
                 captured_piece: Optional[Piece] = None):
        self.piece = piece
        self.from_pos = from_pos
        self.to_pos = to_pos
        self.captured_piece = captured_piece
        self.is_castle = False
        self.is_en_passant = False
        self.promotion_piece = None
        
    def to_notation(self) -> str:
        """Convert to algebraic notation"""

class Board:
    """Chess board with piece positions"""
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.move_history = []
        self.captured_pieces = {Color.WHITE: [], Color.BLACK: []}
        self.current_turn = Color.WHITE
        
    def setup_initial_position(self):
        """Place pieces in starting positions"""
        
    def make_move(self, move: Move):
        """Execute a move on the board"""
        
    def undo_move(self):
        """Undo the last move"""
        
    def is_check(self, color: Color) -> bool:
        """Check if king is under attack"""
        
    def is_checkmate(self, color: Color) -> bool:
        """Check if king is in checkmate"""
        
    def is_stalemate(self, color: Color) -> bool:
        """Check if position is stalemate"""
        
    def get_all_valid_moves(self, color: Color) -> List[Move]:
        """Get all legal moves for a color"""
        
    def evaluate_position(self) -> float:
        """Evaluate board position for AI"""

class ChessAI:
    """AI player using minimax algorithm"""
    def __init__(self, color: Color, depth: int = 3):
        self.color = color
        self.depth = depth
        
    def get_best_move(self, board: Board) -> Move:
        """Find best move using minimax with alpha-beta pruning"""
        
    def minimax(self, board: Board, depth: int, alpha: float, beta: float, 
                maximizing: bool) -> Tuple[float, Optional[Move]]:
        """Minimax algorithm with alpha-beta pruning"""
        
    def evaluate_board(self, board: Board) -> float:
        """Heuristic evaluation of board position"""
        # Consider:
        # - Material balance
        # - Piece positions (center control)
        # - King safety
        # - Pawn structure

class ChessGame:
    """Main game controller"""
    def __init__(self, player1_ai: bool = False, player2_ai: bool = True):
        self.board = Board()
        self.board.setup_initial_position()
        self.ai_players = {}
        if player1_ai:
            self.ai_players[Color.WHITE] = ChessAI(Color.WHITE)
        if player2_ai:
            self.ai_players[Color.BLACK] = ChessAI(Color.BLACK)
            
    def play(self):
        """Main game loop"""
        
    def display_board(self):
        """ASCII or Unicode board display"""
```

Requirements:
- Implement all piece movement rules including special moves
- Add check, checkmate, and stalemate detection
- Create minimax AI with alpha-beta pruning
- Implement move validation and board evaluation
- Add opening book for first few moves
- Create position analysis (material count, threats, etc.)
- Support PGN notation for saving/loading games

## Exercise 4: Debugging Utilities
Create a debugging toolkit:

```python
import functools
import time
import traceback
from typing import Any, Callable

class Debugger:
    """Debugging utility class"""
    def __init__(self, verbose=True):
        self.verbose = verbose
        self.call_count = {}
        self.execution_times = {}
        self.errors = []
        
    def trace(self, func):
        """Decorator to trace function calls"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log entry, exit, arguments, return value
            pass
        return wrapper
        
    def time_it(self, func):
        """Decorator to time function execution"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Time the execution
            pass
        return wrapper
        
    def catch_errors(self, func):
        """Decorator to catch and log errors"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Catch exceptions, log them, optionally re-raise
            pass
        return wrapper
        
    def validate_types(self, func):
        """Decorator to validate argument types"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check types match function annotations
            pass
        return wrapper
        
    def memoize(self, func):
        """Decorator to cache function results"""
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            # Cache results for pure functions
            pass
        return wrapper
        
    def get_report(self):
        """Generate debugging report"""
        pass
```

## Exercise 5: Custom Exception Hierarchy
Design exceptions for a web application:

```python
class ApplicationError(Exception):
    """Base exception for application"""
    def __init__(self, message, error_code=None, details=None):
        super().__init__(message)
        self.error_code = error_code
        self.details = details or {}
        self.timestamp = self._get_timestamp()
        
    def _get_timestamp(self):
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
        
    def to_dict(self):
        """Convert to dictionary for API responses"""
        pass

class ValidationError(ApplicationError):
    """Data validation errors"""
    def __init__(self, field, value, message):
        self.field = field
        self.value = value
        super().__init__(message, error_code="VALIDATION_ERROR")

class AuthenticationError(ApplicationError):
    """Authentication failed"""
    pass

class AuthorizationError(ApplicationError):
    """User not authorized"""
    pass

class ResourceNotFoundError(ApplicationError):
    """Requested resource not found"""
    pass

class RateLimitError(ApplicationError):
    """Rate limit exceeded"""
    def __init__(self, limit, reset_time):
        self.limit = limit
        self.reset_time = reset_time
        super().__init__(f"Rate limit {limit} exceeded", error_code="RATE_LIMIT")

# Error handler
class ErrorHandler:
    def __init__(self):
        self.handlers = {}
        
    def register_handler(self, error_class, handler_func):
        """Register handler for specific error type"""
        
    def handle(self, error):
        """Handle error with appropriate handler"""
```

## Exercise 6: Design Patterns Implementation
Implement common design patterns:

```python
# Singleton Pattern
class DatabaseConnection:
    """Singleton database connection"""
    _instance = None
    
    def __new__(cls):
        # Implement singleton pattern
        pass
        
    def query(self, sql):
        """Execute SQL query"""
        pass

# Observer Pattern
class Subject:
    """Observable subject"""
    def __init__(self):
        self._observers = []
        
    def attach(self, observer):
        """Attach an observer"""
        
    def detach(self, observer):
        """Detach an observer"""
        
    def notify(self, event):
        """Notify all observers"""

class Observer(ABC):
    """Observer interface"""
    @abstractmethod
    def update(self, event):
        pass

# Factory Pattern
class AnimalFactory:
    """Factory for creating animals"""
    @staticmethod
    def create_animal(animal_type, **kwargs):
        """Create animal based on type"""
        animals = {
            'dog': Dog,
            'cat': Cat,
            'bird': Bird
        }
        # Implementation here

# Strategy Pattern
class SortStrategy(ABC):
    """Sorting strategy interface"""
    @abstractmethod
    def sort(self, data):
        pass

class QuickSort(SortStrategy):
    def sort(self, data):
        # Implement quicksort
        pass

class MergeSort(SortStrategy):
    def sort(self, data):
        # Implement mergesort
        pass

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
        
    def sort_data(self, data):
        return self.strategy.sort(data)
```

## Exercise 7: Advanced OOP Features
Implement advanced Python OOP features:

```python
class Vector:
    """N-dimensional vector with operator overloading"""
    def __init__(self, *components):
        self.components = list(components)
        
    def __add__(self, other):
        """Vector addition"""
        
    def __sub__(self, other):
        """Vector subtraction"""
        
    def __mul__(self, scalar):
        """Scalar multiplication"""
        
    def __truediv__(self, scalar):
        """Scalar division"""
        
    def __abs__(self):
        """Magnitude of vector"""
        
    def __getitem__(self, index):
        """Get component by index"""
        
    def __setitem__(self, index, value):
        """Set component by index"""
        
    def __len__(self):
        """Number of dimensions"""
        
    def __repr__(self):
        """String representation"""
        
    def dot(self, other):
        """Dot product"""
        
    def normalize(self):
        """Return unit vector"""

class Matrix:
    """Matrix with operator overloading"""
    def __init__(self, data):
        # data is list of lists
        self.data = data
        
    def __add__(self, other):
        """Matrix addition"""
        
    def __mul__(self, other):
        """Matrix multiplication (handles both matrix and scalar)"""
        
    def __pow__(self, n):
        """Matrix power"""
        
    @property
    def T(self):
        """Transpose property"""
        
    def determinant(self):
        """Calculate determinant"""
        
    def inverse(self):
        """Calculate inverse if exists"""
```

## Exercise 8: Debugging Challenge
Debug and fix these problematic classes:

```python
# Bug 1: Memory leak in circular reference
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self  # Creates circular reference
        
# Bug 2: Mutable default argument
class TaskList:
    def __init__(self, tasks=[]):  # Bug: mutable default
        self.tasks = tasks
        
    def add_task(self, task):
        self.tasks.append(task)

# Bug 3: Incorrect inheritance
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):  # Penguins can't fly!
    pass

# Bug 4: Property setter infinite recursion
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius
        
    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
        
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9  # This might cause issues

# Fix all bugs and explain the problems
```

## Exercise 9: Performance Debugging
Create a performance profiler:

```python
import cProfile
import pstats
import io
from memory_profiler import profile  # If available

class PerformanceProfiler:
    """Profile code performance"""
    def __init__(self):
        self.profiles = {}
        
    def profile_function(self, func, *args, **kwargs):
        """Profile a single function call"""
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        # Process and store results
        
    def compare_implementations(self, implementations, test_data):
        """
        Compare performance of different implementations
        implementations: dict of {name: function}
        """
        
    def find_bottlenecks(self, func, *args, **kwargs):
        """Identify performance bottlenecks"""
        
    def memory_usage(self, func, *args, **kwargs):
        """Track memory usage"""
        
    def generate_report(self):
        """Generate performance report"""

# Example: Compare different fibonacci implementations
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

def fib_memoized(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memoized(n-1, cache) + fib_memoized(n-2, cache)
    return cache[n]
```

## Submission Instructions
- Submit all solutions in a single Python file or module
- Include comprehensive docstrings
- Add unit tests for at least 3 classes
- Include examples demonstrating polymorphism and inheritance
- Due: Before Week 7 lecture

## Grading Rubric
- Exercises 1-3: 12 points each
- Exercises 4-6: 11 points each
- Exercises 7-9: 10 points each
- Code quality, tests, and documentation: 11 points
- **Total: 100 points**