import subprocess
import time

def run_training():
    # Run the training script in a separate process
    train_process = subprocess.Popen(['python', 'train.py'])
    return train_process

def run_testing():
    # Run the testing script in a separate process
    test_process = subprocess.Popen(['python', 'test.py'])
    return test_process

if __name__ == "__main__":
    # Start training
    train_process = run_training()

    # # Wait for 3600 seconds (1 hour) before starting testing
    # time.sleep(10)

    # Start testing
    test_process = run_testing()

    # Optionally wait for processes to complete
    train_process.wait()
    test_process.wait()
