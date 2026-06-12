# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The first time I ran the game, the hint direction was completely backwards. Guessing too high told me to go higher, and guessing too low told me to go lower, which made the game unwinnable through normal play. The score also behaved erratically, sometimes awarding points for wrong guesses depending on whether the attempt number was even or odd. On top of that, after submitting a guess the UI would freeze instead of refreshing into a new guess state, so the game felt broken even when the logic was running correctly underneath.
| Input                        | Expected Behavior              | Actual Behavior                | Console Output / Error |
|------------------------------|--------------------------------|--------------------------------|------------------------|
| Guess 60, secret is 50       | "Too High" hint shown          | "Too Low" hint shown           | None                   |
| Wrong guess on attempt 2     | Score decreases by 5           | Score increased by 5           | None                   |
| Any valid guess submitted    | UI refreshes for next guess    | UI froze, no update            | None                   |



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I used Claude Code as my AI coding assistant throughout this project. One example of a correct suggestion was when I asked it to refactor the game logic out of app.py into logic_utils.py and update the import. It moved all four functions cleanly and the app ran correctly afterward, which I verified by running the game end to end in Streamlit. One example of an incorrect suggestion was when I asked it to fix the scoring bug. The first version of the diff it produced still contained the original return current_score + 5 line on even attempts, meaning the fix had not actually landed. I caught this by reviewing the diff carefully and had to prompt it again to remove the even/odd branch entirely, which I then verified by re-running the game and confirming that wrong guesses consistently deducted points.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I verified fixes by re-running the Streamlit app after each change and playing through a few guesses to confirm the behavior matched what I expected. One specific thing I noticed was that when the "Show hint" checkbox was unchecked, the attempts counter was not visually updating correctly. This pointed me to the session state hint persistence logic as something that needed attention beyond just the checkbox toggle. I also ran pytest after adding the test cases to confirm the scoring and hint logic held up in isolation, which gave me more confidence that the fixes were solid and not just masking the issue in the UI.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit works by rerunning your entire Python script from top to bottom every time something changes, whether that is a button click, a text input, or anything else. Any variable you set during one run is gone by the next unless you store it in st.session_state, which persists across reruns. Think of it like a whiteboard that gets erased every few seconds where session_state is the one marker that does not get wiped. Once I understood that, it became clear why hints were disappearing and why the attempt counter was not updating since the values were not being saved anywhere between reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I want to reuse is a specific debugging loop I developed on this project. When something looks wrong, I describe the symptom to the AI, ask it to identify the exact code causing it, then ask for a targeted fix, and finally re-run the app to verify the behavior changed. This keeps the AI focused on one problem at a time instead of making sweeping changes across the whole file. One thing I would do differently next time is ask the AI to revert changes earlier when a suggested fix does not work, since I let a few half applied edits sit longer than they should have. This project changed how I think about AI generated code because it made me realize that AI output needs the same critical review as any other code, and the bugs were real and required human judgment to catch and fix.