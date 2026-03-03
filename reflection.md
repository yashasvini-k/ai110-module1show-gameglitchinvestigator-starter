# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

When I first ran the game, it worked sometimes but behaved inconsistently. On some guesses, the high/low hints were correct, and on others they were wrong. One major bug was that the secret number was being converted to a string on even attempts, which broke the comparison logic. Another issue was that the game logic was mixed directly into app.py, which made it harder to debug and test properly.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot Agent mode and ChatGPT to help debug and refactor the code. One correct suggestion was that the main bug came from converting the secret number to a string on even attempts. I verified this by removing the conversion, rerunning the game, and confirming that the high/low hints worked consistently, and all pytest tests passed. One misleading suggestion was keeping the try/except block inside check_guess() to handle type errors. After removing the string conversion bug, I realized the try/except was unnecessary, and the game worked correctly without it.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when both the game behaved correctly in Streamlit and all tests passed. I ran pytest tests/test_game_logic.py -v, and all 5 tests passed, which confirmed the logic worked correctly with integers. I also manually tested multiple guesses in the browser to make sure even-numbered attempts no longer behaved differently. AI helped me understand what kinds of test cases to write, especially testing integer vs. string inputs.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because Streamlit reruns the entire script every time the user interacts with the app. If the secret number isn’t stored in st.session_state, it gets regenerated on each rerun. I would explain Streamlit reruns like this: every button click refreshes the script from top to bottom, but session state lets you remember important values between runs. The key change I made was storing the secret number in st.session_state so it only gets created once and stays stable during the game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is writing or running tests immediately after fixing a bug to confirm it’s actually resolved. Next time, I would question AI suggestions more critically instead of assuming code like try/except is always needed. This project changed how I see AI-generated code. It’s helpful for finding patterns and bugs, but I learned that I still need to understand the logic and verify everything myself.