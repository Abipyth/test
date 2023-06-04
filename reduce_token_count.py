def optimize_prompt_text(prompt_text, max_tokens):
    tokens = prompt_text.split()

    if len(tokens) <= max_tokens:
        return prompt_text

    optimized_tokens = tokens[:max_tokens]
    optimized_prompt = ' '.join(optimized_tokens)

    return optimized_prompt


# Take input from the user
prompt_text = input("Enter the prompt text: ")
max_tokens = int(input("Enter the maximum token count: "))

# Perform token count optimization
optimized_prompt = optimize_prompt_text(prompt_text, max_tokens)

print("\nOptimized Prompt Text:")
print(optimized_prompt)



