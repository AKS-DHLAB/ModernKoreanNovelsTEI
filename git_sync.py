import subprocess
import os

repo_dir = r"C:\dev\ModernKoreanNovelsTEI"
os.chdir(repo_dir)

def run_git(args):
    try:
        result = subprocess.run(['git'] + args, capture_output=True, text=True, encoding='utf-8')
        print(f"CMD: git {' '.join(args)}")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
    except Exception as e:
        print(f"Error running git {args}: {e}")

run_git(['status'])
run_git(['pull', 'origin', 'main', '--no-edit'])
run_git(['push', 'origin', 'main'])
