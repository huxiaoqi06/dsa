import subprocess
import os
import sys
from pathlib import Path

def find_first_wrong_testcase(executable_path, test_dir=".", timeout=2):
    """
    查找第一个输出不匹配的测试用例
    
    参数:
    - executable_path: 要测试的可执行文件路径
    - test_dir: 测试样例所在的目录
    - timeout: 运行超时时间（秒）
    """
    test_dir = Path(test_dir)
    
    # 按测试编号排序
    test_files = {}
    for file in test_dir.iterdir():
        if file.suffix == '.in':
            test_num = file.stem
            test_files[test_num] = {
                'in': file,
                'out': test_dir / f"{test_num}.out"
            }
    
    if not test_files:
        print("未找到测试样例文件 (*.in)")
        return
    
    print(f"找到 {len(test_files)} 个测试样例")
    print("-" * 50)
    
    # 按测试编号排序
    sorted_tests = sorted(test_files.items(), key=lambda x: x[0])
    
    for test_num, files in sorted_tests:
        in_file = files['in']
        out_file = files['out']
        
        if not out_file.exists():
            print(f"警告: {test_num}.out 不存在，跳过")
            continue
        
        print(f"测试 {test_num}...", end=" ", flush=True)
        
        try:
            # 运行程序，从文件重定向输入
            with open(in_file, 'r') as f:
                result = subprocess.run(
                    [executable_path],
                    stdin=f,
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )
            
            if result.returncode != 0:
                print(f"\n程序运行错误 (退出码: {result.returncode})")
                print(f"标准错误输出:\n{result.stderr}")
                continue
            
            user_output = result.stdout.strip()
            
            # 读取正确输出
            with open(out_file, 'r') as f:
                correct_output = f.read().strip()
            
            # 比较输出
            if user_output == correct_output:
                print("✓ 通过")
            else:
                print("✗ 失败")
                print("-" * 50)
                print(f"第一个失败的测试用例: {test_num}")
                print("\n输入文件内容:")
                print("-" * 20)
                with open(in_file, 'r') as f:
                    print(f.read().strip())
                print("-" * 20)
                
                print(f"\n你的输出:")
                print("-" * 20)
                print(user_output)
                print("-" * 20)
                
                print(f"\n正确输出:")
                print("-" * 20)
                print(correct_output)
                print("-" * 20)
                
                # 显示差异
                print("\n差异分析:")
                print("-" * 20)
                user_lines = user_output.split('\n')
                correct_lines = correct_output.split('\n')
                
                max_len = max(len(user_lines), len(correct_lines))
                for i in range(max_len):
                    user_line = user_lines[i] if i < len(user_lines) else ""
                    correct_line = correct_lines[i] if i < len(correct_lines) else ""
                    
                    if user_line != correct_line:
                        print(f"第 {i+1} 行:")
                        print(f"  你的输出: {repr(user_line)}")
                        print(f"  正确输出: {repr(correct_line)}")
                
                return test_num
                
        except subprocess.TimeoutExpired:
            print(f"\n程序超时 ({timeout}秒)")
            return test_num
        except Exception as e:
            print(f"\n运行出错: {e}")
            return test_num
    
    print("-" * 50)
    print("所有测试样例通过! ✓")
    return None

if __name__ == "__main__":
    # 使用方法示例
    if len(sys.argv) < 2:
        print("使用方法: python test_program.py <可执行文件> [测试目录]")
        print("示例: python test_program.py ./myprogram .")
        sys.exit(1)
    
    executable = sys.argv[1]
    test_directory = sys.argv[2] if len(sys.argv) > 2 else "."
    
    if not os.path.exists(executable):
        print(f"错误: 可执行文件 '{executable}' 不存在")
        sys.exit(1)
    
    find_first_wrong_testcase(executable, test_directory)