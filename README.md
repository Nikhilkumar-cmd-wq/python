# Simple Python Keylogger

### [YouTube Demonstration](https://youtu.be/ajet-eT-9hY)

## Project Description
This project demonstrates a simple Python keylogger that captures and logs keystrokes. The keylogger is designed to run in the background and save the keystrokes to a file named `log.txt`. The script uses the `pynput` library to listen to keyboard events and record the keys pressed.

## Languages and Utilities Used

- **Python**

## Environments Used 

- **Windows 11**
- **Visual Studio Code**

## Project Walkthrough:

<p align="center">
Code Overview: <br/>

<img src="https://github.com/user-attachments/assets/584654c3-e61a-45f4-9f5c-3ae620266c10" height="80%" width="80%" alt="Keylogger Code Overview"/>
<br />
<br />
Code in Action: <br/>
<img src="https://github.com/user-attachments/assets/5f4c6eab-df06-4af9-bdaa-ceb7b743571b" height="80%" width="80%" alt="Keystroke logging"/>
<br />
</p>

## How It Works

1. **Listening to Keystrokes**: The script uses the `pynput` library to monitor keyboard events. It captures each key press and stores it in a list.
2. **Processing Keystrokes**: When a key is pressed, the `on_press` function is called. It checks if the key is a character or a special key and adds it to the `keys` list.
3. **Writing to File**: The `write_file` function appends the collected keystrokes to a file named `log.txt` and clears the list to prepare for the next batch of keystrokes.
4. **Running in Background**: The `keyboard.Listener` starts the keylogger and runs it in the background, continuously listening for and processing keystrokes until stopped.


## Responsible Usage

This keylogger is intended solely for educational purposes. It should only be used in environments where you have explicit permission to monitor keystrokes. Unauthorized use of keyloggers can breach privacy laws and lead to legal consequences.


