import os
import sys
import hashlib
import time

def init_repo():
    if os.path.exists(".minigit"):
        print("💡 Mini-Git repository already exists here.")
        return

    os.makedirs(".minigit/objects")
    os.makedirs(".minigit/refs")
    
    with open(".minigit/HEAD", "w") as f:
        f.write("ref: refs/heads/main\n")
        
    print("🚀 Initialized empty Mini-Git repository successfully!")

def add_file(filename):
    if not os.path.exists(filename):
        print(f"❌ Error: File '{filename}' milti nahi hai!")
        return

    with open(filename, "rb") as f:
        content = f.read()

    file_hash = hashlib.sha256(content).hexdigest()

    obj_path = os.path.join(".minigit", "objects", file_hash)
    with open(obj_path, "wb") as f:
        f.write(content)

    print(f"✨ File '{filename}' successfully add ho gayi!")
    print(f"🔒 Cryptographic Hash: {file_hash}")

def commit_changes(message):
    objects_dir = os.path.join(".minigit", "objects")
    tracked_files = os.listdir(objects_dir)

    if not tracked_files:
        print("❌ Error: Koi bhi file add nahi hai commit karne ke liye! Pehle 'add' command chalao.")
        return

    timestamp = time.ctime()
    commit_data = f"Timestamp: {timestamp}\nMessage: {message}\nTracked Objects: {len(tracked_files)}"
    
    commit_hash = hashlib.sha256(commit_data.encode()).hexdigest()

    commit_path = os.path.join(objects_dir, commit_hash)
    with open(commit_path, "w") as f:
        f.write(commit_data)

    refs_path = os.path.join(".minigit", "refs", "main")
    with open(refs_path, "w") as f:
        f.write(commit_hash)

    print(f"✅ Commit successful!")
    print(f"📝 Message: '{message}'")
    print(f"🔗 Commit Hash: {commit_hash}")

def show_log():
    refs_path = os.path.join(".minigit", "refs", "main")
    if not os.path.exists(refs_path):
        print("❌ Error: Abhi tak koi commit nahi hua hai!")
        return

    with open(refs_path, "r") as f:
        current_commit_hash = f.read().strip()

    print("\n================== MINI-GIT COMMIT HISTORY ==================")
    commit_path = os.path.join(".minigit", "objects", current_commit_hash)
    
    if os.path.exists(commit_path):
        with open(commit_path, "r") as f:
            commit_content = f.read()
        print(f"Commit Hash: {current_commit_hash}")
        print(commit_content)
        print("-------------------------------------------------------------")
    else:
        print("❌ Commit log mil nahi raha.")
    print("=============================================================\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "init":
            init_repo()
        elif command == "add" and len(sys.argv) > 2:
            add_file(sys.argv[2])
        elif command == "commit" and len(sys.argv) > 3 and sys.argv[2] == "-m":
            commit_changes(sys.argv[3])
        elif command == "log":
            show_log()
        else:
            print("❌ Invalid command usage.")
    else:
        print("❌ Use: py minigit.py init | add <file> | commit -m \"msg\" | log")