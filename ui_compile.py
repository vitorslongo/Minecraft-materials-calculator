from pathlib import Path
import subprocess

def compile_all_ui():
    ui_files = list(Path(".").rglob("*.ui"))
    
    for ui_file in ui_files:
        output_file = ui_file.parent / f"ui_{ui_file.stem}.py"
        
        print(f"Compiling: {ui_file} -> {output_file}")
        subprocess.run(["uv", "run", "pyside6-uic", str(ui_file), "-o", str(output_file)])

if __name__ == "__main__":
    compile_all_ui()
