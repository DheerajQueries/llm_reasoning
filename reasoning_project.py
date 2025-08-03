from transformers import pipeline

# We can use the same model pipeline as before.
model_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

# The classic logic puzzle that LLMs often fail.
# Correct answer: The ball costs $0.05. (Bat = $1.05, Ball = $0.05, Total = $1.10)
# A common wrong answer from an LLM is $0.10.
logic_problem = "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?"

print("--- DEMONSTRATION OF CHAIN-OF-THOUGHT PROMPTING ---")
print(f"Logic Problem: '{logic_problem}'\n")

# --- Prompt 1: Basic (Standard) Prompt ---
# This asks for the answer directly and will likely produce the wrong result.

standard_prompt = f"""
Question: {logic_problem}
Answer:
"""

print("--- 1. Running STANDARD Prompt ---")
# We increase max_new_tokens as the reasoning takes more space.
standard_output = model_pipeline(standard_prompt, max_new_tokens=200)
print("Model's Answer:")
print(standard_output[0]['generated_text'])


# --- Prompt 2: Advanced (Chain-of-Thought) Prompt ---
# Here, we explicitly tell the model to reason step-by-step.

chain_of_thought_prompt = f"""
Question: {logic_problem}

Let's think step by step.
1. Let B be the cost of the bat and L be the cost of the ball.
2. We are given two pieces of information:
   - The total cost: B + L = 1.10
   - The difference in cost: B = L + 1.00
3. Now, we can substitute the second equation into the first one.
   - (L + 1.00) + L = 1.10
4. Simplify the equation:
   - 2L + 1.00 = 1.10
5. Subtract 1.00 from both sides:
   - 2L = 0.10
6. Divide by 2:
   - L = 0.05
So the final answer is:
"""

print("\n--- 2. Running CHAIN-OF-THOUGHT Prompt ---")
# The "thinking" is part of the prompt. The model just needs to provide the final output.
chain_of_thought_output = model_pipeline(chain_of_thought_prompt, max_new_tokens=200)
print("Model's Answer:")
print(chain_of_thought_output[0]['generated_text'])