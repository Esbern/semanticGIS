# A Beginner's Guide to Safely Installing Software

Welcome! As you move into more advanced computing topics, you will often need to install software directly from the internet using your command-line terminal (like PowerShell or Command Prompt). This is a powerful way to get tools, but it comes with a responsibility to be careful.

This guide provides a simple workflow to help you minimize risks when running installation scripts you find online.
The Core Principle: Trust, but Verify

The internet is filled with amazing, free, open-source software. However, a script you run on your computer has the same permissions that you do. It can read your files, install other software, or change system settings.

Therefore, the golden rule is: Never run code from the internet that you do not understand.

You don't have to be a security expert to be safe. You just need to build a habit of checking before you run.
The Risky Pattern: Downloading and Running Blind

## Windows
You will often see installation instructions for Windows PowerShell that look like this:
PowerShell

# This is examples of a risky but usfull command pattern
- Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://some-url.com/install.ps1') or somthing like
- Invoke-Expression ((Invoke-WebRequest -Uri https://some-url.com/install.ps1 -UseBasicParsing).Content) Or, using a more modern alias:
- iwr https://some-url.com/install.ps1 | iex 

(iwr is an alias for Invoke-WebRequest, and iex is an alias for Invoke-Expression)

## The macOS & Linux Equivalent: curl | bash

On macOS and Linux, you will often see installation instructions that use a similar pattern to PowerShell, most commonly using curl piped to a shell like bash or sh.

It can look like this:
Bash

# This is an example of a risky but useful command pattern on Linux/macOS
curl -sSL https://some-url.com/install.sh | bash

Sometimes wget is used instead of curl:
Bash

# An equivalent pattern using the 'wget' command
wget -qO- https://some-url.com/install.sh | sh

Why is this risky? Just like its PowerShell counterpart, this single line of code performs two actions back-to-back with no pause for inspection:

    It downloads a script from a URL.
    It immediately pipes (|) the entire content of that script directly into a shell (bash or sh) to be executed.

This is the exact same problem as before: you're being asked to run code from the internet completely blind. It is the digital equivalent of finding a sealed box and being told to follow the instructions inside without ever looking at them. The script could be a harmless installer, or it could be malicious. You have no way of knowing.
A Simple, Safe Workflow for Evaluating Scripts

Instead of running code blind, take these three simple steps. This unified process works for scripts on Windows, macOS, and Linux.

Step 1: Isolate the URL

Look at the command and find the URL. In the example curl -sSL https://some-url.com/install.sh | bash, the URL is https://some-url.com/install.sh. Don't run the command; just copy the URL.

Step 2: Read the Code

Open your web browser (like Chrome, Firefox, or Safari) and paste the URL into the address bar. This will show you the raw text of the script you were about to run. Again, you don't need to understand every single line. The goal is simply to make the process transparent.

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



### Handling Installers (`.exe`, `.dmg`) and System Warnings

Sometimes, you won't be running a script but will instead download a ready-to-install program, often called a "binary." These are files that typically end in `.exe` or `.msi` on Windows, or `.dmg` and `.pkg` on macOS.

Your operating system has a built-in security feature to protect you.

* On **macOS**, you may see a warning that the app "cannot be opened because it is from an unidentified developer."
* On **Windows**, a blue screen may appear stating "Windows protected your PC" from an "unrecognized app."

These warnings are a good thing! They exist because the software developer has not paid a fee to Apple or Microsoft to have their application digitally signed and registered. While many large companies do this, a huge amount of safe, useful, and important open-source software is created by individuals or non-profit groups who do not pay for this certification.

This means you will often see these warnings on completely harmless software. So, how do you decide when it's safe to proceed?

The answer is **Provenance**.

### Provenance: The Key to Trust

Provenance is the history of where your file came from. It’s your job to verify that you are getting the file from the one, true, official source, not from a questionable third party.

Here are the essential rules for verifying provenance:

✔️ **DO: Go Directly to the Source**
Always download software from the official project website. If you want to install QGIS, go to `qgis.org`. If you need Python, go to `python.org`. A quick web search for "[Project Name] official website" is your best first step.

✔️ **DO: Check the URL Before You Click**
Before you download, look at the URL in your browser's address bar. Make sure it matches the official project. A download from `https://qgis.org/downloads/` is trustworthy. A download from `qgis.free-software-downloads.net` is not.

❌ **NEVER: Use Third-Party Download Portals**
Many websites offer to let you download popular programs. They often make money by "bundling" the installer with adware, spyware, or other junk you don't want. Stick to the official sources.

❌ **NEVER: Download "Cracked" Commercial Software**
Trying to get a free version of a paid application is one of the most common ways to get infected with viruses, spyware, or ransomware. These files are almost always modified to include malware. It is never worth the risk.

### Making an Informed Decision

Once you have personally verified the provenance of a file by downloading it from the official project source, you can be confident that it is safe, even if your operating system shows a warning. You are making an *informed decision* to trust the software based on its origin, not blindly clicking "OK."

> **The key lesson is to always think before you click.** Verifying the source of a program is one of the most important and empowering skills you can develop.