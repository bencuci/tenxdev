# TenXDev

A simple CLI tool that uses Google's Gemini AI to help with coding tasks. Just a personal project to explore AI-assisted development.

## What it does

You give it a request in plain English, and it can:
- Look through your files
- Read code
- Run Python files
- Create, write or modify files
While being constrained with the working directory.

It uses Google's Gemini AI to figure out what you want and do it.

## Setup

1. Install Python 3.13+
2. `pip install -r requirements.txt`
3. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_key_here
   ```

## Usage

```bash
uv run main.py "your request here"
```

Add `--verbose` to see extra details.

## Example Usage

```bash
[bencuci@archlinux tenxdev]$ uv run calculator/main.py "3 + 7 * 2"
┌─────────────┐
│  3 + 7 * 2  │
│             │
│  =          │
│             │
│  20         │
└─────────────┘
[bencuci@archlinux tenxdev]$ uv run main.py 
"When I run the calculator asking '3 + 7 * 2', gives 20 which is incorrect, please fix it."

 - Calling function: get_files_info
 - Calling function: get_file_content
 - Calling function: get_file_content
 - Calling function: write_file

Final response:
I have corrected the precedence of operators in `pkg/calculator.py`. Now, when the 
calculator evaluates the expression '3 + 7 * 2', it will perform the multiplication 
first (7 * 2 = 14) and then the addition (3 + 14 = 17), giving the correct result.

[bencuci@archlinux tenxdev]$ uv run calculator/main.py "3 + 7 * 2"
┌─────────────┐
│  3 + 7 * 2  │
│             │
│  =          │
│             │
│  17         │
└─────────────┘
```

## Calculator Test App

There's a simple calculator in the `calculator/` folder to test the AI agent. It can do basic math operations.

## Configuration

### config.py
Simple settings for the AI agent:
- `MAX_CHARS`: Maximum characters to read from files (10,000)
- `WORKING_DIR`: Default directory to work in ("./calculator")
- `MAX_ITERS`: Maximum AI iterations before stopping (20)

### prompts.py
Contains the system prompt that tells the AI agent how to behave. It instructs the AI to:
- Make function call plans for user requests
- List files, read code, execute Python files, and write files
- Use relative paths (working directory is auto-injected)
- Explain reasoning in responses

## How it works

1. You type a request
2. The AI figures out what to do
3. It calls functions to read/write/run files
4. You get the results

That's it! Pretty simple, but it's been fun to build.
