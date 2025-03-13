import subprocess

def run_script(script_path):
    """Executes a script using subprocess."""
    try:
        # Run the script
        subprocess.run(["python", script_path], check=True)
        print(f"Executed: {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}: {e}")
        exit(1)

def main():
    # Define paths to the scripts
    script1 = r"C:\Users\kaise\OneDrive\Desktop\BE\MAJOR PROJECT\Main\Real-ESRGAN\Real-ESRGAN-master\1_Frame_Splitter.py"
    script2 = r"C:\Users\kaise\OneDrive\Desktop\BE\MAJOR PROJECT\Main\Real-ESRGAN\Real-ESRGAN-master\2_test_main.py"
    script3 = r"C:\Users\kaise\OneDrive\Desktop\BE\MAJOR PROJECT\Main\Real-ESRGAN\Real-ESRGAN-master\3_Video_Merger.py"
    script4 = r"C:\Users\kaise\OneDrive\Desktop\BE\MAJOR PROJECT\Main\Real-ESRGAN\Real-ESRGAN-master\4_Video_Display.py"
    script5 = r"C:\Users\kaise\OneDrive\Desktop\BE\MAJOR PROJECT\Main\Real-ESRGAN\Real-ESRGAN-master\5_Comparator.py"
    script6 = r"C:\Users\kaise\OneDrive\Desktop\BE\MAJOR PROJECT\Main\Real-ESRGAN\Real-ESRGAN-master\5.1_Frame_Comparison.py"

    # Execute the scripts in sequence
    run_script(script1)
    run_script(script2)
    run_script(script3)
    run_script(script4)
    run_script(script5)

if __name__ == "__main__":
    main()
