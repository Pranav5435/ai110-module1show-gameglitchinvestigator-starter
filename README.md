# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** Move the logic into `logic_utils.py`. Run `pytest` in your terminal. Keep fixing until all tests pass!

## 📝 Document Your Experience

Hint directions were inverted — "Too High" told players to go higher and "Too Low" told players to go lower, making the game unwinnable. The score also awarded +5 points on even-numbered wrong guesses instead of deducting points. The UI froze after a guess instead of refreshing for the next attempt.

Fixes applied:
- Corrected hint direction text in check_guess() so "Too High" always tells the player to go lower and "Too Low" always tells them to go higher.
- Removed the even/odd branch in update_score() so all wrong guesses consistently deduct 5 points.
- Added st.rerun() after a non-winning guess so the UI refreshes correctly between attempts.
- Refactored all game logic out of app.py and into logic_utils.py so the UI and tests share one implementation.

I used Claude Code as my AI coding assistant. The most useful thing it did was refactor the game logic into logic_utils.py cleanly in one step. The most important thing I learned is that AI-generated code needs the same critical review as any other code — the bugs were real and required human judgment to find and fix.

## 📸 Demo Walkthrough

1. Player selects Normal difficulty (range 1 to 100, 8 attempts)
2. Player enters a guess of 40 and submits
3. Game returns "Too Low" and deducts 5 points from score
4. Player enters a guess of 70
5. Game returns "Too High" and deducts 5 points from score
6. Player enters a guess of 55
7. Game confirms the correct answer, awards win points, and ends the session
8. Player clicks New Game to reset and play again

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/pranavkishore/ai110-module1show-gameglitchinvestigator-starter-1
plugins: anyio-4.13.0
collected 6 items                                                                                            

tests/test_game_logic.py ......                                                                        [100%]

============================================= 6 passed in 0.01s ==============================================
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]