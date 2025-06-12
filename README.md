# Cursor Drift Preventer
This simple piece of Python script keeps your computer awake by gently drifting your mouse cursor every so often.
This is handy when you need to step away from your computer but want to keep your session active and prevent it from locking or going to sleep.
Your IT Cybersecurity guy will not like this!
And while you are not present at your desk, do not let your busy colleague send emails offering free coffee to the team!
## How it Works

The script uses the `pyautogui` library to get your current mouse position. Then, it moves the cursor one pixel to the right and immediately back one pixel to the left. This tiny movement is usually enough to trick your system into thinking you're still active. It does this every 30 seconds.

You can stop the script at any time by pressing `Ctrl+C` in the terminal where it's running.

## Requirements

To use this script, you'll need Python installed on your system. You'll also need the `pyautogui` library. You can install it using pip:

```bash
pip install pyautogui
```

## Usage

1.  Save the script as a Python file (e.g., `cursor_drift.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the following command:

    ```bash
    python cursor_drift.py
    ```

5.  To stop the script, press `Ctrl+C` in the terminal.

## Note

- If `pyautogui` is not installed, the script will not run. Make sure to install it as shown in the "Requirements" section.
- On some systems, you might need special permissions for Python to control the mouse. If you run into issues, you might need to look into your system's accessibility or security settings.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
