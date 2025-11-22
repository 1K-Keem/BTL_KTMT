import subprocess
import os
import shutil
import filecmp
import pytest

def prepare_and_run(test_dir):
    """
    Copy input files from test_dir to root, build and run the program.
    """
    for f in ["input.txt", "desired.txt", "expected.txt", "output.txt", "main"]:
        if os.path.exists(f):
            os.remove(f)
    
    for name in ["input.txt", "desired.txt", "expected.txt"]:
        src = os.path.join(test_dir, name)
        dst = name
        assert os.path.exists(src), f"{src} not found"
        shutil.copy(src, dst)

    try:
        subprocess.run(['g++', '-o', 'main', 'wiener_filter.cpp'], check=True)
        run_cmd = ['./main']
        result = subprocess.run(run_cmd, check=True, capture_output=True, text=True, timeout=10)
        return result.returncode, result.stdout, result.stderr

        # result = subprocess.run(['java', '-jar', 'Mars45.jar', 'nc', 'wiener_filter.asm'], check=True)
        # return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        pytest.fail("Program execution timed out")
    except Exception as e:
        pytest.fail(f"Failed to run program: {str(e)}")

def test_001():
    test_dir = "tests/test_001"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_002():
    test_dir = "tests/test_002"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_003():
    test_dir = "tests/test_003"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_004():
    test_dir = "tests/test_004"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Size not match, please return code 1"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_005():
    test_dir = "tests/test_005"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_006():
    test_dir = "tests/test_006"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_007():
    test_dir = "tests/test_007"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_008():
    test_dir = "tests/test_008"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_009():
    test_dir = "tests/test_009"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Size does not match, please return exit code 1"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_010():
    test_dir = "tests/test_010"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_011():
    test_dir = "tests/test_011"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_012():
    test_dir = "tests/test_012"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_013():
    test_dir = "tests/test_013"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_014():
    test_dir = "tests/test_014"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_015():
    test_dir = "tests/test_015"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"

def test_016():
    test_dir = "tests/test_016"
    returncode, stdout, stderr = prepare_and_run(test_dir)
    assert returncode == 0, f"Program failed with error: {stderr}"
    with open("output.txt") as f1, open("expected.txt") as f2:
        out = f1.read().strip().replace('\r\n', '\n')
        exp = f2.read().strip().replace('\r\n', '\n')
        assert out == exp, "❌ output.txt does not match expected.txt"
