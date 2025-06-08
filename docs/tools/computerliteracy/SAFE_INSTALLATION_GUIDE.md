# A Beginner's Guide to Safely Installing Software

Welcome! As you move into more advanced computing topics, you will often need to install software directly from the internet using your command-line terminal (like PowerShell or Command Prompt). This is a powerful way to get tools, but it comes with a responsibility to be careful.

This guide provides a simple workflow to help you minimize risks when running installation scripts you find online.
The Core Principle: Trust, but Verify

The internet is filled with amazing, free, open-source software. However, a script you run on your computer has the same permissions that you do. It can read your files, install other software, or change system settings.

Therefore, the golden rule is: Never run code from the internet that you do not understand.

You don't have to be a security expert to be safe. You just need to build a habit of checking before you run.
The Risky Pattern: Downloading and Running Blind

You will often see installation instructions for Windows PowerShell that look like this:
PowerShell

# This is an example of a risky command pattern
- Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://some-url.com/install.ps1') or somthing like
- Invoke-Expression ((Invoke-WebRequest -Uri https://some-url.com/install.ps1 -UseBasicParsing).Content) Or, using a more modern alias:
- iwr https://some-url.com/install.ps1 | iex 

(iwr is an alias for Invoke-WebRequest, and iex is an alias for Invoke-Expression)



Why is this risky? This single line of code performs two actions back-to-back:

    It downloads a script from a URL.
    It immediately runs (executes) that script without giving you a chance to see what's inside it.

This is like being handed a sealed box and told to follow the instructions inside without ever looking at them. The script could be perfectly safe, or it could be malicious. You have no way of knowing.
A Simple, Safe Workflow for Evaluating Scripts

Instead of running code blind, take these three simple steps. It only takes a minute and can save you from a major headache.
Step 1: Isolate the URL

Look at the command and find the URL. In our example, it is https://some-url.com/install.ps1. Don't run the command. Just copy the URL.
Step 2: Read the Code

Open your web browser (like Chrome, Firefox, or Edge) and paste the URL into the address bar. This will show you the raw text of the script you were about to run. Again, you don't need to understand every single line. The goal is simply to make the process transparent.
Step 3: Ask a Capable AI for a Security Review

This is where modern tools can help. You can get a simple, step-by-step analysis of the script from an AI assistant.

Copy the entire script's code from your browser. Then, open a capable AI chatbot (like Google Gemini, ChatGPT, or CoPilot) and paste the code into a prompt like the one below.

    Pro-Tip: Use a detailed prompt to get the best results. Here is an excellent template:

Plaintext

I am a student learning about computer security. I am about to run this script to install a program called '[PROGRAM NAME]'. Can you please review this code and:

1.  Explain what the script does step-by-step in simple, easy-to-understand terms?
2.  Point out any lines that change my system's configuration files (like my shell profile) or download other files from the internet?
3.  Are there any obviously dangerous or malicious commands in this script?

The AI will analyze the script and give you a report. Pay close attention to its answers to the three questions. An installer for a legitimate program will typically:

    Download files from an official source (like GitHub).
    Create folders in standard locations (like AppData or Program Files).
    Modify your system's PATH or a shell profile so you can use the program easily.

If the analysis points out strange behavior—like it tries to delete personal files, access your browser passwords, or download more files from weird, unofficial websites—then do not run the script.

By following this simple process, you turn a blind risk into a calculated, informed decision. This is a fundamental skill for any modern developer or scientist.