



 Bit Protect: A Lightweight System Protection Tool

Bit Protect is a Python-based system utility designed to safeguard your computer from viruses, optimize memory usage, and clean up unnecessary files. It leverages MD5 hashing for virus detection, RAM optimization techniques, and junk file removal utilities.

---

 Features

1. Virus Detection and Removal:
   - Scans files and folders for known viruses using MD5 hash comparison.
   - Provides an option to delete infected files.

2. RAM Optimization:
   - Monitors current memory usage.
   - Boosts available memory to enhance system performance.

3. Junk File Removal:
   - Identifies temporary and unnecessary files based on extensions.
   - Allows users to selectively delete junk files from specific folders.

4. Interactive User Interface:
   - Command-line menu for easy navigation and execution of features.

5. Custom Virus Hash Database:
   - Uses a preloaded file (`hash.txt`) containing virus MD5 hashes for detection.

---

 Getting Started

 Prerequisites
- Python 3.6 or higher
- Required Python modules: `os`, `hashlib`, `psutil`, `time`

 Installation
1. Clone or download the project repository.
2. Ensure Python is installed on your system.
3. Install the required module:
   ```bash
   pip install psutil
   ```
4. Add virus MD5 hashes to the `hash.txt` file (one hash per line).

---

 Usage

1. Run the script:
   ```bash
   python bit_protect.py
   ```
2. Follow the on-screen menu to choose your desired action.

---

 Menu Options

1. Scan and Compare Full System:  
   Scans the entire system for infected files and provides an option to delete them.

2. Scan and Delete Files in a Folder:  
   Scans a specific folder for infected files and provides an option to delete them.

3. Scan and Delete a File:  
   *Feature in progress* - Scan a single file for virus detection.

4. Free RAM Storage and Boost RAM:  
   Displays current memory usage, frees up memory, and boosts performance.

5. Remove Junk Files in a Folder:  
   Identifies and removes temporary or unnecessary files within a specified folder.

6. Exit:  
   Exits the program.

---

 File Structure

- `bit_protect.py`: Main program script.
- `hash.txt`: File containing known virus MD5 hash values.
- Other folders/files: Files and directories to be scanned.

---

 Known Issues and Limitations

- The `Scan and Delete a File` feature is not yet fully implemented.
- May not detect all types of malware due to reliance on MD5 hashes.

---

 Future Enhancements

1. Implement scanning for single files.
2. Add support for SHA-256 hashes for enhanced security.
3. Improve the RAM optimization algorithm.
4. Add a detailed logging mechanism for scan results.
5. Develop a GUI for easier usability.

---

 Contributing

We welcome contributions to improve Bit Protect! If you have any suggestions or enhancements, feel free to fork this repository and submit a pull request.

---



 Contact

For any issues or questions, please contact the developer at [your-email@example.com].

---
